import os
import tkinter as tk
from gui import MacroApp


CONSOLE_COLS = 40
CONSOLE_LINES = 15

def set_console_size(cols: int, lines: int):
    os.system(f"mode con: cols={cols} lines={lines}")

def main():
    set_console_size(CONSOLE_COLS, CONSOLE_LINES)
    root = tk.Tk()
    app = MacroApp(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()