#set the matplotlib backend so figures can be saved in the background
import matplotlib
matplotlib.use("Agg")

# import the necessary packages
from keras.optimizers import Adam
from keras.preprocessing.image import img_to_array
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
# from pyimagesearch.fashionnet import FashionNet
# from imutils import paths
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