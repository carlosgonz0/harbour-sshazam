# SShazam

Shazam for SailfishOS. WIP

## Building

Make sure to set the variables in SPEC file corrently. They're placed at the top of the file and can container eathier `yes` or `no` in them.

1. `package_library`: wether to package the library with the app. If you set it to `no` then you should install the library on your phone yourself and disable sandboxing.
    - To install the library, run this command to install Rust version: `python3 -m pip install shazamio pasimple --user --upgrade` and this to install Python-only version: `python3 -m pip install git+https://github.com/roundedrectangle/ShazamIO pasimple --user --upgrade`
2. `use_rust`: wether to use Rust or pure Python. Rust is recommended, but not supported on armv7hl.