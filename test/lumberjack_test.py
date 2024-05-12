import sys
import time
sys.path.append("../")
from ma_gym.envs.lumberjacks.lumberjacks import Lumberjacks

env = Lumberjacks()

state = env.reset()
for _ in range(200):
    action = env.action_space.sample()
    # communication_list only returned for CatMouseMA
    agent_obs, rewards, terminated, info = env.step(action)
    state = env.get_global_obs()
    print(state)
    env.render()
    time.sleep(0.5)

env.close()