from keras import backend as K
import numpy as np
import shutil, os
import numpy as np
import pandas as pd
from scipy import misc
import pickle
import matplotlib.pyplot as plt
from sklearn.externals import joblib

huber_loss_thresh = 1
action_list = np.array(
    [
        [0.0, 0.0, 0.0],  # 刹车
        [-0.6, 0.05, 0.0],  # 左急转
        [0.6, 0.05, 0.0],  # 右急转
        [0.0, 0.3, 0.0],
    ]
)  # 直行
rgb_mode = True
num_actions = action_list.shape[0]


def sel_action(action_index):
    return action_list[action_index]


def sel_action_index(action):
    for i in range(num_actions):
        if np.all(action == action_list[i]):
            return i
    raise ValueError("选择的动作不在列表中")


def huber_loss(y_true, y_pred):
    error = y_true - y_pred
    cond = K.abs(error) <= huber_loss_thresh
    if cond == True:
        loss = 0.5 * K.square(error)
    else:
        loss = 0.5 * huber_loss_thresh**2 + huber_loss_thresh * (
            K.abs(error) - huber_loss_thresh
        )
    return K.mean(loss)


def rgb2gray(rgb, norm=True):
    gray = np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
    if norm:
        # 归一化
        gray = gray.astype("float32") / 128 - 1
    return gray


def data_store(path, action, reward, state):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        shutil.rmtree(path)
        os.makedirs(path)
    df = pd.DataFrame(action, columns=["Steering", "Throttle", "Brake"])
    df["Reward"] = reward
    df.to_csv(path + "car_racing_actions_rewards.csv", index=False)
    for i in range(len(state)):
        if rgb_mode == False:
            image = rgb2gray(state[i])
        else:
            image = state[i]
    misc.imsave(path + "img" + str(i) + ".png", image)


def model_save(path, name, agent, R):
    """在数据路径中保存动作、奖励和状态(图像)"""
    if not os.path.exists(path):
        os.makedirs(path)
    agent.DQN.model.save(path + name)
    print(name, "saved")
    print("...")
    joblib.dump(agent.memory, path + name + "Memory")
    joblib.dump(
        [agent.epsilon, agent.steps, agent.DQN.opt.get_config()],
        path + name + "AgentParam",
    )
    joblib.dump(R, path + name + "Rewards")
    print("Memory pickle dumped")
