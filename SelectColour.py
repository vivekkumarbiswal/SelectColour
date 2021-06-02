"""
This is a basic python program using 'Pillow' Library which can change color of any image
having multiple options of colors here...
"""

# Importing "Pillow Library" of Python.
from PIL import Image, ImageEnhance

# Provide source of the image which you want to edit.
img = Image.open("stop.png").convert("RGB")

# Defining a function for Gray Color.
def grayscale():											# Define a function and it's name.
    width,height = img.size									# Considering the size of the image in terms of height, width.
    pixels = img.load()										# Load the pixels of the image.
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            newr = (r+g+b)//3
            newg = (r+g+b)//3
            newb = (r+g+b)//3
            pixels[px,py] = (newr,newg,newb)
    img.show()

def contrast():
    img_con = ImageEnhance.Contrast(img)
    img_con.enhance(1.9).show("90% more contrast")

def red_channel():
    width,height = img.size
    pixels = img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            newr = r
            newg = 0
            newb = 0
            pixels[px,py] = (newr,newg,newb)
    img.show()
    
def green_channel():
    width,height = img.size
    pixels = img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            newr = 0
            newg = g
            newb = 0
            pixels[px,py] = (newr,newg,newb)
    img.show()

def blue_channel():
    width,height = img.size
    pixels = img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            newr = 0
            newg = 0
            newb = b
            pixels[px,py] = (newr,newg,newb)
    img.show()

def yellow_channel():
    width,height = img.size
    pixels = img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            newr = r
            newg = g
            newb = 0
            pixels[px,py] = (newr,newg,newb)
    img.show()

def skyblue_channel():
    width,height = img.size
    pixels = img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            newr = 0
            newg = g
            newb = b
            pixels[px,py] = (newr,newg,newb)
    img.show()

def pink_channel():
    width,height = img.size
    pixels = img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            newr = r
            newg = 0
            newb = b
            pixels[px,py] = (newr,newg,newb)
    img.show()

def cold_channel():
    width,height = img.size
    pixels = img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            newr = (g+b-r)
            newg = (b+r-g)
            newb = (r+g-b)
            pixels[px,py] = (newr,newg,newb)
    img.show()

def odd_channel():
    width,height = img.size
    pixels = img.load()
    for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))
            newr = (r+b-g)
            newg = (g+r-b)
            newb = (b+g-r)
            pixels[px,py] = (newr,newg,newb)
    img.show()

def choice():
    answer = str(input("Enter your choise from(grayscale,contrast,red,green,blue,yellow,skyblue,pink,cold,odd): "))
    if (answer == "grayscale"):
        grayscale()
    elif (answer == "contrast"):
        contrast()
    elif (answer == "red"):
        red_channel()
    elif (answer == "green"):
        green_channel()
    elif (answer == "blue"):
        blue_channel()
    elif (answer == "yellow"):
        yellow_channel()
    elif (answer == "skyblue"):
        skyblue_channel()
    elif (answer == "pink"):
        pink_channel()
    elif (answer == "cold"):
        cold_channel()
    elif (answer == "odd"):
        odd_channel()
    else:
        print("Invalid Syntax")
        print("Try Again")

def main():
    choice()

if __name__ == "__main__":
    main()