import tkinter as tk
from gui import MacroApp

def main():
    root = tk.Tk()
    app = MacroApp(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()