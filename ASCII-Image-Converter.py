# Time to code: 45 Minutes
from PIL import Image
import argparse

ASCII = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", ".", " "]

def resizeImg(img, scale):
    width, height = img.size
    #Shrink to account for strench
    return img.resize((int(width*scale), int(height*scale*0.5)), Image.Resampling.LANCZOS)

def greyscaleImg(img):
    return img.convert("L")


def pixelToChar(pixel, invert=False):
    # Convert the pixel value (0-255) into an ASCII index
    index = int(pixel * (len(ASCII) - 1) / 255)

    # Reverse the index if inversion is enabled
    if invert:
        index = len(ASCII) - 1 - index

    return ASCII[index]

def convertToASCII(img, invert = False):
    width, height = img.size 
    pixels = list(img.get_flattened_data())
    string = ""
    for i in range(len(pixels)):

        if i % width == 0:
            string += "\n"

        string += pixelToChar(pixels[i],invert)
    
    return string


#===========================ARGParse===========================
parser = argparse.ArgumentParser()

parser.add_argument("file", help="The image you want to convert")
parser.add_argument("scale", type=float, help="The scale of the ASCII image")
parser.add_argument("-i", "--invert", action="store_true", help="Invert the image color")

args = parser.parse_args()

img = Image.open(args.file)
smallImg = resizeImg(img, args.scale)

greyImg = greyscaleImg(smallImg)
text = convertToASCII(greyImg)
final = convertToASCII(greyImg, invert=args.invert)
#==============================================================

# #===========================Regular===========================
# file = "file location"
# scale = 0.5
# invert = False

# img = Image.open(file)
# smallImg = resizeImg(img, scale)

# greyImg = greyscaleImg(smallImg)
# text = convertToASCII(greyImg)
# final = convertToASCII(greyImg, invert=invert)
# #=============================================================

print(final)