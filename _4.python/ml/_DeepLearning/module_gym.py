"""



"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from matplotlib.colors import ListedColormap

from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# OpenAI Gym

# RL 訓練都需要一個環境。OpenAI Gym 是一個開源的 RL 開發框架，提供數個知名專案的環境建設，包括我們今天要實作的 CartPole。其他還有 Atari、轉筆、賽車等等模擬環境，對想要上手 RL 的人是非常方便的框架。

# Gym 從環境庫中使用設定好的環境：

import gym

env = gym.make("CartPole-v0")

"""
環境包括以下 API：

    env.render()：將環境畫出來，方便從肉眼觀察訓練情況。不過會大幅降低訓練速度，如果想加速可以不用，或是 render 出來後把視窗點掉。
    env.observation_space：state 的設置，例如上下界等等。
    env.action_space：action 的設置，也提供 sample() method 可以隨機選擇 action。
    env.reset()：重置環境，一回合重新開始。
    env.step(action)：在環境中做出 action。會回傳 observation、rewards、done 回合結束與否、及 info 其他資訊。
    env.close()：完成訓練後把環境完整關閉。
"""

# CartPole 指的是讓小車上的柱子直立不倒的任務。

"""
Agent taking random actions.
Based on the example in OpenAI docs: https://gym.openai.com/docs/
"""
import gym
import matplotlib.pyplot as plt

# RL 訓練長度
N_EPISODES = 200
EPISODE_LENGTH = 200


def plot_rewards(rewards, n_episodes, algo):
    plt.plot(list(range(n_episodes)), rewards)
    plt.xlabel("episode")
    plt.ylabel("rewards")
    plt.ylim(0, EPISODE_LENGTH + 5)
    plt.title("Rewards over episodes ({})".format(algo))
    plt.savefig("{}.png".format("_".join(algo.split(" "))))


# 建立環境
env = gym.make("CartPole-v0")

# 開始訓練
all_rewards = []
for i_episode in range(N_EPISODES):
    observation = (
        env.reset()
    )  # reset environment to initial state for each episode # 把柱子擺好
    rewards = 0  # accumulate rewards for each episode
    for t in range(EPISODE_LENGTH):
        env.render()

        # 隨機挑選 action，這邊是向左或向右
        action = env.action_space.sample()  # choose a random action

        # 在環境中做出 action
        observation, reward, done, info, kk = env.step(
            action
        )  # do the action, get the reward

        # 累加 reward
        rewards += reward

        if done:  # 回合結束，可能柱子太傾斜或車子跑遠
            print(
                "Episode finished after {} timesteps, total rewards {}".format(
                    t + 1, rewards
                )
            )
            break
    all_rewards.append(rewards)

env.close()  # need to close, or errors will be reported
plot_rewards(all_rewards, N_EPISODES, "random action")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
