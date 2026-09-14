from tensorflow.keras.datasets import mnist
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
import joblib


# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Flatten each 28 × 28 image into 784 values
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

# Scale pixel values from 0–255 to 0–1
x_train = x_train / 255.0
x_test = x_test / 255.0


# Logistic Regression
model = LogisticRegression(max_iter=1000)

print("Training Logistic Regression...")
model.fit(x_train, y_train)
print("Training complete.")

joblib.dump(model, "week3/model.pkl")
print("Model saved successfully.")


# Decision Tree
tree_model = DecisionTreeClassifier(random_state=42)

print("Training Decision Tree...")
tree_model.fit(x_train, y_train)
print("Decision Tree training complete.")


# Evaluate Logistic Regression
prediction = model.predict(x_test[0].reshape(1, 784))

print("Predicted:", prediction[0])
print("Actual:", y_test[0])

accuracy = model.score(x_test, y_test)
print("Logistic Regression Accuracy:", accuracy)


# Evaluate Decision Tree
tree_accuracy = tree_model.score(x_test, y_test)
print("Decision Tree Accuracy:", tree_accuracy)


# Logistic Regression evaluation details
y_pred = model.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

report = classification_report(y_test, y_pred)
print("Classification Report:")
print(report)