from __future__ import annotations
from tkinter import Event
from typing import TYPE_CHECKING

from API.source.features.gui.bindings import BACKSPACE

if TYPE_CHECKING:
    from API.source.features.gui.ui_controller import SimpleJoystickUI


class KeyHandler:
    def __init__(self, host: SimpleJoystickUI):
        self.host = host
        self.func_id = self.host.bind('<KeyPress>', self.key_press)
        self.host.bind('<KeyRelease>', self.key_release)
        self.sequence = set()
        self.saving_sequence = False
        self.sequence_saved = False

    def key_release(self, event: Event):
        if not self.sequence_saved:
            self.host.release_all()
            self.sequence.discard(event.keycode)
            self.check_sequence()

    def key_press(self, event: Event):
        if event.keycode == BACKSPACE:
            if self.sequence_saved:
                self.clear_sequence()
            else:
                self.sequence_saved = True
        elif self.sequence_saved:
            self.clear_sequence()
            self.sequence.add(event.keycode)
        elif event.keycode not in self.sequence:
            self.sequence.add(event.keycode)
        self.host.release_all()
        self.check_sequence()

    def check_sequence(self):
        for binding in self.host.binds:
            if self.sequence == binding.sequence:
                if binding.button:
                    binding.button.set_pressed()
                return binding

    def clear_sequence(self):
        self.sequence.clear()
        self.sequence_saved = False
