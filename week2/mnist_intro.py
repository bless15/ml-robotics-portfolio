"""from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)"""


#CODE TO GET MNIST FIRST IMAGE
'''import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

image = x_train[0]

print(image.shape)
print("Label:", y_train[0])

plt.imshow(x_train[0], cmap="gray")
plt.show()'''


"""from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

image = x_train[0]
print(image)
print(image.dtype)
print(image.ndim)
print(image.size)
print(image.min())
print(image.max())"""


"""from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

image = x_train[0]
print(image[0, 0])
print(image[14, 14])"""


"""import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

images = x_train[:5]

for i in range(5):
    plt.imshow(images[i], cmap="gray")
    plt.title(f"Label: {y_train[i]}")
    plt.show()"""



#CODE TO DISPLAY FIRST 5 MNIST IMAGES IN DIFFERENT FIGURES
"""import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

images = x_train[:5]

print(images.shape)"""


#CODE TO DISPLAY FIRST 5 MNIST IMAGES IN SAME FIGURE
"""import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist 
(x_train, y_train), (x_test, y_test) = mnist.load_data()

images = x_train[:5]

for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(f"Label: {y_train[i]}")
    plt.axis('off')

plt.show()"""



"""import numpy as np
from tensorflow.keras.datasets import mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()

print(y_train[:10])
print(np.unique(y_train))
print(np.bincount(y_train))

print(x_test.shape)
print(y_test.shape)
print(np.bincount(y_test))"""



#FINAL REHERSALS TO CHECK WHAT WE HAVE DONE SO FAR.

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

image = x_train[10]
'''print(image.shape)
print(image.ndim)
print(image.size)
print(image.min())
print(image.max())'''


'''print("Label: ", y_train[10])
plt.imshow(image, cmap='gray')
plt.title(f"Label: {y_train[10]}")
plt.axis('off')
plt.show()'''


images = x_train[:10]

for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(f"Label: {y_train[i]}")
    plt.axis('off')

plt.show()