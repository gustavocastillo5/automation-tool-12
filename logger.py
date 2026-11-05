import logging
import sys
from pathlib import Path
from typing import Optional


class ClickLogger:
    """Custom logging manager for tracking click automation events and runtime errors."""

    def __init__(
        self, log_file: Optional[Path] = None, level: int = logging.INFO
    ) -> None:
        """Initialize the logger with optional file output and configurable log level.

        Args:
            log_file: Optional Path to write log messages to a file.
            level: Logging level threshold (defaults to logging.INFO).
        """
        self.logger: logging.Logger = logging.getLogger("autoclicker")
        self.logger.setLevel(level)
        self.logger.handlers.clear()

        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        if log_file:
            log_file.parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def log_click(self, x: int, y: int, button: str = "left") -> None:
        """Log a mouse click event with coordinates and mouse button details.

        Args:
            x: Horizontal pixel coordinate of the click.
            y: Vertical pixel coordinate of the click.
            button: Mouse button used ('left', 'right', 'middle').
        """
        self.logger.info("Click executed at (%d, %d) using %s button", x, y, button)

    def log_action(self, action_name: str, details: str = "") -> None:
        """Log a general automation action with optional descriptive details.

        Args:
            action_name: Short identifier for the action executed.
            details: Additional contextual information about the action.
        """
        message = f"Action: {action_name}"
        if details:
            message += f" - {details}"
        self.logger.info(message)

    def log_error(self, message: str, exc: Optional[Exception] = None) -> None:
        """Log error messages with optional exception information.

        Args:
            message: Contextual error description.
            exc: Exception object to include in traceback if present.
        """
        self.logger.error(message, exc_info=exc)


def setup_default_logger(
    log_dir: Optional[Path] = None, debug: bool = False
) -> ClickLogger:
    """Create and return a pre-configured ClickLogger instance.

    Args:
        log_dir: Optional directory path where log output will be stored.
        debug: If True, sets log level to DEBUG; otherwise INFO.

    Returns:
        Configured ClickLogger instance ready for event logging.
    """
    level = logging.DEBUG if debug else logging.INFO
    log_file = log_dir / "autoclicker.log" if log_dir else None
    return ClickLogger(log_file=log_file, level=level)
