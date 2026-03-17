import tkinter as tk
from tkinter import ttk
import threading
import setup
import sys
import subprocess

try:
    result = subprocess.run(["java", "--version"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True)
except FileNotFoundError:
    print("Java is not installed. Please install Java at https://www.java.com/en/download/ and try again.")
    sys.exit(1)

def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        root.destroy()
        sys.exit(0)

sys.excepthook = handle_exception


BG = "#d4d0c8"
FG = "#000000"
FONT = ("MS Sans Serif", 8)


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
root.configure(bg=BG)

style = ttk.Style()
style.theme_use("clam")
style.configure(".", background=BG, foreground=FG, font=FONT)
style.configure("TButton",
    background=BG,
    foreground=FG,
    relief="raised",
    borderwidth=2,
    padding=2,
    font=FONT
)
style.map("TButton",
    background=[("active", BG), ("pressed", BG)],
    relief=[("pressed", "sunken")]
)
style.configure("TProgressbar",
    background="#000080",
    troughcolor="#ffffff",
    borderwidth=2,
    relief="sunken",
    thickness=16
)
style.configure("TCombobox",
    background="#ffffff",
    fieldbackground="#ffffff",
    relief="sunken",
    borderwidth=2,
    font=FONT
)
style.map("TCombobox",
    fieldbackground=[("readonly", "#ffffff")],
    background=[("readonly", BG)]
)

frame = tk.Frame(root, padx=20, pady=20, bg=BG, relief="raised", borderwidth=2)
frame.pack()

root.overrideredirect(True)

combo = ttk.Combobox(frame, values=["9x9"], state="readonly", width=10)
combo.set("9x9")
combo.pack(pady=(0, 15))

btn_frame = tk.Frame(frame, bg=BG)
btn_frame.pack()

ttk.Button(btn_frame, text="Start", command=run, width=8).pack(side="left", padx=5)
ttk.Button(btn_frame, text="Exit", command=stop, width=8).pack(side="left", padx=5)

root.mainloop()