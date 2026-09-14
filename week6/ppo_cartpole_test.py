import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make("CartPole-v1", render_mode="human")

model = PPO.load("week6/ppo_cartpole", env=env)

for episode in range(10):
    obs, info = env.reset()
    total_reward = 0
    done = False

    while not done:
        action, _states = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, info = env.step(action)

        total_reward += reward
        done = terminated or truncated

    print(f"Episode {episode + 1}: {total_reward}")

env.close()