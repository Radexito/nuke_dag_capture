# !/usr/bin/env python
# coding=utf-8
"""Loaded on plugin startup"""

import nuke

import dag_capture
import settings


def plugin_setup():
    """Set up the plugin"""
    settings.load()
    create_nuke_menu()


def create_nuke_menu():
    """Create the menu"""
    nuke_menu = nuke.menu("Nuke")
    nuke_menu.addCommand(
        name="Screenshot",
        command=dag_capture.open_dag_capture,
        tooltip="Open DAG screenshot menu",
    )


if __name__ == '__main__':
    plugin_setup()
