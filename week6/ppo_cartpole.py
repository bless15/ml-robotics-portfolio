import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make("CartPole-v1")

model = PPO("MlpPolicy", env, verbose=1)

model.learn(total_timesteps=10_000)


#to measure its performance
obs, info = env.reset()

total_reward = 0
done = False

while not done:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)

    total_reward += reward
    done = terminated or truncated

print("Total reward:", total_reward)

env.close()

#save the trained model
model.save("week6/ppo_cartpole")