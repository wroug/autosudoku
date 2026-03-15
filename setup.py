import pyautogui
import tkinter as tk
from tkinter import ttk
import read

BG = "#d4d0c8"
FG = "#000000"
FONT = ("MS Sans Serif", 8)

def main(size, root):

    #screenshot.save("screenshot.png")
    root2 = tk.Tk()
    root2.configure(bg=BG)

    for widget in root.winfo_children():
        widget.destroy()
    root.update_idletasks()
    root.minsize(0, 0)
    root.geometry("1x1")
    root.update()

    root2.attributes('-topmost', True)
    root2.overrideredirect(False)
    root2.focus_force()

    for widget in root2.winfo_children():
        widget.destroy()

    root2.title("Setup")
    root2.focus_force()
    label = tk.Label(root2, text="Hover your mouse over the TOP LEFT corner  of the sudoku and press ENTER", bg=BG, fg=FG, font=FONT, padx=10, pady=10)
    label.pack()
    root2.attributes('-topmost', True)

    def on_topleft(event):
        pos_topleft = pyautogui.position()
        label.config(text="Now hover over your mouse over the BOTTOM RIGHT corner of the sudoku and press ENTER")
        root2.attributes('-topmost', True)

        root2.focus_force()

        def on_bottomright(event):
            pos_bottomright = pyautogui.position()
            corners = (pos_topleft, pos_bottomright)  # ((x1,y1), (x2,y2))
            if corners[0][0] > corners[1][0] or corners[0][1] > corners[1][1]:
                label.config(text="Incorrect positioning!")
                root2.after(500, root2.destroy)
                main(size, root)
            label.config(text="Done!")
            root2.after(500, root2.destroy)
            print(corners)
            screenshot = pyautogui.screenshot()
            read.main(corners, size, root,screenshot)

        root2.bind("<Return>", on_bottomright)

    root2.bind("<Return>", on_topleft)
    root2.focus_force()
    root2.bind("<Return>", on_topleft)
    root2.lift()

    root2.mainloop()