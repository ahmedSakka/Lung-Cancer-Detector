from trnsorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np

# Preprocessing the CT scans in the dataset for prediction
def preprocess_image(filepath):
    # Loading the images and resizing them
    img = load_img(filepath, target_size = (224,224))

    # Converting the images to arrays
    img = img_to_array(img)

    # Normalizig the images
    img = np.expand_dims(img, axis = 0)
    img = img/255.0

    return img