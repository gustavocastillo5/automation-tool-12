# automation-tool-12

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

automation-tool-12 is a lightweight Python autoclicker built for precise, repeatable mouse automation. It delivers reliable click sequences for testing, data entry, and repetitive tasks without unnecessary overhead.

## Features
- Configurable click intervals with millisecond precision
- Support for multiple click coordinates executed in sequence
- Hotkey-based start, stop, and pause controls
- Optional randomization of timing and click count to simulate natural input

## Installation

```bash
git clone https://github.com/Developer/automation-tool-12.git
cd automation-tool-12
pip install -r requirements.txt
```

## Usage

Create a configuration file with your target coordinates and timing, then run:

```bash
python main.py --config config.json
```

The tool runs in the background and activates via the configured hotkey (default F8). Press the hotkey again to stop.