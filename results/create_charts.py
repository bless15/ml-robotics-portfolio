import matplotlib.pyplot as plt

# MNIST model comparison
models = ["Logistic Regression", "Decision Tree", "PyTorch MLP"]
accuracy = [92.57, 87.54, 97.64]

plt.figure(figsize=(8, 5))
plt.bar(models, accuracy)
plt.ylabel("Accuracy (%)")
plt.title("MNIST Model Accuracy Comparison")
plt.ylim(0, 100)
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("results/mnist_model_comparison.png", dpi=150)
plt.close()

# CartPole performance comparison
agents = ["Random", "PPO"]
rewards = [25.0, 350.8]

plt.figure(figsize=(7, 5))
plt.bar(agents, rewards)
plt.ylabel("Average Reward")
plt.title("CartPole Performance: Random vs PPO")
plt.tight_layout()
plt.savefig("results/cartpole_performance.png", dpi=150)
plt.close()

print("Charts created successfully.")