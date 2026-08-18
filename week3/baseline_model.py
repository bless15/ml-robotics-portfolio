"""from tensorflow.keras.datasets import mnist

#load the dataset, the MNIST dataset
(x_train, y_train), (x_test, y_test) =  mnist.load_data()

#Flatten each 28 × 28 image into 784 values
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

#chech the shape
print("x_train", x_train.shape)
print("y_train:", y_train.shape)
print("x_test", x_test.shape)
print("y_test:", y_test.shape)"""

from tensorflow.keras.datasets import mnist
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import joblib

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000,784)
x_test = x_test.reshape(10000, 784)

x_train = x_train / 255.0
x_test = x_test / 255.0

#create model
model = LogisticRegression(max_iter=1000)

print("Model Created Successfully.")

print("Training started...")

model.fit(x_train, y_train)

print("Training complete.")

joblib.dump(model, "week3/model.pkl")
print("Model saved successfully.")



prediction = model.predict(x_test[0].reshape(1, 784))

print("Predicted:", prediction[0])
print("Actual:", y_test[0])


accuracy = model.score(x_test, y_test)

print("Accuracy:", accuracy)


y_pred = model.predict(x_test)

cm = confusion_matrix(y_test, y_pred)

print(cm)


report = classification_report(y_test, y_pred)

print(report)