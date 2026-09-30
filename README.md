# automation-tool-12

`automation-tool-12` is a high-performance Python-based autoclicker designed for task automation and repetitive interface interaction. It utilizes low-level system hooks to provide reliable performance with minimal CPU overhead.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

*   **Configurable Interval Control:** Set millisecond-precision click intervals to match any application requirement.
*   **Dynamic Targeting:** Built-in coordinates capture tool to lock clicks to specific UI elements regardless of window size.
*   **Hotkey Integration:** Start and stop execution instantly using customizable keyboard shortcuts without losing focus on the target window.
*   **Human-Mimicry Mode:** Optional randomization jitter to prevent detection in systems that monitor for perfect, rhythmic inputs.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/automation-tool-12.git
cd automation-tool-12
pip install -r requirements.txt
```

## Usage

To run the tool with default settings (100ms interval), execute:

```bash
python main.py --interval 0.1
```

To enable the human-mimicry randomization feature with a 50ms variance:

```bash
python main.py --interval 0.5 --randomize 0.05
```

Once running, press `F8` to start the clicking process and `F9` to terminate the script immediately.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.