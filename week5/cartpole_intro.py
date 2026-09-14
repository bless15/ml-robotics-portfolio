import gymnasium as gym


# Run 10 random CartPole episodes
env = gym.make("CartPole-v1")

rewards = []

for episode in range(10):

    state, info = env.reset()

    terminated = False
    truncated = False
    total_reward = 0

    while not terminated and not truncated:

        action = env.action_space.sample()

        state, reward, terminated, truncated, info = env.step(action)

        total_reward += reward

    rewards.append(total_reward)

    print(f"Episode {episode + 1}: {total_reward}")


# Calculate average reward
average_reward = sum(rewards) / len(rewards)

print(f"Average Reward: {average_reward}")

env.close()