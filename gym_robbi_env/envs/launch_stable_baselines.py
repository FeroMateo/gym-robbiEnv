import gym

env = gym.make("gym_robbi_env:robbiEnv-v0")

env.reset()

for x in range(10000):
    
    env.render()
    
    info = env.step(env.action_space.sample()) # take a random action
    
    print(info)
    
env.close()

