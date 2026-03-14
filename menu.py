import tkinter as tk
from tkinter import ttk
import threading
import setup
import sys


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        root.destroy()
        sys.exit(0)

sys.excepthook = handle_exception





stop_event = threading.Event()

def run():
    setup.main(combo.get(), root)

def start():
    print("Start:", combo.get())

def stop():
    root.destroy()
    sys.exit(0)

root = tk.Tk()
root.title("Panel")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

root.overrideredirect(True)

combo = ttk.Combobox(frame, values=["6x6", "9x9", "9x9 Diagonal"], state="readonly", width=10)
combo.set("6x6")
combo.pack(pady=(0, 15))

btn_frame = tk.Frame(frame)
btn_frame.pack()

tk.Button(btn_frame, text="Start", command=run, width=8).pack(side="left", padx=5)
tk.Button(btn_frame, text="Exit", command=stop, width=8).pack(side="left", padx=5)

root.mainloop()