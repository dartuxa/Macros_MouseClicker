import time
import threading
import ctypes
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key

class MouseClicker:
    def __init__(self):
        self.mouse = Controller()
        self.running = False      # Flag to indicate if the macro is active
        self.active = True        # Flag to indicate if the background thread is alive
        self.clicks_per_click = 1 # Number of clicks to perform per activation
        self.window_bounds = None # GUI coordinates to avoid clicking on the window itself
        self.synthetic_clicking = False

        # Start the keyboard listener (Esc)
        self.keyboard_listener = Listener(on_press=self.on_key_press)
        self.keyboard_listener.start()

        # Instead of MouseListener use asking of the current mouse state via WinAPI
        self._mouse_poll_thread = threading.Thread(target=self._mouse_poll_loop, daemon=True)
        self._mouse_poll_thread.start()

    def is_pointer_outside_window(self):
        if not self.window_bounds:
            return True
        x, y = self.mouse.position
        x0, y0, x1, y1 = self.window_bounds
        return not (x0 <= x <= x1 and y0 <= y <= y1)

    def start_clicking(self, clicks_count):
        """Starts the macro and passes it the number of clicks"""
        self.clicks_per_click = clicks_count
        self.running = True

    def stop_clicking(self):
        """Pauses the macro"""
        self.running = False

    def toggle(self, clicks_count):
        """Toggles the macro state"""
        if self.running:
            self.stop_clicking()
        else:
            self.start_clicking(clicks_count)
        return self.running

    def on_key_press(self, key):
        """Emergency stop of the macro when Esc is pressed"""
        if key == Key.esc:
            print("[Macro] ESC pressed. Emergency shutdown.")
            self.running = False

    def _mouse_poll_loop(self):
        """Asks the current state of the left mouse button via WinAPI and adds additional clicks
        only when the button transitions to a pressed state (edge trigger)."""
        GetAsyncKeyState = ctypes.windll.user32.GetAsyncKeyState
        VK_LBUTTON = 0x01
        prev_pressed = False
        while self.active:
            try:
                # The most significant bit indicates the current state of the button
                pressed = (GetAsyncKeyState(VK_LBUTTON) & 0x8000) != 0
            except Exception:
                pressed = False

            # detect the click (transition from released -> pressed)
            if pressed and not prev_pressed:
                if self.running and self.is_pointer_outside_window() and not self.synthetic_clicking:
                    self.synthetic_clicking = True
                    try:
                        extra_clicks = max(0, self.clicks_per_click - 1)
                        for _ in range(extra_clicks):
                            self.mouse.click(Button.left, 1)
                            time.sleep(0.01)
                    finally:
                        self.synthetic_clicking = False

            prev_pressed = pressed
            time.sleep(0.01)

    def run_loop(self):
        """Background loop for supporting listeners."""
        print("[Macro] Background thread started.")
        while self.active:
            time.sleep(0.1)
