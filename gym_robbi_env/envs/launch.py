import gym

from stable_baselines3 import DQN

env = gym.make("gym_robbi_env:robbiEnv-v0")

model = DQN("MlpPolicy", env, verbose=1, tensorboard_log="./dqn_robbi_tensorboard/")
model.learn(total_timesteps=10000, log_interval=4)
model.save("dqn_robbi")

del model # remove to demonstrate saving and loading

model = DQN.load("dqn_robbi")

obs = env.reset()
while True:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
      obs = env.reset()