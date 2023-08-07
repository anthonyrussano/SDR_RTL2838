# Installation

```
sudo apt install rtl-sdr
```

# Usage

Tuning into FM Radio:

```
$ rtl_fm -f 89.5M -M wbfm -s 1000000 -r 48000 -g 29.6 | aplay -r 48000 -f S16_LE
```
