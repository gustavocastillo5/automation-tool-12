# automation-tool-12

Automation-tool-12 is a high-performance Python-based autoclicker designed for precision tasks and repetitive UI interactions. It utilizes low-level system hooks to provide reliable click execution with minimal CPU overhead.

## Features

*   **Adaptive Intervals:** Set custom click delays with millisecond precision or utilize the "human-mode" to randomize intervals and bypass basic anti-bot triggers.
*   **Dynamic Coordinates:** Configure click points using absolute screen coordinates or dynamic offsets relative to active window elements.
*   **Hotkey Integration:** Start and stop automated sequences instantly using global keyboard listeners, ensuring you remain in control during execution.
*   **Configuration Presets:** Save and load complex click profiles as JSON files to switch between different automation workflows seamlessly.

## Installation

Ensure you have Python 3.8 or higher installed on your system. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/automation-tool-12.git
cd automation-tool-12
pip install -r requirements.txt
```

## Usage

To start a basic click sequence at your current cursor position with a 500ms delay, run the following command:

```bash
python main.py --interval 0.5 --clicks 100
```

For advanced usage, point the tool to a specific configuration file:

```bash
python main.py --config configs/production_run.json
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.