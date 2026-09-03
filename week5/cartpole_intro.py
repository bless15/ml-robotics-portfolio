"""import gymnasium as gym
env = gym.make("CartPole-v1")
print(env)"""


#reset() + step() example together
"""import gymnasium as gym
env = gym.make("CartPole-v1")

state, info = env.reset()

print("Initial state:", state)

action = env.action_space.sample()  # Sample a random action

new_state, reward, terminated, truncated, info = env.step(action)

print("New State:", new_state)
print("Reward:", reward)
print("Terminated:", terminated)
print("Truncated:", truncated)

env.close()"""


#repeating the RL loop
"""import gymnasium as gym

env = gym.make("CartPole-v1")

state, info = env.reset()

terminated = False
truncated = False

total_reward = 0

while not terminated and not truncated:

    action = env.action_space.sample()

    state, reward, terminated, truncated, info = env.step(action)

    total_reward += reward\

print("Total Reward:", total_reward)"""

"""print(env.action_space)

print(env.observation_space)"""

"""env.close() """
#the end of that code



#repeating the loop with multiple episodes - still random learning
"""import gymnasium as gym

env = gym.make("CartPole-v1")

state, info = env.reset()

terminated = False
truncated = False

for episode in range(5):
    state, info = env.reset()
    total_reward = 0

    terminated = False
    truncated = False

    while not terminated and not truncated:
        action = env.action_space.sample()
        state, reward, terminated, truncated, info = env.step(action)
        total_reward += reward

    print(f"Episode {episode + 1}: {total_reward}")\

print(env)"""




# repeating the loop with multiple episodes - simple policy
"""import gymnasium as gym

env = gym.make("CartPole-v1")

for episode in range(5):
    state, info = env.reset()
    total_reward = 0

    terminated = False
    truncated = False

    while not terminated and not truncated:

        if state[2] > 0:
            action = 1
        else:
            action = 0

        state, reward, terminated, truncated, info = env.step(action)

        total_reward += reward

    print(f"Episode {episode + 1}: {total_reward}")

env.close()"""


#to show the cartpole digitally
"""import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")

state, info = env.reset()

terminated = False
truncated = False

while not terminated and not truncated:
    action = env.action_space.sample()

    state, reward, terminated, truncated, info = env.step(action)

env.close()"""


#calculating average reward over multiple episodes
"""import gymnasium as gym

env = gym.make("CartPole-v1",)

rewards = []

for episode in range(5):
    state, info = env.reset()
    total_reward = 0

    terminated = False
    truncated = False

    while not terminated and not truncated:
        action = env.action_space.sample()

        state, reward, terminated, truncated, info = env.step(action)
        total_reward += reward

    rewards.append(total_reward)

    print(f"Episode {episode + 1}: {total_reward}")

average_reward = sum(rewards) / len(rewards)

print(f"Average Reward: {average_reward}")"""


#complete gymnasium pattern
"""import gymnasium as gym

env = gym.make("CartPole-v1")

for episode in range(5):

    state, info = env.reset()

    terminated = False
    truncated = False
    total_reward = 0

    while not terminated and not truncated:

        action = env.action_space.sample()

        state, reward, terminated, truncated, info = env.step(action)

        total_reward += reward

    print(f"Episode {episode + 1}: {total_reward}")

env.close()"""



#practical challenge
# Runs 10 random CartPole episodes and calculates the average reward.
import gymnasium as gym

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

average_reward = sum(rewards) / len(rewards)

print(f"Average Reward: {average_reward}")

env.close()