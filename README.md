# Macros_MouseClicker

Macros_MouseClicker is a lightweight Windows desktop utility that adds configurable extra left-clicks when you click the mouse. It is built with Python, a simple Tkinter GUI, and a small macro engine that watches for real mouse clicks and injects additional clicks automatically.

## Features

- Add extra left mouse clicks per activation
- Simple GUI for configuring click count
- Enable/disable macro with a toggle button
- Emergency stop using the `Esc` key
- Avoids clicking inside its own application window

## Requirements

- Windows 10 / 11
- Python 3.8+ installed
- `pynput` package

## Installation

1. Clone or copy the repository to your machine.
2. Create and activate a Python virtual environment in the repository root (recommended):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the required package:

   ```powershell
   pip install -r requirements.txt
   ```

## Running the Application

From the `Macros_MouseClicker/src` folder, run:

```powershell
python main.py
```

Alternatively, use the included `run_as_admin.bat` file to launch the app with administrator privileges if needed.

## How to Use

1. Enter the number of clicks you want the macro to generate for each manual left mouse click.
2. Click the `Enable macro` button to activate the macro.
3. When the macro is active, each physical click will produce the configured number of clicks.
4. Click the button again to disable the macro.
5. Press `Esc` anytime to immediately stop the macro.

## Notes

- The application uses Windows API polling to detect left mouse button events.
- The macro will not generate extra clicks while the pointer is inside the app window.
- The GUI is intentionally small and simple so it does not interfere with normal mouse usage.

## Project Structure

- `src/main.py` — application entry point
- `src/gui.py` — Tkinter user interface
- `src/macro_engine.py` — macro click engine and input handling
- `requirements.txt` — Python dependency list

## License

This project does not include a specific license. Feel free to use and modify it for your own needs.