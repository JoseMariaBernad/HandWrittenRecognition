import cv2
#import numpy as np
#import matplotlib.pyplot as plt
from pathlib import Path

def invert(image_path):
    try:
        image_path_inverted = image_path.with_name('invert' + image_path.name)
        img = cv2.imread(str(image_path))
        img = cv2.bitwise_not(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #plt.imshow(img)
        cv2.imwrite(str(image_path_inverted), img)
    except:
        print("Error while augmenting " + str(image_path))
    
def augment(path, augmentation, is_recursive = True):
    for file in path.iterdir():
        if file.is_dir():
            if is_recursive:
                augment(file, augmentation)
        else:
            augmentation(file)