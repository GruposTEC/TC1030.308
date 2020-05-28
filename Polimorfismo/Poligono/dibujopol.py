# pip install pillow
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image


def dibuja_linea():
    w, h = 220, 190
    shape = [(40, 40), (w - 10, h - 10)]
    img = Image.new("RGB", (w, h))
    img1 = ImageDraw.Draw(img)
    img1.line(shape, fill=255, width=0)
    img.show()


def dibuja3():
    im = Image.new("RGB", (200, 200))
    draw = ImageDraw.Draw(im)
    draw.polygon(((50, 150), (150, 150), (100, 50), (50, 150)), fill=255)
    im.show()


def dibuja6():
    im2 = Image.new("RGB", (200, 200))
    draw2 = ImageDraw.Draw(im2)
    draw2.polygon(((50, 150), (150, 150), (180, 100),
                   (150, 50), (50, 50), (20, 100)), fill=255)
    im2.show()
