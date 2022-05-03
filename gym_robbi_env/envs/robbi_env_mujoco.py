import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env


class RobbiEnv(gym.Env):
    def __init__(self):
        
        #no se que es 5
        mujoco_env.MujocoEnv.__init__(self,"/Users/mateoruiz/Model_Robot/robbi_model.xml",5)
        
        utils.EzPickle.__init__(self)
        
    def _get_obs(self):
        
        
        """
        En teoria recibo los valores input de los sensores y los redondeo a un numero redondo
        """
        data = self.sim.data.sensordata
        
        return list(map(round,data))
        
        
        
    def step(self, action):
        
        posbefore = self.sim.data.qpos[0]
        self.do_simulation(a, self.frame_skip)
        posafter, height, ang = self.sim.data.qpos[0:3]
        alive_bonus = 1.0
        reward = (posafter - posbefore) / self.dt
        reward += alive_bonus
        reward -= 1e-3 * np.square(a).sum()
        s = self.state_vector()
        done = False
        ob = self._get_obs()
        return ob, reward, done, {}
    
        
    def reset_model(self):
        
    def viewer_setup(self):
        
        
        
