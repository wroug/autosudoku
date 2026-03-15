import subprocess
import inputter
import sys
import os
import pyautogui

def main(grid, root, corners):

    stringe = ""
    for row in grid:
        for item in row:
            stringe += str(item)
    puzzle_string = stringe.replace(" ", ".")

    def get_jar_path():
        if getattr(sys, "frozen", False) or "__compiled__" in globals():
            base = os.path.dirname(sys.executable)
        else:
            base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base, "hodoku.jar")

    subprocess.run(
        ["java", "-jar", get_jar_path(), "/vp", puzzle_string]
    )

    with open("null.out.txt", "r") as f:
        content = f.read()

    solution = content.split("\n")
    solution.pop(0)

    for i, item in enumerate(solution):
        solution[i] = item.strip()[item.find(":")-1:]
    print(solution)
    inputter.main(solution, root, corners)

