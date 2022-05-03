import numpy as np
from gym import utils



class RobbiEnv(gym.Env):
    def __init__(self):
        
        
        self.action_space = gym.spaces.Discrete(6)
        
        
        #OBSERVATION: Ultrasonic sensors = U, LiDAR sensors= L
        # U,U,U,U,L,L
        self.observation_space = gym.spaces.Box(low=np.array([0,0,0,0,0,0]),
                                     high=np.array([1000,1000,1000,1000,1000,1000]),
                                     dtype=np.float64)
        
    def step(self, action):
    
    def _get_obs(self):
        
    def reset_model(self):
        
    def viewer_setup(self):
        
        
        
