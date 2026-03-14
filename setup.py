import pyautogui
import tkinter as tk
import solver

def main(size, root):
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    root2 = tk.Tk()

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
    label = tk.Label(root2, text="Hover over TOP LEFT corner and press ENTER")
    label.pack()
    root2.attributes('-topmost', True)

    def on_topleft(event):
        pos_topleft = pyautogui.position()
        label.config(text="Now hover over BOTTOM RIGHT corner and press ENTER")
        root2.attributes('-topmost', True)

        root2.focus_force()

        def on_bottomright(event):
            pos_bottomright = pyautogui.position()
            corners = (pos_topleft, pos_bottomright)  # ((x1,y1), (x2,y2))
            label.config(text="Done!")
            root2.after(500, root2.destroy)
            print(corners)
            solver.main(corners, size, root)

        root2.bind("<Return>", on_bottomright)

    root2.bind("<Return>", on_topleft)
    root2.focus_force()
    root2.bind("<Return>", on_topleft)
    root2.lift()

    root2.mainloop()