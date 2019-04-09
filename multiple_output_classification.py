# import the necessary packages
from keras.models import Model
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Dropout
from keras.layers.core import Lambda
from keras.layers.core import Dense
from keras.layers import Flatten
from keras.layers import Input
import tensorflow as tf


class FashionNet:
    @staticmethod
    def build_category_branch(inputs, numCategories,finalAct="softmax",chanDim=1):

        # Utlizie a lambda layer to convert the 3 input to a grayscale representation
        x = Lambda(lambda c:tf.image.rgb_to_grayscale(c))(inputs)

        pass
