from PIL import Image, ImageOps
import io
import ddddocr

buffer = io.BytesIO()
ocr = ddddocr.DdddOcr(show_ad=False)

def main(corners, size):
    print("Solving...")
    griddivide = int(size[0])
    img = Image.open("./screenshot.png")
    x1, y1, x2, y2 = corners[0]+corners[1]
    cropped = img.crop((x1, y1, x2, y2))

    cropped.save("./grid.png")
    print(cropped.size)
    size = cropped.size
    imggrid = [[None]*griddivide for _ in range(griddivide)]
    numgrid = [[None]*griddivide for _ in range(griddivide)]
    for ydivision in range(0, griddivide):
        y1 = int((size[1] / griddivide) * ydivision)
        y2 = int((size[1] / griddivide) * (ydivision + 1))
        for xdivision in range(0, griddivide):
            print(f"Processing cell {ydivision}-{xdivision}")
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
            tempimg.save(buffer, format="PNG")
            tempimg.save(f"./digits/{ydivision}-{xdivision}.png")
            digit = ocr.classification(buffer.getvalue())        #pytesseract.image_to_string(tempimg, config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789').strip()
            numgrid[ydivision][xdivision] = int(digit) if digit != "" else " "

    out = ""
    for i in numgrid:
        for j in i:
            out += str(j)
        out += "\n"

    print(out.replace(" ", "·"))

