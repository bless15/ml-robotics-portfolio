import torch
import torch.nn as nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

torch.manual_seed(42)

# Load training dataset
train_dataset = datasets.MNIST(
    root="data",
    train=True,
    download=True,
    transform=transforms.ToTensor()
)

train_loader = DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True
)


# Define the neural network
class MNISTModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer1 = nn.Linear(784, 128)
        self.layer2 = nn.Linear(128, 64)
        self.layer3 = nn.Linear(64, 10)

    def forward(self, x):
        x = self.layer1(x)
        x = torch.relu(x)

        x = self.layer2(x)
        x = torch.relu(x)

        x = self.layer3(x)

        return x


# Create the model
model = MNISTModel()


# Define loss function and optimizer
loss_function = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)


# Train the model
num_epochs = 5

for epoch in range(num_epochs):

    for images, labels in train_loader:

        # Flatten images
        images = images.view(images.shape[0], -1)

        # Forward pass
        outputs = model(images)

        # Calculate loss
        loss = loss_function(outputs, labels)

        # Backpropagation
        loss.backward()

        # Update parameters
        optimizer.step()

        # Clear gradients
        optimizer.zero_grad()

    print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item():.4f}")


# Load test dataset
test_dataset = datasets.MNIST(
    root="data",
    train=False,
    download=True,
    transform=transforms.ToTensor()
)

test_loader = DataLoader(
    test_dataset,
    batch_size=64,
    shuffle=False
)


# Evaluate the model
model.eval()

correct = 0
total = 0

with torch.no_grad():

    for images, labels in test_loader:

        # Flatten images
        images = images.view(images.shape[0], -1)

        # Make predictions
        outputs = model(images)
        predictions = outputs.argmax(dim=1)

        total += labels.size(0)
        correct += (predictions == labels).sum().item()


# Calculate accuracy
accuracy = correct / total * 100

print(f"Test Accuracy: {accuracy:.2f}%")


# Save the trained model
torch.save(model.state_dict(), "week4/mnist_model.pth")

print("Model saved successfully.")


# Load the saved model
loaded_model = MNISTModel()

loaded_model.load_state_dict(
    torch.load("week4/mnist_model.pth")
)

loaded_model.eval()

print("Saved model loaded successfully.")


# Make a prediction
image, label = test_dataset[0]

image = image.view(1, -1)

with torch.no_grad():
    output = loaded_model(image)
    prediction = output.argmax(dim=1).item()

print(f"Predicted: {prediction}")
print(f"Actual: {label}")