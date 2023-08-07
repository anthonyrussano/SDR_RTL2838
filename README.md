# Background

This repo contains apps for use with the `RTL2838` USB module.

# Installation

```
sudo apt install rtl-sdr
```

# Usage

Tuning into FM Radio:

```
rtl_fm -f 89.5M -M wbfm -s 1000000 -r 48000 -g 29.6 | aplay -r 48000 -f S16_LE
```
Receive ADS-B signals and track flights:

```
sudo apt install dump1090-mutability
dump1090-mutability --interactive
```

Flask App Usage:

```
Start capturing metrics...
Use the binary included in this repo:
./dump1090 --quiet --write-json json/
Run flask app
pipenv install flask
pipenv run python app.py
```
Example:
![map](https://github.com/anthonyrussano/SDR_RTL2838/blob/a130223834111fff5ccb2b0b1d882b72d28f7ba0/Screenshot%20from%202023-08-06%2023-02-36.png)
