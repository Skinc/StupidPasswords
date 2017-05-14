import sys
import PIL
import PIL.Image
import PIL.ImageDraw
import PIL.ImageOps
import PIL.ImageFont

PIXEL_ON = 0
PIXEL_OFF = 255
filename = sys.argv[1]

def main():
    image = text_image(filename)
    image.show()
    image.save('image.png')


def text_image(text_path):

    grayscale = 'L'

    with open(text_path) as text_file:
        lines = tuple(l.rstrip() for l in text_file.readlines())

    large_font = 20
    font_path = 'cour.ttf'
    try:
        font = PIL.ImageFont.truetype(font_path, size=large_font)
    except IOError:
        font = PIL.ImageFont.load_default()
        print("couldn't use chosen font, using default.")

    pt2px = lambda pt: int(round(pt * 96.0 / 72 ))
    max_width_line = max(lines, key = lambda s: font.getsize(s)[0])
    max_height = pt2px(font.getsize(lines[0])[1])
    max_width = pt2px(font.getsize(max_width_line)[0])

    height = max_height * len(lines)
    width = int(round(max_width + 40))
    
    image = PIL.Image.new(grayscale, (width, height), color=PIXEL_OFF)
    draw = PIL.ImageDraw.Draw(image)

    horizontal_position = 5
    vertical_position = 5
    line_spacing = int(round(max_height * 0.8))
    for line in lines:
        draw.text((horizontal_position, vertical_position),
            line, fill=PIXEL_ON)
        vertical_position += line_spacing

    c_box = PIL.ImageOps.invert(image).getbbox()
    image = image.crop(c_box)
    return image

if __name__ == '__main__':
    main()