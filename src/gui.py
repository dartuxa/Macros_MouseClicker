import tkinter as tk
from tkinter import messagebox
import threading
from macro_engine import MouseClicker

class MacroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Macro's Mouse Clicker")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        # Initalize the macro engine
        self.clicker = MouseClicker()
        self.update_clicker_window_bounds()

        # Start the macro loop in a separate thread to prevent GUI freezing
        self.clicker_thread = threading.Thread(target=self.clicker.run_loop, daemon=True)
        self.clicker_thread.start()

        self.create_widgets()

    def update_clicker_window_bounds(self):
        self.clicker.window_bounds = (
            self.root.winfo_rootx(),
            self.root.winfo_rooty(),
            self.root.winfo_rootx() + self.root.winfo_width(),
            self.root.winfo_rooty() + self.root.winfo_height()
        )
        self.root.after(100, self.update_clicker_window_bounds)

    def create_widgets(self):
        # Text mark for input field
        self.label = tk.Label(self.root, text="Number of clicks per activation:", font=("Arial", 11))
        self.label.pack(pady=15)

        # Input field
        self.click_entry = tk.Entry(self.root, font=("Arial", 12), width=10, justify="center")
        self.click_entry.insert(0, "2")  # Default value
        self.click_entry.pack(pady=2)

        # Toggle button
        self.toggle_btn = tk.Button(
            self.root, 
            text="Enable macro", 
            font=("Arial", 12, "bold"),
            bg="green", 
            fg="white",
            command=self.toggle_macro,
            width=18,
            height=2
        )
        self.toggle_btn.pack(pady=20)

        # User hint
        self.info_label = tk.Label(self.root, text="Press ESC for emergency stop", font=("Arial", 8), fg="gray")
        self.info_label.pack()

    def toggle_macro(self):
        # Check if the input is a valid integer
        try:
            clicks_count = int(self.click_entry.get())
            if clicks_count <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer greater than 0")
            return

        # Switch the state of the macro in the engine
        is_running = self.clicker.toggle(clicks_count)

        # Change the appearance of the button depending on the state
        if is_running:
            self.toggle_btn.config(text="Disable macro", bg="red")
            # Block the input field while the macro is running
            self.click_entry.config(state="disabled")
        else:
            self.toggle_btn.config(text="Enable macro", bg="green")
            # Unblock the input field
            self.click_entry.config(state="normal")