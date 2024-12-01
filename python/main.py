from pyotherside import send as qsend
import sys, io, asyncio
import logging
from pathlib import Path
import json
import configparser

logging.basicConfig()

# Pyotherside waits for all components to be created before running module import callback

script_path = Path(__file__).absolute().parent # /usr/share/harbour-sshazam/python
sys.path.append(str(script_path.parent / 'lib/deps')) # /usr/share/harbour-sshazam/lib/deps

while True: # FIXME
    try:
        import shazamio
    except configparser.MissingSectionHeaderError:
        logging.info("Workarounding configparser.MissingSectionHeaderError...")
        continue
    break

import pasimple

shazam = shazamio.Shazam()
use_rust = 'recognize' in dir(shazam)

duration = 10 # seconds
rate = 41000

def set_settings(d, r, l):
    global duration, rate
    duration, rate = d, r
    shazam.language = l

def load(out):
    if isinstance(out, str):
        out = json.loads(out)
    track = shazamio.Serialize.full_track(out).track
    if not track:
        return (False,'','','')
    return (True, json.dumps(out), track.title, track.subtitle)

async def _recognize(path):
    if use_rust:
        out = await shazam.recognize(path)
    else:
        out = await shazam.recognize_song(path)
    return load(out)

def recognize(path):
    # '/home/defaultuser/Music/Tobu - Higher.mp3'
    return asyncio.run(_recognize(path))

def record():
    f = io.BytesIO()
    pasimple.record_wav(f, duration, sample_rate=rate)
    return asyncio.run(_recognize(f.getvalue()))