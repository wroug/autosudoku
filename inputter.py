from windmouse.pyautogui_controller import PyautoguiMouseController
from windmouse.core import Coordinate
import pyautogui
from tkinter import ttk
import tkinter as tk
import math
import os
import sys
import re

def main(solution, root, corners):
    for widget in root.winfo_children():
        widget.destroy()

    import re

    def parse_code(s):
        m = re.match(r'r(\d+)c(\d+)=(\d+)', s)
        if m:
            return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
        return None


    def calcoords(ind):
        row = int(ind[0])
        column = int(ind[1])


        corner_1, corner_2 = corners

        x1, y1 = corner_1
        x2, y2 = corner_2

        range_x = x2 - x1
        range_y = y2 - y1

        cell_w = range_x / 9
        cell_h = range_y / 9

        x = int(x1 + cell_w * (column - 0.5))
        y = int(y1 + cell_h * (row - 0.5))

        return x, y



    def move_to(x, y, speed=1000):

        cx, cy = pyautogui.position()
        distance = math.hypot(x - cx, y - cy)
        duration = distance / speed
        pyautogui.moveTo(x, y, duration=duration)


    tk.Label(root, text="Select movement speed", font=("Arial", 12)).pack(pady=(16, 8))

    btn_frame = tk.Frame(root)


    btn_frame.pack(pady=(0, 16), padx=24)

    def on_speed_chosen(speed):
        for widget in root.winfo_children():
            widget.destroy()


        progress = ttk.Progressbar(root, length=300, mode='determinate')

        progress.pack()

        progress['maximum'] = len(solution) - 1

        root.update_idletasks()

        root.update()

        if speed == "fast":
            for task in solution:
                move = parse_code(task)
                if move is None:
                    continue
                move_to(*calcoords(move), 4000)
                pyautogui.click()
                pyautogui.press(str(move[2]))

                progress['value'] += 1
                root.update_idletasks()
                root.update()
            os.execv(sys.executable, [sys.executable] + sys.argv)

        elif speed == "humane":
            for task in solution:
                move = parse_code(task)
                if move is None:
                    continue
                mouse = PyautoguiMouseController()
                mouse.dest_position = calcoords(move)
                mouse.move_to_target()
                pyautogui.click()
                pyautogui.press(str(move[2]))

                progress['value'] += 1
                root.update_idletasks()
                root.update()
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            for task in solution:
                move = parse_code(task)
                if move is None:
                    continue
                #mouse = PyautoguiMouseController()
                #mouse.dest_position = calcoords(move)
                pyautogui.moveTo(*calcoords(move))
                pyautogui.click()
                pyautogui.press(str(move[2]))

                progress['value'] += 1
                root.update_idletasks()
                root.update()
            os.execv(sys.executable, [sys.executable] + sys.argv)


    tk.Button(btn_frame, text="Instant", width=12, command=lambda: on_speed_chosen("instant")).pack(side="left", padx=8)

    tk.Button(btn_frame, text="Fast", width=12, command=lambda: on_speed_chosen("fast")).pack(side="left", padx=8)

    tk.Button(btn_frame, text="Humane", width=12, command=lambda: on_speed_chosen("humane")).pack(side="left", padx=8)