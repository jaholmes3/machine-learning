from keras.layers import Conv2D
#Conv2D(filters, kernel_size, strides, padding, activation='relu', input_shape)
Conv2D(filters=16, kernel_size=2, strides=2, activation='relu', input_shape=(200, 200, 1))
