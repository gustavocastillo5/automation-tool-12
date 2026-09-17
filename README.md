# automation-tool-12

`automation-tool-12` is a high-performance Python-based autoclicker designed for task automation and rapid input simulation. It utilizes low-level system hooks to provide reliable, low-latency clicking across all desktop applications.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features
*   **Dynamic Intervals:** Supports millisecond-precision timing between clicks to mimic human behavior or maximize throughput.
*   **Coordinate Targeting:** Trigger clicks at fixed screen coordinates or follow your current cursor position dynamically.
*   **Hotkey Control:** Start and stop automation instantly using customizable global keyboard shortcuts.
*   **Multi-Button Support:** Toggle between left, right, and middle mouse button emulation via simple configuration.

## Installation

Ensure you have [Python 3.8+](https://www.python.org/) installed, then clone the repository and install the dependencies:

```bash
git clone https://github.com/Developer/automation-tool-12.git
cd automation-tool-12
pip install -r requirements.txt
```

## Usage

To start the autoclicker with default settings (Left Click, 100ms interval), run:

```bash
python main.py --interval 0.1 --button left
```

### Configuration
You can define custom click sequences or specific target zones by modifying the `config.json` file:

```json
{
  "interval": 0.05,
  "button": "left",
  "toggle_key": "f8",
  "coordinates": [500, 500]
}
```

Once running, press your configured **toggle_key** (default: `F8`) to begin clicking. Press it again to terminate the automation process.

## License
Distributed under the MIT License. See `LICENSE` for more information.