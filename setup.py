import pyautogui
import tkinter as tk
import solver

def main(size):
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

    root2 = tk.Tk()
    root2.title("Setup")

    label = tk.Label(root2, text="Hover over TOP LEFT corner and press ENTER")
    label.pack()

    def on_topleft(event):
        pos_topleft = pyautogui.position()
        label.config(text="Now hover over BOTTOM RIGHT corner and press ENTER")

        def on_bottomright(event):
            pos_bottomright = pyautogui.position()
            corners = (pos_topleft, pos_bottomright)  # ((x1,y1), (x2,y2))
            label.config(text="Done!")
            root2.after(500, root2.destroy)
            print(corners)
            solver.main(corners, size)

        root2.bind("<Return>", on_bottomright)

    root2.bind("<Return>", on_topleft)

    root2.bind("<Return>", on_topleft)
    root2.mainloop()