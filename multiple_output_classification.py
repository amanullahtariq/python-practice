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
        """
        Model for classify clothing type

        :param inputs: The input volume to our category branch sub-network.
        :param numCategories: The number of categories such as 'dress', 'shoes', 'jeans', 'shirt' etc
        :param finalAct: The final activation layer type with default being a softmax classifier.
                For multi-ouput and multi-label use sigmoid activation function.
        :param chanDim: channel dimension
        :return:
        """

        # Utlizie a lambda layer to convert the 3 input to a grayscale representation
        x = Lambda(lambda c:tf.image.rgb_to_grayscale(c))(inputs)

        # CONV => RELU => POOL
        x = Conv2D(3, (32,32),padding="same")(x)
        x = Activation("relu")(x)
        x = BatchNormalization(axis=chanDim)(x)
        x = MaxPooling2D(pool_size=(3,3))(x)

        # For reducing the overfitting as no one single node in the layer will be responsible for prediction a
        # certain class, object, edge or corner
        x = Dropout(0.25)(x)

        # (CONV => RELU) * 2 => POOL


        pass
