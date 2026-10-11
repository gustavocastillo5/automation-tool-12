# automation-tool-12

`automation-tool-12` is a high-performance Python-based autoclicker designed for task automation and repetitive interface interaction. It utilizes the `pynput` library to deliver low-latency mouse event simulation with minimal system resource consumption.

## Features

*   **Configurable CPS:** Precisely control clicks-per-second settings to mimic human interaction or maximize speed.
*   **Dynamic Hotkeys:** Start or stop the automation sequence instantly using customizable global keyboard shortcuts.
*   **Coordinate Targeting:** Optional screen coordinate locking to ensure clicks are performed at specific pixels.
*   **Anti-Detection Layer:** Implements randomized jitter and interval variance to bypass basic rate-limiting mechanisms.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/automation-tool-12.git
cd automation-tool-12
pip install -r requirements.txt
```

## Usage

To start the autoclicker with default settings, execute the following command in your terminal:

```bash
python main.py --cps 10
```

For advanced usage, you can define specific target coordinates and toggle the anti-detection mode:

```bash
python main.py --cps 15 --x 500 --y 500 --jitter
```

Press `F6` (default) at any time to toggle the clicking state. Use `Ctrl+C` in the terminal to terminate the process.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.