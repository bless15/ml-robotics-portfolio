import gymnasium as gym
from stable_baselines3 import PPO


# Create CartPole environment with visual rendering
env = gym.make("CartPole-v1", render_mode="human")


# Load trained PPO model
model = PPO.load("week6/ppo_cartpole", env=env)


# Evaluate the model for 10 episodes
for episode in range(10):

    obs, info = env.reset()

    terminated = False
    truncated = False
    total_reward = 0

    while not terminated and not truncated:

        action, _states = model.predict(obs, deterministic=True)

        obs, reward, terminated, truncated, info = env.step(action)

        total_reward += reward

    print(f"Episode {episode + 1}: {total_reward}")


env.close()