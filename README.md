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

## TODO

Listen to FM Radio: This is a basic starting point, but it's always fun to use your SDR as a traditional FM radio receiver.

Aircraft Tracking with ADS-B: Aircraft transmit data about their position, altitude, and other details using Automatic Dependent Surveillance-Broadcast (ADS-B). With an SDR and software like Dump1090, you can track aircraft in real-time within your vicinity.

Satellite Image Reception: You can receive weather satellite images directly from satellites like NOAA and Meteor using your SDR. With software like WXtoImg, you can decode and view these images.

Decode Digital Voice: With software like DSD (Digital Speech Decoder), you can decode and listen to various digital voice protocols used by emergency services, businesses, and more.

Capture Images from the ISS: The International Space Station occasionally transmits SSTV (Slow Scan TV) images that you can receive and decode using your SDR.

Listen to International Shortwave Radio: Explore shortwave bands and listen to broadcasts from around the world.

Analyze GSM Signals: While it's illegal to intercept private communications, you can analyze the GSM spectrum and understand its structure.

Radio Astronomy: You can use your SDR for basic radio astronomy experiments, like detecting the rotation of the Milky Way or observing solar flares.

Capture and Decode Pagers: In some areas, pagers are still in use, especially in medical settings. You can capture and decode pager transmissions (but be cautious about privacy laws in your jurisdiction).

RDS and TMC Decoding: Decode Radio Data System (RDS) information transmitted alongside FM radio, which can include station names, song titles, and even Traffic Message Channel (TMC) data in some regions.

Explore Unknown Signals: Use software like SDR# or SDR Console in combination with the "waterfall" display to visually explore the RF spectrum. If you come across unknown signals, you can use tools and communities like SigIDWiki to help identify them.

RF Replay Attacks: Capture and replay RF signals, like those from remote-controlled outlets or garage doors. This can be done using tools like Universal Radio Hacker. (Always ensure you have permission and are acting within legal guidelines.)
