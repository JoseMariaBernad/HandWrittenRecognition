from fastai import *
from fastai.vision import *
import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_classes(file, path=Path('.')):
    path = path/'models'
    file = path/file
    filestr = str(file)
    with open(filestr + '.classes', 'r') as f:
        return json.loads(f.read())

path = Path('.')

model_name = 'stage-2-resnet34-224px-spanish-white'
classes = load_classes(model_name)
SIZE = 224
print(classes)

empty_data = ImageDataBunch.single_from_classes(path, classes, tfms=get_transforms())
learn = create_cnn(empty_data, models.resnet34)

#learn.path = Path('.')
learn.load(model_name)



def predict(image_path, invert = False):
    img = cv2.imread(image_path)
    if invert:
        img = cv2.bitwise_not(img)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #plt.imshow(img)
    #cv2.imwrite('invert.png',img)
    #img = open_image("invert.png")
    #img.show()
    #img = cv2.imread('invert.png')
    img = cv2.resize(img, (SIZE,SIZE))
    plt.imshow(img)
    cv2.imwrite('predict.png',img)
    img = open_image("predict.png")
    return learn.predict(img)