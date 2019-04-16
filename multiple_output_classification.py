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
        x = Conv2D(64, (3,3), padding="same")(x)
        x = Activation("relu")(x)
        x = BatchNormalization(axis=chanDim)(x)
        x = Conv2D(64,(3,3),padding="same")(x)
        x = Activation("relu")(x)
        x = BatchNormalization(axis=chanDim)(x)
        x = MaxPooling2D(pool_size=(2,2))(x)
        x = Dropout(0.25)(x)

        # (CONV => RELU) * 2 => POOL
        x = Conv2D(128, (3, 3), padding="same")(x)
        x = Activation("relu")(x)
        x = BatchNormalization(axis=chanDim)(x)
        x = Conv2D(128, (3, 3), padding="same")(x)
        x = Activation("relu")(x)
        x = BatchNormalization(axis=chanDim)(x)
        x = MaxPooling2D(pool_size=(2, 2))(x)
        x = Dropout(0.25)(x)

        # Define a branch of output layers of the number of different
        # clothing categories (i.e shirts, jeans, dresses, etc)
        x = Flatten(x)
        x = Dense(256)(x)
        x = Activation("relu")(x)
        x = Dropout(0.5)(x)
        x = Dense(numCategories)(x)
        x = Activation(finalAct, name="category_output")(x)

        # return the category prediction
        return x

    @staticmethod
    def build_color_branch(inputs,numColors,finalAct="softmax",chanDim=1):
        # CONV => RELU => POOL
        x = Conv2D(16,(3,3),padding="same")(inputs)
        x = Activation("relu")(x)
        x = BatchNormalization(axis=chanDim)(x)
        x = MaxPooling2D(pool_size=(3,3))(x)
        x = Dropout(0.25)(x)

        # CONV => RELU => POOL
        x = Conv2D(32, (3,3), padding="same")(x)
        x = Activation("relu")(x)
        x = BatchNormalization(axis=chanDim)(x)
        x = MaxPooling2D(pool_size=(2,2))(x)
        x = Dropout(0.25)(x)

        # CONV => RELU => POOL
        x = Conv2D(32,(3,3),padding="same")(x)
        x = Activation("relu")(x)
        x = BatchNormalization(pool_size=(2,2))(x)
        x = BatchNormalization(axis=chanDim)(x)
        x = MaxPooling2D(pool_size=(2, 2))(x)
        x = Dropout(0.25)(x)

        # define a branch of output layers for the number of different
        # colors (i.e. red, black, blue, etc.)
        x = Flatten(x)
        x = Dense(128)(x)
        x = Activation("relu")(x)
        x = BatchNormalization()(x)
        x = Dropout(0.5)(x)
        x = Dense(numColors)(x)
        x = Activation(finalAct, name="color_output")(x)

        # return the color prediction sub-network
        return x

    @staticmethod
    def build_model(width, height, numCategories, numColors, finalAct="softmax"):

        # intializing the input shape and channel dimension (this code assume you are
        # using TensorFlow which utilizes channels las ordering)

        inputShape = (height,width,3)
        chanDims = -1

        input = Input(shape=inputShape)

        # construct both the "category" and "color" sub-networks
        categoryBranch = FashionNet.build_category_branch(input, numCategories,finalAct="softmax",chanDim=chanDims)
        colorBranch = FashionNet.build_color_branch(input, numColors,finalAct="softmax",chanDim=chanDims)

        # create model combining category and color branch
        model = Model(inputs= input, outputs=[categoryBranch,colorBranch], name="fashionnet")
        return model
