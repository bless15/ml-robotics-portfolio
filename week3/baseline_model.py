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
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import joblib


# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()


# Flatten each 28 × 28 image into 784 values
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)


# Scale pixel values from 0–255 to 0–1
x_train = x_train / 255.0
x_test = x_test / 255.0


# =========================
# Logistic Regression Model
# =========================

# Create the Logistic Regression model
model = LogisticRegression(max_iter=1000)

print("Model Created Successfully.")
print("Training started...")


# Train the model using the training data
model.fit(x_train, y_train)

print("Training complete.")


# Save the trained Logistic Regression model
joblib.dump(model, "week3/model.pkl")
print("Model saved successfully.")


# =========================
# Decision Tree Comparison
# =========================

# Create the Decision Tree model
tree_model = DecisionTreeClassifier()

print("Decision Tree training started...")


# Train the Decision Tree
tree_model.fit(x_train, y_train)

print("Decision Tree training complete.")


# =========================
# Test Logistic Regression
# =========================

# Make a prediction for the first test image
prediction = model.predict(x_test[0].reshape(1, 784))

print("Predicted:", prediction[0])
print("Actual:", y_test[0])


# Calculate Logistic Regression accuracy
accuracy = model.score(x_test, y_test)

print("Accuracy:", accuracy)


# =========================
# Compare Decision Tree
# =========================

# Calculate Decision Tree accuracy
tree_accuracy = tree_model.score(x_test, y_test)

print("Decision Tree Accuracy:", tree_accuracy)


# =========================
# Logistic Regression Results
# =========================

# Make predictions for all test images
y_pred = model.predict(x_test)


# Create the confusion matrix
cm = confusion_matrix(y_test, y_pred)

print(cm)


# Generate the classification report
report = classification_report(y_test, y_pred)

print(report)