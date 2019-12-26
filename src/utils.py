import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def load_data(data_file):
    """ loads fer2013.csv dataset
    # Arguments: data_file fer2013.csv
    """
    data = pd.read_csv(data_file)
    pixels = data['pixels'].tolist()
    width, height = 48,48
    faces = []
    for pixel_sequence in pixels:
        face = [int(pixel) for pixel in pixel_sequence.split(' ')]
        face = np.asarray(face).reshape(width,height)
        faces.append(face)
    faces = np.asarray(faces)
    #faces = preprocess_input(faces)
    faces = np.expand_dims(faces,-1)
    emotions = pd.get_dummies(data['emotion']).as_matrix()
    return faces, emotions

def display_image(image, one_hot_encoder=None, labels=None):
    
    image = np.squeeze(image)
    plt.imshow(image, cmap='gray')
    if one_hot_encoder != None:
        label_arg = np.argmax(one_hot_encoder)
        plt.title(labels[label_arg])
    plt.show()
    return None

def preprocess_input(images):
   
    images = images/255.0
    return images