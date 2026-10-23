# automation-tool-12

`automation-tool-12` is a high-performance Python-based autoclicker designed for task automation and repetitive interface testing. It provides a lightweight, low-latency solution for simulating mouse events with customizable timing and coordinate precision.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

*   **Precision Targeting:** Define specific X/Y screen coordinates or utilize the current cursor position to execute clicks.
*   **Variable Intervals:** Configure millisecond-accurate delays between clicks to mimic human behavior and avoid detection.
*   **Safety Hotkeys:** Global interrupt support allows you to instantly pause or terminate the script using a dedicated keyboard shortcut.
*   **Multi-Click Sequences:** Support for scripted click patterns and loop counts to handle complex automation workflows.

## Installation

Ensure you have [Python 3.8+](https://www.python.org/) installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/automation-tool-12.git
cd automation-tool-12
pip install -r requirements.txt
```

## Usage

To run the tool with default settings (100ms interval, infinite loop), execute the following command in your terminal:

```bash
python main.py --interval 0.1 --clicks 0
```

### Configuration Options
*   `--interval`: Set time between clicks in seconds.
*   `--clicks`: Number of iterations (set to 0 for infinite).
*   `--button`: Select mouse button (`left`, `right`, `middle`).

**Example:**
To perform 50 right-clicks with a 0.5-second delay:
```bash
python main.py --button right --clicks 50 --interval 0.5
```

*Note: You may need to grant Accessibility permissions (macOS) or run as Administrator (Windows) for the script to successfully inject inputs into other applications.*

## License

Distributed under the MIT License. See `LICENSE` for more information.