from PIL import Image
from pillow_heif import register_heif_opener
import os
import logging

# Set logger level
logging.basicConfig(level="DEBUG")

# 
register_heif_opener()

# Get list of HEIF and HEIC files in directory
directory = input("Enter the path to the directory: ") #add a final \ if the path is absolute
files = [f for f in os.listdir(directory) if f.endswith('.heic') or f.endswith('.heif') or f.endswith('.HEIC')]

logging.debug(directory)
logging.debug(files)

# Create output directory if it does not exist
if not os.path.exists(os.path.join(directory, 'output')):
    os.makedirs(os.path.join(directory, 'output'))

# Convert each file to JPEG
for filename in files:
    image = Image.open(os.path.join(directory, filename))
    image.convert('RGB').save(os.path.join(directory, 'output', os.path.splitext(filename)[0] + '.jpg'))