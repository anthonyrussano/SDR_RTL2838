# Background

This repo contains apps for use with the `RTL2838` USB module.

# Installation

```
sudo apt install rtl-sdr
```

# Usage

## Tuning into FM Radio

Running the following command, should enable you to listen to the FM radio station broadcasting at 89.5 MHz on your computer, provided that the RTL2838 dongle is set up correctly and you have an appropriate antenna connected.

```
./rtl_fm -f 89.5M -M wbfm -s 1000000 -r 48000 -g 29.6 | aplay -r 48000 -f S16_LE
```

This command utilizes the `rtl_fm`` utility to interface with an RTL2838 USB module (commonly known as an RTL-SDR) to receive FM radio, and pipes the output to aplay to play the audio on your computer.

rtl_fm is a command-line tool used for demodulating FM and other analog broadcasts from an RTL2838 dongle.

- `-f 89.5M` sets the frequency to 89.5 MHz
- `-M wbfm:` sets the modulation type to wideband FM (WBFM), which is typically used for FM radio broadcasts.
- `-s 1000000` sets the sample rate to 1,000,000 samples per second (1 Msps). This is the rate at which the RTL-SDR samples the incoming signal.
- `-r 48000` sets the output sample rate to 48,000 samples per second. This is the rate at which the audio will be output after demodulation.
- `-g 29.6` sets the gain to 29.6 dB. Adjusting the gain can help in improving reception, but setting it too high can also introduce noise.
- `|` The pipe (|) takes the output of the command on its left and sends it as input `aplay`, a command-line sound player for Linux. It plays the audio data it receives from `rtl_fm`.
- `-r 48000` sets the playback sample rate to 48,000 samples per second, matching the output rate of rtl_fm.
- `-f S16_LE` sets the audio format. `S16_LE`` stands for 16-bit signed little-endian samples, which is a common audio data format.


## Receive ADS-B signals and track flights

### Install dump1090

```bash
sudo apt install dump1090-mutability
```

Interactive Command-Line Usage:

```bash
dump1090-mutability --interactive
```

### Flask App

#### Requirements

Install python/pipenv:

```bash
Instructions for Ubuntu:

sudo apt update
sudo apt install python3-pip
pip3 install --user pipenv
echo "export PATH=$PATH:~/.local/bin" >> ~/.bashrc
source ~/.bashrc
```

#### Usage

```bash
pipenv install
pipenv run python app.py
```

Example:
![map](https://github.com/anthonyrussano/SDR_RTL2838/blob/a130223834111fff5ccb2b0b1d882b72d28f7ba0/Screenshot%20from%202023-08-06%2023-02-36.png)
