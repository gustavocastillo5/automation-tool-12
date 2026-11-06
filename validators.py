import re
from typing import Any, Optional

class ClickValidator:
    """Handles input validation for automation parameters."""

    @staticmethod
    def validate_interval(interval: Any) -> float:
        """Ensures interval is a positive numeric value."""
        try:
            value = float(interval)
            if value < 0.01:
                return 0.01
            return value
        except (ValueError, TypeError):
            return 0.1

    @staticmethod
    def validate_coordinates(x: Any, y: Any) -> tuple[int, int]:
        """Sanitizes screen coordinate inputs."""
        try:
            return int(x), int(y)
        except (ValueError, TypeError):
            return 0, 0

    @staticmethod
    def validate_process_name(name: Any) -> str:
        """Validates process name against basic pattern."""
        if not isinstance(name, str) or not name:
            return ""
        # Basic alphanumeric and underscore validation
        clean_name = re.sub(r'[^a-zA-Z0-9_.]', '', name)
        return clean_name