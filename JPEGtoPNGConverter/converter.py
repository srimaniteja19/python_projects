from PIL import Image
import os
import sys

img_folder = sys.argv[1]
output_folder = sys.argv[2]


if not (os.path.exists(output_folder)):
    os.makedirs(output_folder)

for filename in os.listdir(img_folder):
    img = Image.open(f"{img_folder}{filename}")
    # r = filename.find('.jpg')
    c_name = os.path.splitext(filename)[0]
    img.save(f"{output_folder}{c_name}.png", "png")
