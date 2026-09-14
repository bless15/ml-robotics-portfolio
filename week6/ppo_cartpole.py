import gymnasium as gym
from stable_baselines3 import PPO


# Create CartPole environment
env = gym.make("CartPole-v1")


# Train PPO model
model = PPO("MlpPolicy", env, verbose=1)

model.learn(total_timesteps=10_000)


# Evaluate trained model
obs, info = env.reset()

total_reward = 0
terminated = False
truncated = False

while not terminated and not truncated:

    action, _states = model.predict(obs, deterministic=True)

    obs, reward, terminated, truncated, info = env.step(action)

    total_reward += reward


print("Total reward:", total_reward)


# Save trained model
model.save("week6/ppo_cartpole")

env.close()