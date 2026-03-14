from PIL import Image, ImageOps
import io
import ddddocr
from tqdm import tqdm
import tkinter as tk
from tkinter import ttk
import sys
import os
import solver

BG = "#d4d0c8"
FG = "#000000"
FONT = ("MS Sans Serif", 8)

ocr = ddddocr.DdddOcr(show_ad=False)


def draw_grid(root, grid, scale=1.0):
    for widget in root.winfo_children():
        widget.destroy()

    font_size = int(12 * scale)
    pad = int(5 * scale)
    size = len(grid)
    box_w = 3
    box_h = 2 if size == 6 else 3

    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            left = 2 if x % box_w == 0 and x != 0 else 0
            top  = 2 if y % box_h == 0 and y != 0 else 0

            frame = tk.Frame(root, bg="black", bd=0)
            frame.grid(row=y, column=x, padx=(left, 0), pady=(top, 0))
            label = tk.Label(frame, text=str(val) if val != " " else "", width=3, height=1, font=("MS Sans Serif", font_size), relief="flat", borderwidth=0, bg="white", fg="black", highlightbackground="#808080", highlightthickness=1)
            label.pack()

def main(corners, size, root, img):
    root.geometry("")
    root.configure(bg=BG)
    print("Solving...")
    griddivide = int(size[0])
    root3 = root #tk.Tk
    for widget in root.winfo_children():
        widget.destroy()

    progress = ttk.Progressbar(root3, length=300, mode='determinate')
    progress.pack()


    progress['maximum'] = griddivide * griddivide


    #img = Image.open("./screenshot.png")
    x1, y1, x2, y2 = corners[0]+corners[1]
    cropped = img.crop((x1, y1, x2, y2))

    #cropped.save("./grid.png")
    print(cropped.size)
    size = cropped.size
    imggrid = [[None]*griddivide for _ in range(griddivide)]
    numgrid = [[None]*griddivide for _ in range(griddivide)]

    total = griddivide * griddivide
    with tqdm(total=total, desc="Processing cell 0-0") as pbar:
        for ydivision in range(0, griddivide):
            y1 = int((size[1] / griddivide) * ydivision)
            y2 = int((size[1] / griddivide) * (ydivision + 1))
            for xdivision in range(0, griddivide):
                pbar.set_description(f"Processing cell {ydivision}-{xdivision}")
                x1 = int((size[0]/griddivide)*xdivision)
                x2 = int((size[0]/griddivide)*(xdivision+1))
                imggrid[ydivision][xdivision] = cropped.crop((x1, y1, x2, y2))
                tempimg = ImageOps.autocontrast(imggrid[ydivision][xdivision].convert("L")).resize((256,256))
                tempsize = tempimg.size
                tempimg = tempimg.crop((
                    int(tempsize[0] / 6),
                    int(tempsize[1] / 6),
                    int(tempsize[0] / 6) * 5,
                    int(tempsize[1] / 6) * 5
                ))
                buffer = io.BytesIO()
                tempimg.save(buffer, format="PNG")
                #tempimg.save(f"./digits/{ydivision}-{xdivision}.png")
                digit = ocr.classification(buffer.getvalue())
                buffer.seek(0)
                numgrid[ydivision][xdivision] = int(digit if digit in "0123456789" else 0) if digit != ""  else " "
                pbar.update(1)
                progress['value'] += 1
                root3.update_idletasks()
                root3.update()

    out = ""
    for i in numgrid:
        for j in i:
            out += str(j)
        out += "\n"

    print(out.replace(" ", "·"))

    def stop():
        root.destroy()
        sys.exit(0)

    def correct():
        solver.main(numgrid, root, corners)

    def incorrect():
        os.execv(sys.executable, [sys.executable] + sys.argv)

    draw_grid(root, numgrid)

    cols = len(numgrid[0])

    confirm_frame = tk.Frame(root, bg=BG)
    confirm_frame.grid(row=len(numgrid), column=0, columnspan=cols, pady=10)
    tk.Label(confirm_frame, text="Is this correct?", bg=BG, fg=FG, font=FONT).pack()
    btn_row = tk.Frame(confirm_frame, bg=BG)
    btn_row.pack()
    ttk.Button(btn_row, text="Yes", command=correct, width=8).pack(side="left", padx=5)
    ttk.Button(btn_row, text="No", command=incorrect, width=8).pack(side="left", padx=5)

    exit_frame = tk.Frame(root, bg=BG)
    exit_frame.grid(row=len(numgrid) + 1, column=0, columnspan=cols, sticky="ew")
    ttk.Button(exit_frame, text="Exit", command=stop).pack(fill="x")

    root.update()



