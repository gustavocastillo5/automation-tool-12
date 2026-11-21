# automation-tool-12

`automation-tool-12` is a high-performance, lightweight Python autoclicker designed for rapid task execution and UI testing. It provides a robust command-line interface to automate mouse interactions with sub-millisecond precision.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features
*   **Variable Click Rates:** Configure clicks-per-second (CPS) dynamically to suit specific testing requirements.
*   **Customizable Hotkeys:** Easily start or stop the automation process using globally registered keyboard shortcuts.
*   **Precision Targeting:** Supports coordinate-based clicking or current-mouse-position mode for versatile workflow integration.
*   **Anti-Detection Jitter:** Includes an optional randomized offset feature to mimic human movement patterns.

## Installation

Ensure you have [Python 3.8+](https://www.python.org/) installed, then clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/automation-tool-12.git
cd automation-tool-12
pip install -r requirements.txt
```

## Usage

You can execute the tool via the command line by specifying the click frequency and the desired duration.

**Basic execution:**
```bash
python main.py --cps 10 --duration 60
```

**Run with jitter for human-like behavior:**
```bash
python main.py --cps 5 --jitter 15
```

### Configuration
* `--cps`: Number of clicks per second.
* `--duration`: Total time to run in seconds (default is infinite).
* `--button`: Specify the mouse button (`left`, `right`, or `middle`).

## License
Distributed under the MIT License. See `LICENSE` for more information.