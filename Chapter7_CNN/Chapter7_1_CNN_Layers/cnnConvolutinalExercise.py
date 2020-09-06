import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.datasets import mnist


# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

image = x_train[0]
image = image.reshape((28, 28))

kernel = np.random.uniform(low=0.0, high=1.0, size=(2, 2))


# Stride (1,1)
# Conv Funktion definieren und anschließend plotten
def conv2D(image, kernel):
    return image


conv_image = conv2D(image, kernel)

# Input und Outputbild des Pooling Layers mit imshow() ausgeben
plt.imshow(image, cmap="gray")
plt.show()

plt.imshow(conv_image, cmap="gray")
plt.show()
