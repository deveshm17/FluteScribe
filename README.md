# FluteScribe 🎶

FluteScribe is a Python-based project that converts melodic audio recordings into flute-readable musical notation.

---

## Project Overview

- Converts audio files containing a clear melody into musical notes  
- Designed specifically for **monophonic instruments** such as the flute  
- Extracts the main melody instead of handling full polyphonic music  
- Produces a clean MIDI file suitable for sheet music generation  

---

## Features

- Audio-to-note transcription using pitch detection  
- Filtering of notes to match the playable range of a flute  
- Removal of unnecessary background or overlapping notes  
- MIDI output compatible with notation software like MuseScore  
- Simple and lightweight implementation  

---

## Workflow

- Input audio file (`.wav` or `.mp3`)  
- Melody extraction using pitch detection  
- Flute-specific note filtering  
- MIDI file generation  
- Export to sheet music using notation software  

---

## Use Cases

- Transcribing songs for flute practice  
- Helping music students learn melodies  
- Educational projects in music technology  
- Understanding audio processing and MIDI generation  

---

## Installation

- Ensure Python is installed on the system  
- Install required dependencies using:

```bash
pip install -r requirements.txt
