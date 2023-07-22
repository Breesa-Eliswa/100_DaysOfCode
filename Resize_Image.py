# A program to resize an image
from PIL import Image

def resize_image(size1, size2):
    image = Image.open('filename.jpg')  #Enter the filename of the image to be resized
    print(f"Current size: {image.size}")
    resized_image=image.resize((size1,size2))
    resized_image.save("TEDDY2.jpg")

size1 = int(input("Enter the width: "))
size2 = int(input("Enter the length: "))
resize_image(size1,size2)