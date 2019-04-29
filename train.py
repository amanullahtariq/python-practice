# set the matplotlib backend so figures can be saved in the background
import matplotlib

matplotlib.use("Agg")

# import the necessary packages
from keras.optimizers import Adam
from keras.preprocessing.image import img_to_array
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from multiple_output_classification import FashionNet
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import pickle
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="path to input dataset (i.e., directory of images)")
ap.add_argument("-m", "--model", required=True,
                help="path to output model")
ap.add_argument("-l", "--categorybin", required=True,
                help="path to output category label binarizer")
ap.add_argument("-c", "--colorbin", required=True,
                help="path to output color label binarizer")
ap.add_argument("-p", "--plot", type=str, default="output",
                help="base filename for generated plots")
args = vars(ap.parse_args())

# Initialize the number of epochs to train for, initial learning rate,
# batch size and image dimensions

EPOCHS = 50
INIT_LR = 1e-3
BATCH_SIZE = 32
IMAGE_DIMS = (96, 96, 3)

# grab the images from the file path and randomly shuffle them
print("[INFO] loading images....")
imagePaths = sorted(list(paths.list_images(args["dataset"])))
random.seed(42)
random.shuffle(imagePaths)

# initializing the data, clothing category labels (i.e., shirts, jeans, dresses, etc.)
# along with the color labels (i.e. red, blue etc.)
data = []
categoryLabels = []
colorLabels = []

# Loop over the input images and populate the data categoryLabels and colorLabels Lists
for path in imagePaths:
    # load the image, pre-process it and store it in the data list
    image = cv2.imread(path)
    image = cv2.resize(image, (IMAGE_DIMS[1], IMAGE_DIMS[0]))
    image = img_to_array(image)
    data.append(image)

    # extract the clothing color and category from the path and
    # update the respective lists

    (color,cat) = path.split(os.path.sep)[-2].split("_")
    categoryLabels.append(cat)
    colorLabels.append(color)


# scale the raw pixel intensities to the range [0, 1] and convert to
# a NumPy array
data = np.array(data, dtype="float") / 255.0
print("[INFO] data matrix: {} images ({:.2f}MB)".format(len(imagePaths), data.nbytes / (1024 * 1000.0)))

# convert the label lists to NumPy arrays prior to binarization
categoryLabels = np.array(categoryLabels)
colorLabels = np.array(colorLabels)

# binarize both sets of labels
print("[INFO] binarizing labels...")
categoryLB = LabelBinarizer()
colorLB = LabelBinarizer()
categoryLabels = categoryLB.fit_transform(categoryLabels)
colorLabels = colorLB.fit_transform(colorLabels)

# Partitioning dataset into train and test split
split = train_test_split(data, categoryLabels, colorLabels, test_size=0.2, random_state=42)
(trainX, testX, trainCategoryY, testCategoryY,	trainColorY, testColorY) = split

