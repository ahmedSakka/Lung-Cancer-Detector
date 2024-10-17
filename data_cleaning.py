import os
from PIL import Image
import numpy as np


# Finding the duplicated images in the dataset and deleting them
def find_duplicates(directory):
    images_hash = {}
    duplicates = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('png', 'jpg', 'jpeg')):
                filepath = os.path.join(root, file)
                try:
                    image = Image.open(filepath)
                    image_array = np.array(image)

                    # Creating the hash for the image according to its pixels value
                    image_hash = hash(image_array.tostring())
                    # If the hash already exists that means the image already exists so delete it
                    if image_hash in images_hash:
                        os.remove(filepath)
                        duplicates += 1
                        print(f"Duplicate removed: {file}")
                    else:
                        images_hash[image_hash] = filepath
                except Exception as e:
                    # Removing the corrupt images
                    print(f"Corrupt image removed: {file}")
                    os.remove(filepath)
    print(f"Total duplicated images removed: {duplicates}")

if __name__ == "__main__":
    data_dir = "D:\The IQ-OTHNCCD lung cancer dataset"
    find_duplicates(data_dir)    