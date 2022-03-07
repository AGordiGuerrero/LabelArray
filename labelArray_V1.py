#!/usr/bin/env python3

# Define an array of n x m images in a A4 paper
import argparse

from PIL import Image

text = 'This program performs an A4 size image with r by c copies of the input image.'

# Initiate the parser with a description
parser = argparse.ArgumentParser(description=text)

parser.add_argument("--rows", "-r", help="Number of rows")
parser.add_argument("--cols", "-c", help="Number of columns")
parser.add_argument("--file", "-f", help="Input image file name")

parser.parse_args()

# Read arguments from the command line
args = parser.parse_args()

if args.rows:
    print("Number of rows to do: %s" % args.rows)
if args.cols:
    print("Number of cols to do: %s" % args.cols)
if args.file:
    print("Input file name: %s" % args.file)
    
##################################
#define new image for A4 size
# resolution = 72 dpi
#imA4=Image.new('RGBA', (595, 842), 'white')
# resolution = 300 dpi
A4pixwidth=2480
A4pixlength=3508
imA4=Image.new('RGBA', (A4pixwidth, A4pixlength), 'white')

#loading image file
imOriginal = Image.open("logo-smart-open-lab-rectangular.png")
print(imOriginal.format, imOriginal.size, imOriginal.mode)

cols_int=int(args.cols)
rows_int=int(args.rows)


#defining new image size
imResized = imOriginal.resize((int(A4pixwidth / cols_int), int(A4pixlength / rows_int)))
#imResized = imOriginal.resize((200, 200))

#making array of images
for i in range (int(cols_int)):
  for j in range (int(rows_int)):
    imA4.paste(imResized, (int(A4pixwidth / cols_int *i), int(A4pixlength / rows_int * j)))

#imA4.paste(imResized, (0, 0))

imA4=imA4.convert('RGB')
# saving the label created label array 
imA4.save('labelarray_ouput.jpg')

print("Array done, showing result after file save. Exiting...")
#imOriginal.show()

imA4.show()

