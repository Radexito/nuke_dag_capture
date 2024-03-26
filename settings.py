# !/usr/bin/env python
# coding=utf-8
"""Loads and Saves settings."""
import json
import os
from typing import Optional, Any, Dict

settings_file = os.path.expanduser("~/.nuke/screenshot_settings.ini")
_settings: Dict = {}


def load() -> None:
    """Load settings from file"""
    global _settings
    _create_initial_config()
    with open(settings_file, "r") as f:
        _settings = json.load(f)



def get(name: str) -> Optional[str]:
    """Get setting value by name, on setting not found it raises by default"""
    value = _settings.get(name)
    if value is None:
        raise RuntimeError(f"Setting {name} not found")

    return value


def set_(setting_name: str, value: Any, save_now: bool = True) -> None:
    """Set a setting, by default saves"""
    _settings[setting_name] = str(value)
    if save_now:
        save()


def save() -> None:
    """Save settings to file"""
    with open(settings_file, "w") as f:
        json.dump(_settings, f)


def _create_initial_config() -> None:
    """Creates the initial config file"""
    if os.path.exists(settings_file):
        return

    with open(settings_file, "w") as f:
        json.dump(
            {
                "path": "",
                "increment": "1",
                "zoom": "1",
                "margins": "20",
                "ignore_right": "200",
                "delay": "0",
                "capture": "0",
                "deselect": "1"
            },
            f
        )
