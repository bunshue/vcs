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
from sklearn import tree
from sklearn import metrics
from matplotlib.colors import ListedColormap


def show():
    plt.show()
    pass


def get_dataset(N=20, sigma=0.1):
    """Generate N training samples"""
    # X is a set of random points from [-1, 1]
    X = 2 * np.random.sample(N) - 1
    # Y are corresponding target values (with noise included)
    Y = np.array([math.sin(math.pi * x) + np.random.normal(0, sigma) for x in X])
    return X, Y


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# import tensorflow as tf
import tensorflow.compat.v1 as tf  # 強制使用tensorflow 1.0

tf.disable_v2_behavior()

hello = tf.constant("Hello, TensorFlow!")
sess = tf.Session()  # tensorflow 1.0才有的指令
print(sess.run(hello))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
language model
"""

# data_processing

import re
import codecs

filepath = "data/war_and_peace.txt"  # in
out_file = "tmp_war_and_peace.txt"  # out

# Regexes used to clean up the text
NEW_LINE_IN_PARAGRAPH_REGEX = re.compile(r"(\S)\n(\S)")
MULTIPLE_NEWLINES_REGEX = re.compile(r"(\n)(\n)+")

# Read text as string
with codecs.open(filepath, encoding="utf-8", mode="r") as f_input:
    book_str = f_input.read()

# Cleanup
book_str = NEW_LINE_IN_PARAGRAPH_REGEX.sub("\g<1> \g<2>", book_str)
book_str = MULTIPLE_NEWLINES_REGEX.sub("\n\n", book_str)

# Write proccessed text to file
with codecs.open(out_file, encoding="utf-8", mode="w") as f_output:
    f_output.write(book_str)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from six.moves import range
import codecs


class DataReader(object):
    # Data reader used for training language model.

    def __init__(self, filepath, batch_length, batch_size):
        self.batch_length = batch_length
        self.batch_size = batch_size
        # Read data into string
        with codecs.open(filepath, encoding="utf-8", mode="r") as f:
            self.data_str = f.read()
        self.data_length = len(self.data_str)
        print("data_length: ", self.data_length)
        # Create a list of characters, indices are class indices for softmax
        char_set = set()
        for ch in self.data_str:
            char_set.add(ch)
        self.char_list = sorted(list(char_set))
        print("char_list: ", len(self.char_list), self.char_list)
        # Create reverse mapping to look up the index based on the character
        self.char_dict = {val: idx for idx, val in enumerate(self.char_list)}
        print("char_dict: ", self.char_dict)
        # Initalise random start indices
        self.reset_indices()

    def reset_indices(self):
        self.start_idxs = np.random.random_integers(
            0, self.data_length, self.batch_size
        )

    def get_sample(self, start_idx, length):
        # Get a sample and wrap around the data string
        return [
            self.char_dict[self.data_str[i % self.data_length]]
            for i in range(start_idx, start_idx + length)
        ]

    def get_input_target_sample(self, start_idx):
        sample = self.get_sample(start_idx, self.batch_length + 1)
        inpt = sample[0 : self.batch_length]
        trgt = sample[1 : self.batch_length + 1]
        return inpt, trgt

    def get_batch(self, start_idxs):
        input_batch = np.zeros((self.batch_size, self.batch_length), dtype=np.int32)
        target_batch = np.zeros((self.batch_size, self.batch_length), dtype=np.int32)
        for i, start_idx in enumerate(start_idxs):
            inpt, trgt = self.get_input_target_sample(start_idx)
            input_batch[i, :] = inpt
            target_batch[i, :] = trgt
        return input_batch, target_batch

    def __iter__(self):
        while True:
            input_batch, target_batch = self.get_batch(self.start_idxs)
            self.start_idxs = (self.start_idxs + self.batch_length) % self.data_length
            yield input_batch, target_batch


filepath = "tmp_war_and_peace.txt"
batch_length = 10
batch_size = 2
reader = DataReader(filepath, batch_length, batch_size)
s = "As in the question of astronomy then, so in the question of history now,"
print([reader.char_dict[c] for c in s])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# connect_4.py

"""
Full code for running a game of connect 4 on a board_width, board_height and winning length can be specified in relevant
methods. Allowing you to play connect 5, 6, 7, etc. Defaults are board_width = 7, board_height = 6, winning_length = 4

The main method to use here is play_game which simulates a game to the end using the function args it takes to determine
where each player plays.
The board is represented by a board_width x board_height tuple of ints. A 0 means no player has played in a space, 1
means player one has played there, -1 means the seconds player has played there. The apply_move method can be used to
return a copy of a given state with a given move applied. This can be useful for doing min-max or monte carlo sampling.
"""


def _new_board(board_width, board_height):
    """Return a emprty tic-tac-toe board we can use for simulating a game.

    Args:
        board_width (int): The width of the board, a board_width * board_height board is created
        board_height (int): The height of the board, a board_width * board_height board is created

    Returns:
        board_width x board_height tuple of ints
    """
    return tuple(tuple(0 for _ in range(board_height)) for _ in range(board_width))


def apply_move(board_state, move_x, side):
    """Returns a copy of the given board_state with the desired move applied.

    Args:
        board_state (2d tuple of int): The given board_state we want to apply the move to.
        move_x (int): Which column we are going to "drop" our piece in
        side (int): The side we are making this move for, 1 for the first player, -1 for the second player.

    Returns:
        (2d tuple of int): A copy of the board_state with the given move applied for the given side.
    """
    # find position in which move will settle
    move_y = 0
    for x in board_state[move_x]:
        if x == 0:
            break
        else:
            move_y += 1

    def get_tuples():
        for i in range(len(board_state)):
            if move_x == i:
                temp = list(board_state[i])
                temp[move_y] = side
                yield tuple(temp)
            else:
                yield board_state[i]

    return tuple(get_tuples())


def available_moves(board_state):
    """Get all legal moves for the current board_state. For Tic-tac-toe that is all positions that do not currently have
    pieces played.

    Args:
        board_state: The board_state we want to check for valid moves.

    Returns:
        Generator of int: All the valid moves that can be played in this position.
    """
    for x in range(len(board_state)):
        if any(y == 0 for y in board_state[x]):
            yield x


def _has_winning_line(line, winning_length):
    count = 0
    last_side = 0
    for x in line:
        if x == last_side:
            count += 1
            if count == winning_length:
                return last_side
        else:
            count = 1
            last_side = x
    return 0


def has_winner(board_state, winning_length=4):
    """Determine if a player has won on the given board_state.

    Args:
        board_state (2d tuple of int): The current board_state we want to evaluate.
        winning_length (int): The number of moves in a row needed for a win.

    Returns:
        int: 1 if player one has won, -1 if player 2 has won, otherwise 0.
    """
    board_width = len(board_state)
    board_height = len(board_state[0])

    # check rows
    for x in range(board_width):
        winner = _has_winning_line(board_state[x], winning_length)
        if winner != 0:
            return winner
    # check columns
    for y in range(board_height):
        winner = _has_winning_line((i[y] for i in board_state), winning_length)
        if winner != 0:
            return winner

    # check diagonals
    diagonals_start = -(board_width - winning_length)
    diagonals_end = board_width - winning_length
    for d in range(diagonals_start, diagonals_end):
        winner = _has_winning_line(
            (
                board_state[i][i + d]
                for i in range(max(-d, 0), min(board_width, board_height - d))
            ),
            winning_length,
        )
        if winner != 0:
            return winner
    for d in range(diagonals_start, diagonals_end):
        winner = _has_winning_line(
            (
                board_state[i][board_height - i - d - 1]
                for i in range(max(-d, 0), min(board_width, board_height - d))
            ),
            winning_length,
        )
        if winner != 0:
            return winner

    return 0  # no one has won, return 0 for a draw


def play_game(
    plus_player_func,
    minus_player_func,
    board_width=7,
    board_height=6,
    winning_length=4,
    log=False,
):
    """Run a single game of tic-tac-toe until the end, using the provided function args to determine the moves for each
    player.

    Args:
        plus_player_func ((board_state(board_size by board_size tuple of int), side(int)) -> move((int, int))):
            Function that takes the current board_state and side this player is playing, and returns the move the player
            wants to play.
        minus_player_func ((board_state(board_size by board_size tuple of int), side(int)) -> move((int, int))):
            Function that takes the current board_state and side this player is playing, and returns the move the player
            wants to play.
        board_width (int): The width of the board, a board_width * board_height board is created
        board_height (int): The height of the board, a board_width * board_height board is created
        winning_length (int): The number of pieces in a row needed to win a game.
        log (bool): If True progress is logged to console, defaults to False

    Returns:
        int: 1 if the plus_player_func won, -1 if the minus_player_func won and 0 for a draw
    """
    board_state = _new_board(board_width, board_height)
    player_turn = 1

    while True:
        _avialable_moves = list(available_moves(board_state))
        if len(_avialable_moves) == 0:
            # draw
            if log:
                print("no moves left, game ended a draw")
            return 0.0
        if player_turn > 0:
            move = plus_player_func(board_state, 1)
        else:
            move = minus_player_func(board_state, -1)

        if move not in _avialable_moves:
            # if a player makes an invalid move the other player wins
            if log:
                print("illegal move ", move)
            return -player_turn

        board_state = apply_move(board_state, move, player_turn)
        if log:
            print(board_state)

        winner = has_winner(board_state, winning_length)
        if winner != 0:
            if log:
                print("we have a winner, side: %s" % player_turn)
            return winner
        player_turn = -player_turn


def random_player(board_state, _):
    """A player func that can be used in the play_game method. Given a board state it chooses a move randomly from the
    valid moves in the current state.

    Args:
        board_state (2d tuple of int): The current state of the board
        _: the side this player is playing, not used in this function because we are simply choosing the moves randomly

    Returns:
        (int, int): the move we want to play on the current board
    """
    moves = list(available_moves(board_state))
    return random.choice(moves)


if __name__ == "__main__":
    # example of playing a game
    play_game(
        random_player,
        random_player,
        log=True,
        board_width=7,
        board_height=6,
        winning_length=4,
    )

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# actor_critic_advantage_cart_pole.py

# note must import tensorflow before gym
from collections import deque
import pickle

# import tensorflow as tf
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()  # tensorflow2下使用tensorflow1的方法

import gym

env = gym.make("CartPole-v0")

ACTIONS_COUNT = 2
FUTURE_REWARD_DISCOUNT = 0.9
LEARN_RATE_ACTOR = 0.01
LEARN_RATE_CRITIC = 0.01
STORE_SCORES_LEN = 5
GAMES_PER_TRAINING = 3
INPUT_NODES = env.observation_space.shape[0]

ACTOR_HIDDEN = 20
CRITIC_HIDDEN = 20

session = tf.Session()

actor_feed_forward_weights_1 = tf.Variable(
    tf.truncated_normal([INPUT_NODES, ACTOR_HIDDEN], stddev=0.01)
)
actor_feed_forward_bias_1 = tf.Variable(tf.constant(0.0, shape=[ACTOR_HIDDEN]))

actor_feed_forward_weights_2 = tf.Variable(
    tf.truncated_normal([ACTOR_HIDDEN, ACTIONS_COUNT], stddev=0.01)
)
actor_feed_forward_bias_2 = tf.Variable(tf.constant(0.1, shape=[ACTIONS_COUNT]))

actor_input_placeholder = tf.placeholder("float", [None, INPUT_NODES])
actor_hidden_layer = tf.nn.tanh(
    tf.matmul(actor_input_placeholder, actor_feed_forward_weights_1)
    + actor_feed_forward_bias_1
)
actor_output_layer = tf.nn.softmax(
    tf.matmul(actor_hidden_layer, actor_feed_forward_weights_2)
    + actor_feed_forward_bias_2
)

actor_action_placeholder = tf.placeholder("float", [None, ACTIONS_COUNT])
actor_advantage_placeholder = tf.placeholder("float", [None, 1])

policy_gradient = tf.reduce_mean(
    actor_advantage_placeholder * actor_action_placeholder * tf.log(actor_output_layer)
)
actor_train_operation = tf.train.AdamOptimizer(LEARN_RATE_ACTOR).minimize(
    -policy_gradient
)

critic_feed_forward_weights_1 = tf.Variable(
    tf.truncated_normal([INPUT_NODES, CRITIC_HIDDEN], stddev=0.01)
)
critic_feed_forward_bias_1 = tf.Variable(tf.constant(0.0, shape=[CRITIC_HIDDEN]))

critic_feed_forward_weights_2 = tf.Variable(
    tf.truncated_normal([CRITIC_HIDDEN, 1], stddev=0.01)
)
critic_feed_forward_bias_2 = tf.Variable(tf.constant(0.0, shape=[1]))

critic_input_placeholder = tf.placeholder("float", [None, INPUT_NODES])
critic_hidden_layer = tf.nn.tanh(
    tf.matmul(critic_input_placeholder, critic_feed_forward_weights_1)
    + critic_feed_forward_bias_1
)
critic_output_layer = (
    tf.matmul(critic_hidden_layer, critic_feed_forward_weights_2)
    + critic_feed_forward_bias_2
)

critic_target_placeholder = tf.placeholder("float", [None, 1])

critic_cost = tf.reduce_mean(tf.square(critic_target_placeholder - critic_output_layer))
critic_train_operation = tf.train.AdamOptimizer(LEARN_RATE_CRITIC).minimize(critic_cost)

critic_baseline = critic_target_placeholder - critic_output_layer

scores = deque(maxlen=STORE_SCORES_LEN)

# set the first action to do nothing
last_action = np.zeros(ACTIONS_COUNT)
last_action[1] = 1

time = 0

session.run(tf.initialize_all_variables())


def choose_next_action(state):
    probability_of_actions = session.run(
        actor_output_layer, feed_dict={actor_input_placeholder: [state]}
    )[0]
    try:
        move = np.random.multinomial(1, probability_of_actions)
    except ValueError:
        # sometimes because of rounding errors we end up with probability_of_actions summing to greater than 1.
        # so need to reduce slightly to be a valid value
        move = np.random.multinomial(
            1, probability_of_actions / (sum(probability_of_actions) + 1e-6)
        )
    return move


def train(states, actions_taken, advantages):
    # learn that these actions in these states lead to this reward
    session.run(
        actor_train_operation,
        feed_dict={
            actor_input_placeholder: states,
            actor_action_placeholder: actions_taken,
            actor_advantage_placeholder: advantages,
        },
    )


last_state = env.reset()
total_reward = 0
current_game_observations = []
current_game_rewards = []
current_game_actions = []

episode_observation = []
episode_rewards = []
episode_actions = []
games = 0
plot_x = []
plot_y = []

critic_costs = deque(maxlen=10)


""" NG
while True:
    env.render()
    last_action = choose_next_action(last_state)
    current_state, reward, terminal, info = env.step(np.argmax(last_action))
    total_reward += reward

    if terminal:
        reward = -0.10
    else:
        reward = 0.1

    current_game_observations.append(last_state)
    current_game_rewards.append(reward)
    current_game_actions.append(last_action)

    if terminal:
        games += 1
        scores.append(total_reward)

        if games % STORE_SCORES_LEN == 0:
            plot_x.append(games)
            plot_y.append(np.mean(scores))

        # get temporal difference values for critic
        cumulative_reward = 0
        for i in reversed(range(len(current_game_observations))):
            cumulative_reward = (
                current_game_rewards[i] + FUTURE_REWARD_DISCOUNT * cumulative_reward
            )
            current_game_rewards[i] = [cumulative_reward]

        values_t = session.run(
            critic_output_layer, {critic_input_placeholder: current_game_observations}
        )
        advantages = []

        for i in range(len(current_game_observations) - 1):
            advantages.append(
                [
                    current_game_rewards[i][0]
                    + FUTURE_REWARD_DISCOUNT * values_t[i + 1][0]
                    - values_t[i][0]
                ]
            )

        advantages.append([current_game_rewards[-1][0] - values_t[-1][0]])

        _, cost = session.run(
            [critic_train_operation, critic_cost],
            {
                critic_input_placeholder: current_game_observations,
                critic_target_placeholder: current_game_rewards,
            },
        )

        critic_costs.append(cost)

        print(
            "Game: %s reward %s average scores %s critic cost %s"
            % (games, total_reward, np.mean(scores), np.mean(critic_costs))
        )

        episode_observation.extend(current_game_observations)
        episode_actions.extend(current_game_actions)
        episode_rewards.extend(advantages)

        total_reward = 0
        current_game_observations = []
        current_game_rewards = []
        current_game_actions = []

        if games % GAMES_PER_TRAINING == 0:
            episode_rewards = np.array(episode_rewards)
            normalized_rewards = episode_rewards - np.mean(episode_rewards)
            normalized_rewards /= np.std(normalized_rewards)

            train(episode_observation, episode_actions, normalized_rewards)

            episode_observation = []
            episode_actions = []
            episode_rewards = []

    time += 1

    # update the old values
    if terminal:
        last_state = env.reset()
    else:
        last_state = current_state
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# actor_critic_baseline_cart_pole.py

# note must import tensorflow before gym
from collections import deque
import pickle

# import tensorflow as tf
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()  # tensorflow2下使用tensorflow1的方法

import gym

env = gym.make("CartPole-v0")

ACTIONS_COUNT = 2
FUTURE_REWARD_DISCOUNT = 0.9
LEARN_RATE_ACTOR = 0.01
LEARN_RATE_CRITIC = 0.01
STORE_SCORES_LEN = 5
GAMES_PER_TRAINING = 3
INPUT_NODES = env.observation_space.shape[0]

ACTOR_HIDDEN = 20

session = tf.Session()

actor_feed_forward_weights_1 = tf.Variable(
    tf.truncated_normal([INPUT_NODES, ACTOR_HIDDEN], stddev=0.01)
)
actor_feed_forward_bias_1 = tf.Variable(tf.constant(0.0, shape=[ACTOR_HIDDEN]))

actor_feed_forward_weights_2 = tf.Variable(
    tf.truncated_normal([ACTOR_HIDDEN, ACTIONS_COUNT], stddev=0.01)
)
actor_feed_forward_bias_2 = tf.Variable(tf.constant(0.1, shape=[ACTIONS_COUNT]))

actor_input_placeholder = tf.placeholder("float", [None, INPUT_NODES])
actor_hidden_layer = tf.nn.tanh(
    tf.matmul(actor_input_placeholder, actor_feed_forward_weights_1)
    + actor_feed_forward_bias_1
)
actor_output_layer = tf.nn.softmax(
    tf.matmul(actor_hidden_layer, actor_feed_forward_weights_2)
    + actor_feed_forward_bias_2
)

actor_action_placeholder = tf.placeholder("float", [None, ACTIONS_COUNT])
actor_advantage_placeholder = tf.placeholder("float", [None, 1])

policy_gradient = tf.reduce_mean(
    actor_advantage_placeholder * actor_action_placeholder * tf.log(actor_output_layer)
)
actor_train_operation = tf.train.AdamOptimizer(LEARN_RATE_ACTOR).minimize(
    -policy_gradient
)

CRITIC_HIDDEN = 20

critic_feed_forward_weights_1 = tf.Variable(
    tf.truncated_normal([INPUT_NODES, CRITIC_HIDDEN], stddev=0.01)
)
critic_feed_forward_bias_1 = tf.Variable(tf.constant(0.0, shape=[CRITIC_HIDDEN]))

critic_feed_forward_weights_2 = tf.Variable(
    tf.truncated_normal([CRITIC_HIDDEN, 1], stddev=0.01)
)
critic_feed_forward_bias_2 = tf.Variable(tf.constant(0.0, shape=[1]))

critic_input_placeholder = tf.placeholder("float", [None, INPUT_NODES])
critic_hidden_layer = tf.nn.tanh(
    tf.matmul(critic_input_placeholder, critic_feed_forward_weights_1)
    + critic_feed_forward_bias_1
)
critic_output_layer = (
    tf.matmul(critic_hidden_layer, critic_feed_forward_weights_2)
    + critic_feed_forward_bias_2
)

critic_target_placeholder = tf.placeholder("float", [None, 1])

critic_cost = tf.reduce_mean(tf.square(critic_target_placeholder - critic_output_layer))
critic_train_operation = tf.train.AdamOptimizer(LEARN_RATE_CRITIC).minimize(critic_cost)

critic_advantages = critic_target_placeholder - critic_output_layer

scores = deque(maxlen=STORE_SCORES_LEN)

# set the first action to do nothing
last_action = np.zeros(ACTIONS_COUNT)
last_action[1] = 1

time = 0

session.run(tf.initialize_all_variables())


def choose_next_action(state):
    probability_of_actions = session.run(
        actor_output_layer, feed_dict={actor_input_placeholder: [state]}
    )[0]
    try:
        move = np.random.multinomial(1, probability_of_actions)
    except ValueError:
        # sometimes because of rounding errors we end up with probability_of_actions summing to greater than 1.
        # so need to reduce slightly to be a valid value
        move = np.random.multinomial(
            1, probability_of_actions / (sum(probability_of_actions) + 1e-6)
        )
    return move


def train(states, actions_taken, advantages):
    # learn that these actions in these states lead to this reward
    session.run(
        actor_train_operation,
        feed_dict={
            actor_input_placeholder: states,
            actor_action_placeholder: actions_taken,
            actor_advantage_placeholder: advantages,
        },
    )


last_state = env.reset()
total_reward = 0
current_game_observations = []
current_game_rewards = []
current_game_actions = []

episode_observation = []
episode_rewards = []
episode_actions = []
games = 0

critic_costs = deque(maxlen=100)

""" NG
while True:
    env.render()
    last_action = choose_next_action(last_state)
    current_state, reward, terminal, info = env.step(np.argmax(last_action))
    total_reward += reward

    if terminal:
        reward = -0.10

    current_game_observations.append(last_state)
    current_game_rewards.append(reward)
    current_game_actions.append(last_action)

    if terminal:
        games += 1
        scores.append(total_reward)

        # get temporal difference values for critic
        cumulative_reward = 0
        for i in reversed(range(len(current_game_observations))):
            cumulative_reward = (
                current_game_rewards[i] + FUTURE_REWARD_DISCOUNT * cumulative_reward
            )
            current_game_rewards[i] = [cumulative_reward]

        _, cost, advantages = session.run(
            [critic_train_operation, critic_cost, critic_advantages],
            {
                critic_input_placeholder: current_game_observations,
                critic_target_placeholder: current_game_rewards,
            },
        )

        critic_costs.append(cost)

        print(
            "Game: %s reward %s average scores %s critic cost %s"
            % (games, total_reward, np.mean(scores), np.mean(critic_costs))
        )

        episode_observation.extend(current_game_observations)
        episode_actions.extend(current_game_actions)
        episode_rewards.extend(advantages)

        total_reward = 0
        current_game_observations = []
        current_game_rewards = []
        current_game_actions = []

        if games % GAMES_PER_TRAINING == 0:
            train(episode_observation, episode_actions, episode_rewards)

            episode_observation = []
            episode_actions = []
            episode_rewards = []

    time += 1

    # update the old values
    if terminal:
        last_state = env.reset()
    else:
        last_state = current_state
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# deep_q_breakout.py

# note must import tensorflow before gym
from collections import deque
import pickle

# import tensorflow as tf
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()  # tensorflow2下使用tensorflow1的方法

import gym
import zlib

resume = True
CHECKPOINT_PATH = "deep_q_breakout_path"
ACTIONS_COUNT = 3
SCREEN_WIDTH, SCREEN_HEIGHT = (72, 84)
FUTURE_REWARD_DISCOUNT = 0.99
OBSERVATION_STEPS = 100000.0  # time steps to observe before training
EXPLORE_STEPS = 2000000.0  # frames over which to anneal epsilon
INITIAL_RANDOM_ACTION_PROB = 1.0  # starting chance of an action being random
FINAL_RANDOM_ACTION_PROB = 0.05  # final chance of an action being random
MEMORY_SIZE = 800000  # number of observations to remember
MINI_BATCH_SIZE = 128  # size of mini batches
STATE_FRAMES = 2  # number of frames to store in the state
(
    OBS_LAST_STATE_INDEX,
    OBS_ACTION_INDEX,
    OBS_REWARD_INDEX,
    OBS_CURRENT_STATE_INDEX,
    OBS_TERMINAL_INDEX,
) = range(5)
SAVE_EVERY_X_STEPS = 20000
LEARN_RATE = 1e-4
STORE_SCORES_LEN = 100
verbose_logging = True


def _create_network():
    CONVOLUTIONS_LAYER_1 = 32
    CONVOLUTIONS_LAYER_2 = 64
    CONVOLUTIONS_LAYER_3 = 64
    FLAT_SIZE = 11 * 9 * CONVOLUTIONS_LAYER_3
    FLAT_HIDDEN_NODES = 512

    # network weights
    convolution_weights_1 = tf.Variable(
        tf.truncated_normal([8, 8, STATE_FRAMES, CONVOLUTIONS_LAYER_1], stddev=0.01)
    )
    convolution_bias_1 = tf.Variable(tf.constant(0.01, shape=[CONVOLUTIONS_LAYER_1]))

    convolution_weights_2 = tf.Variable(
        tf.truncated_normal(
            [4, 4, CONVOLUTIONS_LAYER_1, CONVOLUTIONS_LAYER_2], stddev=0.01
        )
    )
    convolution_bias_2 = tf.Variable(tf.constant(0.01, shape=[CONVOLUTIONS_LAYER_2]))

    convolution_weights_3 = tf.Variable(
        tf.truncated_normal(
            [3, 3, CONVOLUTIONS_LAYER_2, CONVOLUTIONS_LAYER_3], stddev=0.01
        )
    )
    convolution_bias_3 = tf.Variable(tf.constant(0.01, shape=[CONVOLUTIONS_LAYER_2]))

    feed_forward_weights_1 = tf.Variable(
        tf.truncated_normal([FLAT_SIZE, FLAT_HIDDEN_NODES], stddev=0.01)
    )
    feed_forward_bias_1 = tf.Variable(tf.constant(0.01, shape=[FLAT_HIDDEN_NODES]))

    feed_forward_weights_2 = tf.Variable(
        tf.truncated_normal([FLAT_HIDDEN_NODES, ACTIONS_COUNT], stddev=0.01)
    )
    feed_forward_bias_2 = tf.Variable(tf.constant(0.01, shape=[ACTIONS_COUNT]))

    input_layer = tf.placeholder(
        "float", [None, SCREEN_HEIGHT, SCREEN_WIDTH, STATE_FRAMES]
    )

    hidden_convolutional_layer_1 = tf.nn.relu(
        tf.nn.conv2d(
            input_layer, convolution_weights_1, strides=[1, 4, 4, 1], padding="SAME"
        )
        + convolution_bias_1
    )

    hidden_convolutional_layer_2 = tf.nn.relu(
        tf.nn.conv2d(
            hidden_convolutional_layer_1,
            convolution_weights_2,
            strides=[1, 2, 2, 1],
            padding="SAME",
        )
        + convolution_bias_2
    )

    hidden_convolutional_layer_3 = tf.nn.relu(
        tf.nn.conv2d(
            hidden_convolutional_layer_2,
            convolution_weights_3,
            strides=[1, 1, 1, 1],
            padding="SAME",
        )
        + convolution_bias_3
    )

    hidden_convolutional_layer_3_flat = tf.reshape(
        hidden_convolutional_layer_3, [-1, FLAT_SIZE]
    )

    final_hidden_activations = tf.nn.relu(
        tf.matmul(hidden_convolutional_layer_3_flat, feed_forward_weights_1)
        + feed_forward_bias_1
    )

    output_layer = (
        tf.matmul(final_hidden_activations, feed_forward_weights_2)
        + feed_forward_bias_2
    )

    return input_layer, output_layer


_session = tf.Session()
_input_layer, _output_layer = _create_network()

_action = tf.placeholder("float", [None, ACTIONS_COUNT])
_target = tf.placeholder("float", [None])

readout_action = tf.reduce_sum(tf.multiply(_output_layer, _action), reduction_indices=1)

cost = tf.reduce_mean(tf.square(_target - readout_action))
_train_operation = tf.train.AdamOptimizer(LEARN_RATE).minimize(cost)

_observations = deque(maxlen=MEMORY_SIZE)
_last_scores = deque(maxlen=STORE_SCORES_LEN)

# set the first action to do nothing
_last_action = np.zeros(ACTIONS_COUNT)
_last_action[1] = 1

_last_state = None
_probability_of_random_action = INITIAL_RANDOM_ACTION_PROB
_time = 0

_session.run(tf.initialize_all_variables())

saver = tf.train.Saver()

if not os.path.exists(CHECKPOINT_PATH):
    os.mkdir(CHECKPOINT_PATH)

if resume:
    checkpoint = tf.train.get_checkpoint_state(CHECKPOINT_PATH)
    if checkpoint:
        saver.restore(_session, checkpoint.model_checkpoint_path)


def _choose_next_action(state):
    new_action = np.zeros([ACTIONS_COUNT])

    if random.random() <= _probability_of_random_action:
        # choose an action randomly
        action_index = random.randrange(ACTIONS_COUNT)
    else:
        # choose an action given our last state
        readout_t = _session.run(_output_layer, feed_dict={_input_layer: [state]})[0]
        if verbose_logging:
            print("Action Q-Values are %s" % readout_t)
        action_index = np.argmax(readout_t)

    new_action[action_index] = 1
    return new_action


def pre_process(screen_image):
    """change the 210x160x3 uint8 frame into 84x72 float"""
    screen_image = screen_image[32:-10, 8:-8]  # crop
    screen_image = screen_image[::2, ::2, 0]  # downsample by factor of 2
    screen_image[screen_image != 0] = 1  # set everything is either black:0 or white:1
    return screen_image.astype(np.float)


def _key_presses_from_action(action_set):
    if action_set[0] == 1:
        return 1
    elif action_set[1] == 1:
        return 2
    elif action_set[2] == 1:
        return 3
    raise Exception("Unexpected action")


def _train():
    # sample a mini_batch to train on
    mini_batch_compressed = random.sample(_observations, MINI_BATCH_SIZE)
    mini_batch = [
        pickle.loads(zlib.decompress(comp_item)) for comp_item in mini_batch_compressed
    ]

    # get the batch variables
    previous_states = [d[OBS_LAST_STATE_INDEX] for d in mini_batch]
    actions = [d[OBS_ACTION_INDEX] for d in mini_batch]
    rewards = [d[OBS_REWARD_INDEX] for d in mini_batch]
    current_states = [d[OBS_CURRENT_STATE_INDEX] for d in mini_batch]
    agents_expected_reward = []
    # this gives us the agents expected reward for each action we might take
    agents_reward_per_action = _session.run(
        _output_layer, feed_dict={_input_layer: current_states}
    )
    for i in range(len(mini_batch)):
        if mini_batch[i][OBS_TERMINAL_INDEX]:
            # this was a terminal frame so there is no future reward...
            agents_expected_reward.append(rewards[i])
        else:
            agents_expected_reward.append(
                rewards[i]
                + FUTURE_REWARD_DISCOUNT * np.max(agents_reward_per_action[i])
            )

    # learn that these actions in these states lead to this reward
    _session.run(
        _train_operation,
        feed_dict={
            _input_layer: previous_states,
            _action: actions,
            _target: agents_expected_reward,
        },
    )

    # save checkpoints for later
    if _time % SAVE_EVERY_X_STEPS == 0:
        saver.save(_session, CHECKPOINT_PATH + "/network", global_step=_time)


# env = gym.make("Breakout-v0")
env = gym.make("CartPole-v0")

observation = env.reset()
reward = 0
score_pre_game = 0
""" NG
while True:
    env.render()

    observation, reward, terminal, info = env.step(
        _key_presses_from_action(_last_action)
    )
    score_pre_game += reward

    screen_binary = pre_process(observation)

    # first frame must be handled differently
    if _last_state is None:
        # the _last_state will contain the image data from the last self.STATE_FRAMES frames
        _last_state = np.stack(
            tuple(screen_binary for _ in range(STATE_FRAMES)), axis=2
        )
    else:
        screen_binary = np.reshape(screen_binary, (SCREEN_HEIGHT, SCREEN_WIDTH, 1))
        current_state = np.append(_last_state[:, :, 1:], screen_binary, axis=2)

        _observations.append(
            zlib.compress(
                pickle.dumps(
                    (_last_state, _last_action, reward, current_state, terminal), 2
                ),
                2,
            )
        )

        # only train if done observing
        if len(_observations) > OBSERVATION_STEPS:
            _train()
            _time += 1

        if terminal:
            _last_scores.append(score_pre_game)
            score_pre_game = 0
            env.reset()
            _last_state = None
        else:
            # update the old values
            _last_state = current_state
            _last_action = _choose_next_action(_last_state)

        # gradually reduce the probability of a random action
        if (
            _probability_of_random_action > FINAL_RANDOM_ACTION_PROB
            and len(_observations) > OBSERVATION_STEPS
        ):
            _probability_of_random_action -= (
                INITIAL_RANDOM_ACTION_PROB - FINAL_RANDOM_ACTION_PROB
            ) / EXPLORE_STEPS

        print(
            "Time: %s random_action_prob: %s reward %s scores differential %s"
            % (_time, _probability_of_random_action, reward, np.mean(_last_scores))
        )
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# deep_q_cart_pole.py

# note must import tensorflow before gym
from collections import deque

# import tensorflow as tf
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()  # tensorflow2下使用tensorflow1的方法

import gym

env = gym.make("CartPole-v0")

ACTIONS_COUNT = 2
FUTURE_REWARD_DISCOUNT = 0.9
OBSERVATION_STEPS = 5000.0  # time steps to observe before training
EXPLORE_STEPS = 15000.0  # frames over which to anneal epsilon
INITIAL_RANDOM_ACTION_PROB = 1.0  # starting chance of an action being random
FINAL_RANDOM_ACTION_PROB = 0.0  # final chance of an action being random
MEMORY_SIZE = 20000  # number of observations to remember
MINI_BATCH_SIZE = 100  # size of mini batches
(
    OBS_LAST_STATE_INDEX,
    OBS_ACTION_INDEX,
    OBS_REWARD_INDEX,
    OBS_CURRENT_STATE_INDEX,
    OBS_TERMINAL_INDEX,
) = range(5)
LEARN_RATE = 1e-3
STORE_SCORES_LEN = 100
INPUT_NODES = env.observation_space.shape[0]
HIDDEN_NODES = 20

session = tf.Session()

feed_forward_weights_1 = tf.Variable(
    tf.truncated_normal([INPUT_NODES, HIDDEN_NODES], stddev=0.01)
)
feed_forward_bias_1 = tf.Variable(tf.constant(0.0, shape=[HIDDEN_NODES]))

feed_forward_weights_2 = tf.Variable(
    tf.truncated_normal([HIDDEN_NODES, ACTIONS_COUNT], stddev=0.01)
)
feed_forward_bias_2 = tf.Variable(tf.constant(0.0, shape=[ACTIONS_COUNT]))

input_placeholder = tf.placeholder("float", [None, INPUT_NODES])
hidden_layer = tf.nn.tanh(
    tf.matmul(input_placeholder, feed_forward_weights_1) + feed_forward_bias_1
)
output_layer = tf.matmul(hidden_layer, feed_forward_weights_2) + feed_forward_bias_2

action_placeholder = tf.placeholder("float", [None, ACTIONS_COUNT])
target_placeholder = tf.placeholder("float", [None])

readout_action = tf.reduce_sum(
    tf.multiply(output_layer, action_placeholder), reduction_indices=1
)

cost = tf.reduce_mean(tf.square(target_placeholder - readout_action))
train_operation = tf.train.AdamOptimizer(LEARN_RATE).minimize(cost)

observations = deque(maxlen=MEMORY_SIZE)
scores = deque(maxlen=STORE_SCORES_LEN)

# set the first action to do nothing
last_action = np.zeros(ACTIONS_COUNT)
last_action[1] = 1

probability_of_random_action = INITIAL_RANDOM_ACTION_PROB
time = 0

session.run(tf.initialize_all_variables())


def choose_next_action(state):
    new_action = np.zeros([ACTIONS_COUNT])

    if random.random() <= probability_of_random_action:
        # choose an action randomly
        action_index = random.randrange(ACTIONS_COUNT)
    else:
        # choose an action given our state
        action_values = session.run(
            output_layer, feed_dict={input_placeholder: [state]}
        )[0]
        # we will take the highest value action
        action_index = np.argmax(action_values)

    new_action[action_index] = 1
    return new_action


def train():
    # sample a mini_batch to train on
    mini_batch = random.sample(observations, MINI_BATCH_SIZE)

    # get the batch variables
    previous_states = [d[OBS_LAST_STATE_INDEX] for d in mini_batch]
    actions = [d[OBS_ACTION_INDEX] for d in mini_batch]
    rewards = [d[OBS_REWARD_INDEX] for d in mini_batch]
    current_states = [d[OBS_CURRENT_STATE_INDEX] for d in mini_batch]
    agents_expected_reward = []
    # this gives us the agents expected reward for each action we might take
    agents_reward_per_action = session.run(
        output_layer, feed_dict={input_placeholder: current_states}
    )
    for i in range(len(mini_batch)):
        if mini_batch[i][OBS_TERMINAL_INDEX]:
            # this was a terminal frame so there is no future reward...
            agents_expected_reward.append(rewards[i])
        else:
            agents_expected_reward.append(
                rewards[i]
                + FUTURE_REWARD_DISCOUNT * np.max(agents_reward_per_action[i])
            )

    # learn that these actions in these states lead to this reward
    session.run(
        train_operation,
        feed_dict={
            input_placeholder: previous_states,
            action_placeholder: actions,
            target_placeholder: agents_expected_reward,
        },
    )


last_state = env.reset()
total_reward = 0

""" NG
while True:
    env.render()
    last_action = choose_next_action(last_state)
    current_state, reward, terminal, info, kk = env.step(np.argmax(last_action))
    total_reward += reward

    if terminal:
        reward = -1.0
        scores.append(total_reward)

        print(
            "Time: %s random_action_prob: %s reward %s scores differential %s"
            % (time, probability_of_random_action, total_reward, np.mean(scores))
        )
        total_reward = 0

    # store the transition in previous_observations
    observations.append((last_state, last_action, reward, current_state, terminal))

    # only train if done observing
    if len(observations) > OBSERVATION_STEPS:
        train()
        time += 1

    # update the old values
    if terminal:
        last_state = env.reset()
    else:
        last_state = current_state

    # gradually reduce the probability of a random action
    if (
        probability_of_random_action > FINAL_RANDOM_ACTION_PROB
        and len(observations) > OBSERVATION_STEPS
    ):
        probability_of_random_action -= (
            INITIAL_RANDOM_ACTION_PROB - FINAL_RANDOM_ACTION_PROB
        ) / EXPLORE_STEPS
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# deep_q_pong.py

# note must import tensorflow before gym
from collections import deque

# import tensorflow as tf
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()  # tensorflow2下使用tensorflow1的方法

import gym

resume = True
CHECKPOINT_PATH = "deep_q_pong"
ACTIONS_COUNT = 3
SCREEN_WIDTH, SCREEN_HEIGHT = (80, 80)
FUTURE_REWARD_DISCOUNT = 0.99
OBSERVATION_STEPS = 50000.0  # time steps to observe before training
EXPLORE_STEPS = 2000000.0  # frames over which to anneal epsilon
INITIAL_RANDOM_ACTION_PROB = 1.0  # starting chance of an action being random
FINAL_RANDOM_ACTION_PROB = 0.05  # final chance of an action being random
MEMORY_SIZE = 100000  # number of observations to remember
MINI_BATCH_SIZE = 100  # size of mini batches
STATE_FRAMES = 2  # number of frames to store in the state
(
    OBS_LAST_STATE_INDEX,
    OBS_ACTION_INDEX,
    OBS_REWARD_INDEX,
    OBS_CURRENT_STATE_INDEX,
    OBS_TERMINAL_INDEX,
) = range(5)
SAVE_EVERY_X_STEPS = 10000
LEARN_RATE = 1e-6
STORE_SCORES_LEN = 1000.0
verbose_logging = True


def _create_network():
    # network weights
    convolution_weights_1 = tf.Variable(
        tf.truncated_normal([8, 8, STATE_FRAMES, 32], stddev=0.01)
    )
    convolution_bias_1 = tf.Variable(tf.constant(0.01, shape=[32]))

    convolution_weights_2 = tf.Variable(
        tf.truncated_normal([4, 4, 32, 64], stddev=0.01)
    )
    convolution_bias_2 = tf.Variable(tf.constant(0.01, shape=[64]))

    convolution_weights_3 = tf.Variable(
        tf.truncated_normal([3, 3, 64, 64], stddev=0.01)
    )
    convolution_bias_3 = tf.Variable(tf.constant(0.01, shape=[64]))

    feed_forward_weights_1 = tf.Variable(tf.truncated_normal([256, 256], stddev=0.01))
    feed_forward_bias_1 = tf.Variable(tf.constant(0.01, shape=[256]))

    feed_forward_weights_2 = tf.Variable(
        tf.truncated_normal([256, ACTIONS_COUNT], stddev=0.01)
    )
    feed_forward_bias_2 = tf.Variable(tf.constant(0.01, shape=[ACTIONS_COUNT]))

    input_layer = tf.placeholder(
        "float", [None, SCREEN_WIDTH, SCREEN_HEIGHT, STATE_FRAMES]
    )

    hidden_convolutional_layer_1 = tf.nn.relu(
        tf.nn.conv2d(
            input_layer, convolution_weights_1, strides=[1, 4, 4, 1], padding="SAME"
        )
        + convolution_bias_1
    )

    hidden_max_pooling_layer_1 = tf.nn.max_pool(
        hidden_convolutional_layer_1,
        ksize=[1, 2, 2, 1],
        strides=[1, 2, 2, 1],
        padding="SAME",
    )

    hidden_convolutional_layer_2 = tf.nn.relu(
        tf.nn.conv2d(
            hidden_max_pooling_layer_1,
            convolution_weights_2,
            strides=[1, 2, 2, 1],
            padding="SAME",
        )
        + convolution_bias_2
    )

    hidden_max_pooling_layer_2 = tf.nn.max_pool(
        hidden_convolutional_layer_2,
        ksize=[1, 2, 2, 1],
        strides=[1, 2, 2, 1],
        padding="SAME",
    )

    hidden_convolutional_layer_3 = tf.nn.relu(
        tf.nn.conv2d(
            hidden_max_pooling_layer_2,
            convolution_weights_3,
            strides=[1, 1, 1, 1],
            padding="SAME",
        )
        + convolution_bias_3
    )

    hidden_max_pooling_layer_3 = tf.nn.max_pool(
        hidden_convolutional_layer_3,
        ksize=[1, 2, 2, 1],
        strides=[1, 2, 2, 1],
        padding="SAME",
    )

    hidden_convolutional_layer_3_flat = tf.reshape(
        hidden_max_pooling_layer_3, [-1, 256]
    )

    final_hidden_activations = tf.nn.relu(
        tf.matmul(hidden_convolutional_layer_3_flat, feed_forward_weights_1)
        + feed_forward_bias_1
    )

    output_layer = (
        tf.matmul(final_hidden_activations, feed_forward_weights_2)
        + feed_forward_bias_2
    )

    return input_layer, output_layer


_session = tf.Session()
_input_layer, _output_layer = _create_network()

_action = tf.placeholder("float", [None, ACTIONS_COUNT])
_target = tf.placeholder("float", [None])

readout_action = tf.reduce_sum(tf.multiply(_output_layer, _action), reduction_indices=1)

cost = tf.reduce_mean(tf.square(_target - readout_action))
_train_operation = tf.train.AdamOptimizer(LEARN_RATE).minimize(cost)

_observations = deque()
_last_scores = deque()

# set the first action to do nothing
_last_action = np.zeros(ACTIONS_COUNT)
_last_action[1] = 1

_last_state = None
_probability_of_random_action = INITIAL_RANDOM_ACTION_PROB
_time = 0

_session.run(tf.initialize_all_variables())

saver = tf.train.Saver()

if not os.path.exists(CHECKPOINT_PATH):
    os.mkdir(CHECKPOINT_PATH)

if resume:
    checkpoint = tf.train.get_checkpoint_state(CHECKPOINT_PATH)
    if checkpoint:
        saver.restore(_session, checkpoint.model_checkpoint_path)


def _choose_next_action():
    new_action = np.zeros([ACTIONS_COUNT])

    if random.random() <= _probability_of_random_action:
        # choose an action randomly
        action_index = random.randrange(ACTIONS_COUNT)
    else:
        # choose an action given our last state
        readout_t = _session.run(
            _output_layer, feed_dict={_input_layer: [_last_state]}
        )[0]
        if verbose_logging:
            print("Action Q-Values are %s" % readout_t)
        action_index = np.argmax(readout_t)

    new_action[action_index] = 1
    return new_action


def pre_process(screen_image):
    """change the 210x160x3 uint8 frame into 6400 (80x80) float"""
    screen_image = screen_image[35:195]  # crop
    screen_image = screen_image[::2, ::2, 0]  # downsample by factor of 2
    screen_image[screen_image == 144] = 0  # erase background (background type 1)
    screen_image[screen_image == 109] = 0  # erase background (background type 2)
    screen_image[screen_image != 0] = 1  # everything else (paddles, ball) just set to 1
    return screen_image.astype(np.float)


def _key_presses_from_action(action_set):
    # 1 = still
    # 2 = up
    # 3 = down

    if action_set[0] == 1:
        return 1
    elif action_set[1] == 1:
        return 2
    elif action_set[2] == 1:
        return 3
    raise Exception("Unexpected action")


def _train():
    # sample a mini_batch to train on
    mini_batch = random.sample(_observations, MINI_BATCH_SIZE)
    # get the batch variables
    previous_states = [d[OBS_LAST_STATE_INDEX] for d in mini_batch]
    actions = [d[OBS_ACTION_INDEX] for d in mini_batch]
    rewards = [d[OBS_REWARD_INDEX] for d in mini_batch]
    current_states = [d[OBS_CURRENT_STATE_INDEX] for d in mini_batch]
    agents_expected_reward = []
    # this gives us the agents expected reward for each action we might take
    agents_reward_per_action = _session.run(
        _output_layer, feed_dict={_input_layer: current_states}
    )
    for i in range(len(mini_batch)):
        if mini_batch[i][OBS_TERMINAL_INDEX]:
            # this was a terminal frame so there is no future reward...
            agents_expected_reward.append(rewards[i])
        else:
            agents_expected_reward.append(
                rewards[i]
                + FUTURE_REWARD_DISCOUNT * np.max(agents_reward_per_action[i])
            )

    # learn that these actions in these states lead to this reward
    _session.run(
        _train_operation,
        feed_dict={
            _input_layer: previous_states,
            _action: actions,
            _target: agents_expected_reward,
        },
    )

    # save checkpoints for later
    if _time % SAVE_EVERY_X_STEPS == 0:
        saver.save(_session, CHECKPOINT_PATH + "/network", global_step=_time)


# env = gym.make("Pong-v0")
env = gym.make("CartPole-v0")
observation = env.reset()
next_action = 1

""" NG
while True:
    env.render()

    observation, reward, done, info, kk = env.step(next_action)

    if done:
        env.reset()

    terminal = False

    screen_binary = pre_process(observation)

    if reward != 0.0:
        terminal = True
        _last_scores.append(reward)
        if len(_last_scores) > STORE_SCORES_LEN:
            _last_scores.popleft()

    # first frame must be handled differently
    if _last_state is None:
        # the _last_state will contain the image data from the last self.STATE_FRAMES frames
        _last_state = np.stack(
            tuple(screen_binary for _ in range(STATE_FRAMES)), axis=2
        )
        next_action = _key_presses_from_action(_last_action)
    else:
        screen_binary = np.reshape(screen_binary, (SCREEN_WIDTH, SCREEN_HEIGHT, 1))
        current_state = np.append(_last_state[:, :, 1:], screen_binary, axis=2)

        # store the transition in previous_observations
        _observations.append(
            (_last_state, _last_action, reward, current_state, terminal)
        )

        if len(_observations) > MEMORY_SIZE:
            _observations.popleft()

        # only train if done observing
        if len(_observations) > OBSERVATION_STEPS:
            _train()
            _time += 1

        # update the old values
        _last_state = current_state

        _last_action = _choose_next_action()

        # gradually reduce the probability of a random action
        if (
            _probability_of_random_action > FINAL_RANDOM_ACTION_PROB
            and len(_observations) > OBSERVATION_STEPS
        ):
            _probability_of_random_action -= (
                INITIAL_RANDOM_ACTION_PROB - FINAL_RANDOM_ACTION_PROB
            ) / EXPLORE_STEPS

        print(
            "Time: %s random_action_prob: %s reward %s scores differential %s"
            % (
                _time,
                _probability_of_random_action,
                reward,
                sum(_last_scores) / STORE_SCORES_LEN,
            )
        )

        next_action = _key_presses_from_action(_last_action)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# q_learning_1d.py

# import tensorflow as tf
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()  # tensorflow2下使用tensorflow1的方法

states = [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
NUM_STATES = len(states)
NUM_ACTIONS = 2
DISCOUNT_FACTOR = 0.5


def one_hot_state(index):
    array = np.zeros(NUM_STATES)
    array[index] = 1.0
    return array


session = tf.Session()
state = tf.placeholder("float", [None, NUM_STATES])
targets = tf.placeholder("float", [None, NUM_ACTIONS])

weights = tf.Variable(tf.constant(0.0, shape=[NUM_STATES, NUM_ACTIONS]))

output = tf.matmul(state, weights)

loss = tf.reduce_mean(tf.square(output - targets))
train_operation = tf.train.GradientDescentOptimizer(1.0).minimize(loss)

session.run(tf.initialize_all_variables())

for _ in range(50):
    state_batch = []
    rewards_batch = []

    for state_index in range(NUM_STATES):
        state_batch.append(one_hot_state(state_index))

        minus_action_index = (state_index - 1) % NUM_STATES
        plus_action_index = (state_index + 1) % NUM_STATES

        minus_action_state_reward = session.run(
            output, feed_dict={state: [one_hot_state(minus_action_index)]}
        )
        plus_action_state_reward = session.run(
            output, feed_dict={state: [one_hot_state(plus_action_index)]}
        )

        minus_action_q_value = DISCOUNT_FACTOR * (
            states[minus_action_index] + np.max(minus_action_state_reward)
        )
        plus_action_q_value = DISCOUNT_FACTOR * (
            states[plus_action_index] + np.max(plus_action_state_reward)
        )

        action_rewards = [minus_action_q_value, plus_action_q_value]
        rewards_batch.append(action_rewards)

    session.run(train_operation, feed_dict={state: state_batch, targets: rewards_batch})

    print(
        [
            states[x]
            + np.max(session.run(output, feed_dict={state: [one_hot_state(x)]}))
            for x in range(NUM_STATES)
        ]
    )

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# q_learning_1d_terminal.py

# import tensorflow as tf
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()  # tensorflow2下使用tensorflow1的方法

states = [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
terminal = [False, False, False, False, True, False, False, False, False, False]
NUM_STATES = len(states)
NUM_ACTIONS = 2
DISCOUNT_FACTOR = 0.5


def one_hot_state(index):
    array = np.zeros(NUM_STATES)
    array[index] = 1.0
    return array


session = tf.Session()
state = tf.placeholder("float", [None, NUM_STATES])
targets = tf.placeholder("float", [None, NUM_ACTIONS])

weights = tf.Variable(tf.constant(0.0, shape=[NUM_STATES, NUM_ACTIONS]))

output = tf.matmul(state, weights)

loss = tf.reduce_mean(tf.square(output - targets))
train_operation = tf.train.GradientDescentOptimizer(1.0).minimize(loss)

session.run(tf.initialize_all_variables())

for _ in range(50):
    state_batch = []
    rewards_batch = []

    for state_index in range(NUM_STATES):
        state_batch.append(one_hot_state(state_index))

        minus_action_index = (state_index - 1) % NUM_STATES
        plus_action_index = (state_index + 1) % NUM_STATES

        if terminal[minus_action_index]:
            minus_action_q_value = DISCOUNT_FACTOR * states[minus_action_index]
        else:
            minus_action_state_reward = session.run(
                output, feed_dict={state: [one_hot_state(minus_action_index)]}
            )
            minus_action_q_value = DISCOUNT_FACTOR * (
                states[minus_action_index] + np.max(minus_action_state_reward)
            )

        if terminal[plus_action_index]:
            plus_action_q_value = DISCOUNT_FACTOR * states[plus_action_index]
        else:
            plus_action_state_reward = session.run(
                output, feed_dict={state: [one_hot_state(plus_action_index)]}
            )
            plus_action_q_value = DISCOUNT_FACTOR * (
                states[plus_action_index] + np.max(plus_action_state_reward)
            )

        action_rewards = [minus_action_q_value, plus_action_q_value]
        rewards_batch.append(action_rewards)

    session.run(train_operation, feed_dict={state: state_batch, targets: rewards_batch})

    print(
        [
            states[x]
            + (1 - float(terminal[x]))
            * np.max(session.run(output, feed_dict={state: [one_hot_state(x)]}))
            for x in range(NUM_STATES)
        ]
    )

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Deep learning(DL)
convolutional neural networks (CNN卷積神經網路) - deep feed-forward neural networks (discussed today)
recurrent neural networks (RNN) - connections between nodes can go backward (used e.g. for speech recognition)
generative adversarial networks (GAN) - system of two neural networks competing with each other (one generates fake data and the other compare them with real data)
"""

# just to overwrite default colab style
plt.style.use("default")
plt.style.use("seaborn-talk")

# Convolutional neural networks 卷積神經網路

from skimage import io
from scipy.signal import convolve2d

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Albert_Einstein_Head.jpg/220px-Albert_Einstein_Head.jpg"

# image = skimage.io.imread(filename, True)  # True:轉為灰階
img = io.imread(url, True)

# define first filter
filter01 = np.array([[0, 1, 0], [0, -2, 0], [0, 1, 0]])

# define first filter
filter02 = np.array([[0, 0, 0], [1, -2, 1], [0, 0, 0]])

# apply filters
out01 = convolve2d(img, filter01, mode="valid")
out02 = convolve2d(img, filter02, mode="same")

plt.subplot(131)
plt.title(img.shape)
plt.imshow(img, cmap="gray")

plt.subplot(132)
plt.title(out01.shape)
plt.imshow(out01, cmap="gray")

plt.subplot(133)
plt.title(out02.shape)
plt.imshow(out02, cmap="gray")

plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個

from skimage.measure import block_reduce

images = [img]

# perform 5 poolings
for i in range(5):
    images.append(block_reduce(images[-1], (2, 2), np.max))

# plot them all
for i in range(6):
    plt.subplot(231 + i)
    plt.imshow(images[i], cmap="gray")

plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個

# CNN structure

# Deep MNIST
"""
    Last week we got about 92% accuracy on MNIST dataset
    Today we are going to do better with CNN
    First, lets load the data
"""

import tensorflow as tf

# tensorflow2下使用tensorflow1的方法
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()


"""
先將 tutorials
放在
C:/Users/070601/AppData/Local/Programs/Python/Python311/Lib/site-packages/tensorflow/examples
之下
"""

from tensorflow.examples.tutorials.mnist import input_data

# import tensorflow.examples.tutorials.mnist.input_data as input_data

# to avoid warnings printed in the notebook
# tf.logging.set_verbosity(tf.logging.ERROR)

# one hot -> label 0-9 -> 0...01, 0...10, ...
mnist = input_data.read_data_sets(
    "C:/_git/vcs/_4.python/ml/data/MNIST_data/", one_hot=True
)

# Create placeholders for tensors to fed

x = tf.placeholder(tf.float32, [None, 784])  # img -> 28x28 -> 784
y = tf.placeholder(tf.float32, [None, 10])  # 10 classes

# Build the network

# reshape to 28x28 image with 1 color channel
x_image = tf.reshape(x, [-1, 28, 28, 1])

##### The first convolution (conv1) with 32 filters 5x5 #####

# init weights randomly from normal distribution with bounds
W_conv1 = tf.Variable(tf.truncated_normal([5, 5, 1, 32], stddev=0.1))

# init bias with 0.1
b_conv1 = tf.Variable(tf.constant(0.1, shape=[32]))

# create convolution
# input tensor has 4 dimensions: [batch, height, width, channels]
# strides defines how to move in each dimension
# padding = "SAME" (zero padding) or "VALID" (no padding)
conv1 = tf.nn.conv2d(x_image, W_conv1, strides=[1, 1, 1, 1], padding="SAME")

# ReLU activation funtion
h_conv1 = tf.nn.relu(conv1 + b_conv1)

# pooling layer 2x2 with stride 2
h_pool1 = tf.nn.max_pool(
    h_conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME"
)

##### The second convolutional layer - maps 32 feature maps to 64 #####

W_conv2 = tf.Variable(tf.truncated_normal([5, 5, 32, 64], stddev=0.1))
b_conv2 = tf.Variable(tf.constant(0.1, shape=[64]))

# last pooling layer is an input for this layer
conv2 = tf.nn.conv2d(h_pool1, W_conv2, strides=[1, 1, 1, 1], padding="SAME")
h_conv2 = tf.nn.relu(conv2 + b_conv2)
h_pool2 = tf.nn.max_pool(
    h_conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME"
)

# Convolution is done with zero padding - preserves image size
# Each pooling downsamples by 2x
# 28x28 -> 14x14x32 -> 7x7x64

###### Fully connected layer maps above to 1024 features #####

W_fc1 = tf.Variable(tf.truncated_normal([7 * 7 * 64, 1024], stddev=0.1))
b_fc1 = tf.Variable(tf.constant(0.1, shape=[1024]))

# we need to reshape last layer
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])

# matmul - matrix multiplication
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

##### Dropout layer #####

# keep_prob controls no. of deactivated neurons
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

##### Output layer #####

# Map the 1024 features to 10 classes, one for each digit
W_fc2 = tf.Variable(tf.truncated_normal([1024, 10], stddev=0.1))
b_fc2 = tf.Variable(tf.constant(0.1, shape=[10]))

out = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

# loss function
cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=out)
)

# training step - using Adam SGD with initial learning rate 1e-4
# train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy) old
train_step = tf.compat.v1.train.AdamOptimizer(1e-4).minimize(cross_entropy)

# For convenience we define a method to measure accuracy

# argmax returns the index of the heighest index in a tensor
# equal returns True / False if prediction is equal/not equal to true label
# cast would convert True/False to 1/0, so we can calculate the average

correct_prediction = tf.equal(tf.argmax(out, 1), tf.argmax(y, 1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 必須使用 GPU
# Make sure we are running on GPU
device_name = tf.test.gpu_device_name()

print("device_name :", device_name)

print("無 GPU 跳過")
"""
if device_name != "/device:GPU:0":
    raise SystemError("無 GPU")
print("Found GPU at: {}".format(device_name))

# Found GPU at: /device:GPU:0

# Finally we can train the network on MNIST dataset

# to use GPU through Colaboratory
config = tf.ConfigProto()
config.gpu_options.allow_growth = True

nof_iterations = 20000  # number of training steps
test_every = 1000  # calculate accuracy every test_every step
batch_size = 32  # traning batch size
acc_batch = 2048  # the size of a subset used to measure accuracy

train_accuracy = []
valid_accuracy = []

with tf.Session(config=config) as sess:
    # initialize weights and biases
    sess.run(tf.global_variables_initializer())

    for i in range(nof_iterations):
        # take mini batch from MNIST dataset
        batch = mnist.train.next_batch(batch_size)

        # every test_every iterations save current accuracy scores
        if i % test_every == 0:
            # for testing we do not want dropout neurons - keep_prob = 1
            # to save time we calculate accuracy on a subset of data

            train_batch = mnist.train.next_batch(acc_batch)
            train_accuracy.append(
                accuracy.eval(
                    feed_dict={x: train_batch[0], y: train_batch[1], keep_prob: 1.0}
                )
            )

            test_batch = mnist.test.next_batch(acc_batch)
            valid_accuracy.append(
                accuracy.eval(
                    feed_dict={x: test_batch[0], y: test_batch[1], keep_prob: 1.0}
                )
            )

        # run training step with 50% neurons deactivated
        train_step.run(feed_dict={x: batch[0], y: batch[1], keep_prob: 0.5})

    # calculate the accuracy on the whole testing dataset
    print(
        "test accuracy %g"
        % accuracy.eval(
            feed_dict={x: mnist.test.images, y: mnist.test.labels, keep_prob: 1.0}
        )
    )

show()
# test accuracy 0.9915

iterations = np.linspace(0, nof_iterations, nof_iterations // test_every)

plt.xlabel("Iteration")
plt.ylabel("Accuracy")

plt.plot(iterations, train_accuracy, label="Training accuracy")
plt.plot(iterations, valid_accuracy, label="Valid accuracy")

plt.legend()
show()
"""
print("------------------------------------------------------------")  # 60個

# Batch normalization

# BN layer

# Data augmentation

# Flipping

from skimage import io
from scipy.signal import convolve2d

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Albert_Einstein_Head.jpg/220px-Albert_Einstein_Head.jpg"

# image = skimage.io.imread(filename, True)  # True:轉為灰階
img = io.imread(url, True)


img_flip_x = np.flip(img, axis=1)
img_flip_y = np.flip(img, axis=0)
img_flip_xy = np.flip(img_flip_y, axis=1)

plt.subplot(221)
plt.title("original")
plt.imshow(img, cmap="gray")

plt.subplot(222)
plt.title("x-flip")
plt.imshow(img_flip_x, cmap="gray")

plt.subplot(223)
plt.title("y-flip")
plt.imshow(img_flip_y, cmap="gray")

plt.subplot(224)
plt.title("xy-flip")
plt.imshow(img_flip_xy, cmap="gray")

plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個

# Rotation

from scipy.ndimage.interpolation import rotate

for i, angle in enumerate((30, 60, 90, 120)):
    img_rot = rotate(img, angle=angle)
    plt.subplot(221 + i)
    plt.title("angle = {}".format(angle))
    plt.imshow(img_rot, cmap="gray")

plt.tight_layout()

show()

print("------------------------------------------------------------")  # 60個

# Translation

from scipy.ndimage.interpolation import shift

for i, (dx, dy) in enumerate(((30, 30), (60, 60), (-30, -30), (-60, -60))):
    img_trans = shift(img, (dx, dy))
    plt.subplot(221 + i)
    plt.title("dx, dy = {}, {}".format(dx, dy))
    plt.imshow(img_trans, cmap="gray")

plt.tight_layout()

show()

print("------------------------------------------------------------")  # 60個

# Scaling

from skimage.transform import rescale

for i, scale in enumerate((1.0, 0.9, 0.8, 0.7)):
    img_scaled = rescale(img, scale).copy()
    img_scaled = np.pad(
        img_scaled, (img.shape[0] - img_scaled.shape[0]) // 2, mode="constant"
    )
    plt.subplot(221 + i)
    plt.title("scale = {}".format(scale))
    plt.imshow(img_scaled, cmap="gray")

plt.tight_layout()

show()

print("------------------------------------------------------------")  # 60個

# Noise

# salt and pepper noise
for i, prob in enumerate((0.05, 0.10, 0.15, 0.20)):
    img_noised = img.copy()
    rnd = np.random.rand(img.shape[0], img.shape[1])
    img_noised[rnd < prob] = 0  # pepper
    img_noised[rnd > 1 - prob] = 1  # salt
    plt.subplot(221 + i)
    plt.title("prob = {}".format(prob))
    plt.imshow(img_noised, cmap="gray")

plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# sugar不能用 import theano 失敗

"""
Neural Network
    Artificial neural network (in particular deep NN) is the most popular machine learning method these days
    They are inspired by human brains (at least initially)
    Artifical neuron is a mathematical function
    Neurons are connected with each other (kind of synapses)
    Usually connections have some weights
    Today, feedforward neural networks (multilayer perceptrons) will be discussed
    However, before we go there, lets start with linear and logistic regression
"""

# just to overwrite default colab style
plt.style.use("default")
plt.style.use("seaborn-talk")

# Linear regression

N = 100  # number of samples

a = 0.50  # slope
b = 0.50  # y-intercept
s = 0.25  # sigma

### GENERATE SAMPLES ###

X = 10.0 * np.random.sample(N)  # features
Y = [(a * X[i] + b) + np.random.normal(0, s) for i in range(N)]  # targets

### PLOT SAMPLES ###

plt.xlabel("Feature")
plt.ylabel("Target")
plt.scatter(X, Y, marker=".")
show()

print("------------------------------------------------------------")  # 60個

#!pip install theano

import theano
import theano.tensor as T

x = T.vector("x")  # feature vector
y = T.vector("y")  # target vector

# weights initialized randomly
# a = theano.shared(np.random.randn(), name = 'w')
# b = theano.shared(np.random.randn(), name = 'b')

# initial weights by hand for demonstration (random may be to close)
a = theano.shared(-0.5, name="w")
b = theano.shared(1.0, name="b")


pred = T.dot(x, a) + b  # hyphothesis
cost = T.sum(T.pow(pred - y, 2)) / N  # cost function
grad_a, grad_b = T.grad(cost, [a, b])  # gradients

# And finally, we define gradient descent method (which also returns the value of the cost function)

alpha = 0.005  # learning rate

# at each training step we update weights:
# w -> w - alpha * grad_w and b -> b - alpha * grad_b
train = theano.function(
    inputs=[x, y],
    outputs=cost,
    updates=((a, a - alpha * grad_a), (b, b - alpha * grad_b)),
)

# Each training step involves the full cycle on training data (epoch)

n_epochs = 1000  # number of training steps / epochs
costs = []  # to keep track on the value of cost function on each step
weights = []  # to store few set of weights

keep = (0, 10, 100, 500, 1000)  # save result for some epochs passed

for i in range(n_epochs + 1):
    if i in keep:
        weights.append((a.get_value(), b.get_value()))

    costs.append(train(X, Y))

# Finally, we can visualize the results

plt.figure(figsize=(10, 15))
n_rows = 3
n_cols = 2

for i, (a_, b_) in enumerate(weights):
    plt.subplot(n_rows, n_cols, i + 1)

    plt.title("Epoch %i: y = %.2f x + %.2f" % (keep[i], a_, b_))
    plt.xlabel("Feature")
    plt.ylabel("Target")

    x_ = np.arange(0, 10, 0.1)

    plt.plot(x_, a_ * x_ + b_, color="C1")
    plt.scatter(X, Y, marker=".")


plt.subplot(n_rows, n_cols, len(weights) + 1)
plt.title("Cost function")
plt.xlabel("Epoch")
plt.ylabel("L")
plt.ylim([0, 0.2])

plt.plot(range(len(costs)), costs)

plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x_ = np.arange(-10, 10, 0.1)

plt.plot(x_, 1 / (1 + np.exp(-x_)))

plt.xlabel("x")
plt.ylabel("$1/(1 + e^{-x})$")
plt.title("Logistic function 邏輯斯函數")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Once again lets use theano

import theano
import theano.tensor as T

x = T.vector("x")  # feature vector
y = T.vector("y")  # target vector

a = theano.shared(np.random.randn(), name="w")  # weights initialized randomly
b = theano.shared(np.random.randn(), name="b")

hypo = 1 / (1 + T.exp(-T.dot(x, a) - b))  # hyphothesis
xent = -y * T.log(hypo) - (1 - y) * T.log(1 - hypo)  # cross-entropy loss function
cost = xent.sum()  # cost function
grad_a, grad_b = T.grad(cost, [a, b])  # gradients

alpha = 0.01  # learning rate

# at each training step we update weights:
# w -> w - alpha * grad_w and b -> b - alpha * grad_b
train = theano.function(
    inputs=[x, y],
    outputs=cost,
    updates=((a, a - alpha * grad_a), (b, b - alpha * grad_b)),
)

print("------------------------------------------------------------")  # 60個

x_min = min(X)
x_max = max(X)

s = lambda x: (x - x_min) / (x_max - x_min)  # scale

# Now, we train the model on normalized data

n_epochs = 1000

[train(s(X), Y) for _ in range(n_epochs)]

plt.xlabel("Study time [h]")
plt.ylabel("Success")

plt.scatter(X, Y)

h_ = np.arange(0, 60, 0.01)

plt.plot(h_, 1 / (1 + np.exp(-s(h_) * a.get_value() - b.get_value())), "C1")

plt.plot([0, 60], [0.5, 0.5], "C2--")
show()

print("------------------------------------------------------------")  # 60個

# Multinominal logistic regression

# Logit approach


def grade(init_know, study_time):
    """Arbitrary grading system."""
    score = np.random.normal(init_know + 2 * study_time, 5)

    if score > 90:
        return 3  # bdb
    elif score > 70:
        return 2  # db
    elif score > 50:
        return 1  # dst
    else:
        return 0  # ndst


# The training set

N = 1000  # number of students

X = np.random.sample((N, 2)) * [100, 50]
Y = np.array([grade(*student) for student in X], dtype="int32")

plt.xlabel("Initial knowledge")
plt.ylabel("Study time")

for student, g in zip(X, Y):
    plt.scatter(*student, color="C" + str(g), marker=".")
show()

# Data preparation

X_train = np.multiply(X, np.array([1 / 100, 1 / 50]))

# Lets add 1 for bias term to the dataset

X_train = np.hstack((np.ones((N, 1)), X_train))

# How does it look?

print("Original:", X[:5], "Preprocessed:", X_train[:5], sep="\n\n")

# Training
# The implementation of MLR in theano

import theano
import theano.tensor as T

x = T.matrix("x")  # feature vectors
y = T.ivector("y")  # target vector

W = theano.shared(np.random.randn(3, 4))  # weight matrix (2 features + bias,
#                4 possible outcomes)

hypo = T.nnet.softmax(T.dot(x, W))  # hyphothesis
cost = -T.mean(T.log(hypo)[T.arange(y.shape[0]), y])  # cost function
grad_W = T.grad(cost=cost, wrt=W)  # gradients

alpha = 0.5  # learning rate

# define a training step
train = theano.function(inputs=[x, y], outputs=cost, updates=[(W, W - alpha * grad_W)])

# predict a class label
predict = theano.function(inputs=[x], outputs=T.argmax(hypo, axis=1))

# The training process on normalized data

n_epochs = 10000
acc_train = []  # accuracy on training dataset

for _ in range(n_epochs):
    # do a single step of gradient descent
    train(X_train, Y)
    # calculate accuracy with current set of weights
    acc_train.append((Y == predict(X_train)).sum() / Y.shape[0])

plt.xlabel("Epoch")
plt.ylabel("Cost")

plt.plot(range(len(acc_train)), acc_train)
show()

print("------------------------------------------------------------")  # 60個

# Validation
# First we need unseen data for testing

# another set of students
X_test = np.random.sample((N, 2)) * [100, 50]
Y_test = np.array([grade(*student) for student in X_test], dtype="int32")

# normalize and add bias
X_test_normalized = np.multiply(X_test, np.array([1 / 100, 1 / 50]))
X_test_normalized = np.hstack((np.ones((N, 1)), X_test_normalized))

# To predict a grade we use the function predict defined earlier

Y_pred = predict(X_test_normalized)

# We can visualize the prediction

plt.xlabel("Initial knowledge")
plt.ylabel("Study time")

for student, g in zip(X_test, Y_pred):
    plt.scatter(*student, color="C" + str(g), marker=".")
show()

print("------------------------------------------------------------")  # 60個

# 計算準確率

cc = (Y_test == Y_pred).sum() / Y_test.shape[0]
print(cc)

# Softmax visualization

softmax = theano.function(inputs=[x], outputs=hypo)

probs = softmax(X_test_normalized)

print(probs.shape)

# (1000, 4)

# We can plot each class separately

from mpl_toolkits.mplot3d import Axes3D

grades = ("ndst", "dst", "db", "bdb")

for i in range(4):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.set_xlabel("Initial knowledge", labelpad=20)
    ax.set_ylabel("Study time", labelpad=20)

    ax.set_title("Grade: " + grades[i])

    ax.scatter(X_test.T[0], X_test.T[1], probs.T[i], marker=".")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Neural Networks
# Here are some helpful functions to draw neural networks
"""
radius = 0.3

arrow_kwargs = dict(head_width=0.05, fc="black")


def draw_connecting_arrow(ax, circ1, rad1, circ2, rad2):
    theta = np.arctan2(circ2[1] - circ1[1], circ2[0] - circ1[0])

    starting_point = (circ1[0] + rad1 * np.cos(theta), circ1[1] + rad1 * np.sin(theta))

    length = (
        circ2[0] - circ1[0] - (rad1 + 1.4 * rad2) * np.cos(theta),
        circ2[1] - circ1[1] - (rad1 + 1.4 * rad2) * np.sin(theta),
    )

    ax.arrow(starting_point[0], starting_point[1], length[0], length[1], **arrow_kwargs)


def draw_circle(ax, center, radius):
    circ = plt.Circle(center, radius, fill=False, lw=2)
    ax.add_patch(circ)


def draw_net(input_size, output_size, hidden_layers=[], w=6, h=4):
    # Draw a network
    x = 0  # initial layer position

    ax = plt.subplot()
    ax.set_aspect("equal")
    ax.axis("off")

    ax.set_xlim([-2, -2 + w])
    ax.set_ylim([-h / 2, h / 2 + 1])

    # set y position
    y_input = np.arange(-(input_size - 1) / 2, (input_size + 1) / 2, 1)
    y_output = np.arange(-(output_size - 1) / 2, (output_size + 1) / 2, 1)
    y_hidden = [np.arange(-(n - 1) / 2, (n + 1) / 2, 1) for n in hidden_layers]

    # draw input layer
    plt.text(x, h / 2 + 0.5, "Input\nLayer", ha="center", va="top")

    for i, y in enumerate(y_input):
        draw_circle(ax, (x, y), radius)
        ax.text(
            x - 0.9,
            y,
            "$x_%i$" % (input_size - 1 - i),
            ha="right",
            va="center",
        )
        draw_connecting_arrow(ax, (x - 0.9, y), 0.1, (x, y), radius)

    last_layer = y_input  # last layer y positions

    # draw hidden layers
    for ys in y_hidden:
        # shift x
        x += 2
        plt.text(x, h / 2 + 0.5, "Hidden\nLayer", ha="center", va="top")

        # draw neurons for each hidden layer
        for i, y1 in enumerate(ys):
            draw_circle(ax, (x, y1), radius)

            # connect a neuron with all neurons from previous layer
            if i != len(ys) - 1:  # skip bias
                for y2 in last_layer:
                    draw_connecting_arrow(ax, (x - 2, y2), radius, (x, y1), radius)

        # update last layer
        last_layer = ys

    x += 2  # update position for output layer

    # draw output layer
    plt.text(x, h / 2 + 0.5, "Output\nLayer", ha="center", va="top")

    for i, y1 in enumerate(y_output):
        draw_circle(ax, (x, y1), radius)
        ax.text(x + 0.8, y1, "Output", ha="left", va="center")
        draw_connecting_arrow(ax, (x, y1), radius, (x + 0.8, y1), 0.1)

        # connect each output neuron with all neurons from previous layer
        for y2 in last_layer:
            draw_connecting_arrow(ax, (x - 2, y2), radius, (x, y1), radius)
    show()


draw_net(3, 1)

draw_net(3, 1, [5], w=9, h=6)

draw_net(3, 1, [5, 7, 9, 5], w=14, h=10)

draw_net(3, 4, [5, 7, 9, 5], w=14, h=10)

draw_net(3, 2, [3], w=9, h=4)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
# Single neuron approach

draw_net(3, 1)

import theano
import theano.tensor as T

x = T.matrix("x")  # feature vector
y = T.vector("y")  # target vector

w = theano.shared(np.random.randn(2), name="w")  # weights initialized randomly
b = theano.shared(np.random.randn(), name="b")  # bias term

hypo = 1 / (1 + T.exp(-T.dot(x, w) - b))  # hyphothesis
xent = -y * T.log(hypo) - (1 - y) * T.log(1 - hypo)  # cross-entropy loss function
cost = xent.sum()  # cost function
grad_w, grad_b = T.grad(cost, [w, b])  # gradients

alpha = 0.1  # learning rate

# at each training step we update weights:
# w -> w - alpha * grad_w and b -> b - alpha * grad_b
train = theano.function(
    inputs=[x, y],
    outputs=cost,
    updates=((w, w - alpha * grad_w), (b, b - alpha * grad_b)),
)

predict = theano.function(inputs=[x], outputs=hypo)

# Train for all gates and save prediction

N = 1000

gates = ("AND", "OR", "XOR")
gates_pred = {}

for gate, data in zip(gates, (Y_and, Y_or, Y_xor)):
    # reset weights
    w.set_value(np.random.randn(2))
    b.set_value(np.random.randn())

    # train neuron
    [train(X, data) for _ in range(N)]
    gates_pred[gate] = predict(X)

# Let's see the result

for gate in gates:
    for i, (x1, x2) in enumerate(X):
        print("{} {} {} -> {}".format(x1, gate, x2, gates_pred[gate][i]))
    print()

# Neural network approach

draw_net(3, 1, [3], w=8)

import theano
import theano.tensor as T

x = T.matrix("x")  # feature vector
y = T.vector("y")  # target vector

# first layer's weights (including bias)
w1 = theano.shared(np.random.randn(3, 2), name="w1")
# second layer's weights (including bias)
w2 = theano.shared(np.random.randn(3), name="w2")

h = T.nnet.sigmoid(T.dot(x, w1[:2,]) + w1[2,])  # hidden layer
o = T.nnet.sigmoid(T.dot(h, w2[:2,]) + w2[2,])  # output layer

xent = -y * T.log(o) - (1 - y) * T.log(1 - o)  # cross-entropy loss function
cost = xent.sum()  # cost function
grad_w1, grad_w2 = T.grad(cost, [w1, w2])  # gradients

alpha = 0.1  # learning rate

# at each training step we update weights:
# w -> w - alpha * grad_w and b -> b - alpha * grad_b
train = theano.function(
    inputs=[x, y],
    outputs=cost,
    updates=((w1, w1 - alpha * grad_w1), (w2, w2 - alpha * grad_w2)),
)

predict = theano.function(inputs=[x], outputs=o)

# Train on XOR and print prediction

[train(X, Y_xor) for _ in range(10000)]
prediction = predict(X)

for i, (x1, x2) in enumerate(X):
    print("{} XOR {} -> {}".format(x1, x2, prediction[i]))

# Again the same, but with tensorflow

import tensorflow as tf

# x = T.matrix('x') # feature vector
# y = T.vector('y') # target vector
x = tf.placeholder(tf.float32, [4, 2])
y = tf.placeholder(tf.float32, [4, 1])

# w1 = theano.shared(np.random.randn(3,2), name = 'w1')
# w2 = theano.shared(np.random.randn(3), name = 'w2')
w1 = tf.Variable(tf.random_normal([3, 2]), name="w1")
w2 = tf.Variable(tf.random_normal([3, 1]), name="w2")

# h = T.nnet.sigmoid(T.dot(x, w1[:2,]) + w1[2,])
# o = T.nnet.sigmoid(T.dot(h, w2[:2,]) + w2[2,])
h = tf.sigmoid(tf.add(tf.matmul(x, w1[:2,]), w1[2,]))
o = tf.sigmoid(tf.add(tf.matmul(h, w2[:2,]), w2[2,]))

# xent = - y * tf.log(o) - (1 - y) * tf.log(1 - o)
xent = tf.losses.log_loss(y, o)
cost = tf.reduce_mean(xent)

opt = tf.train.GradientDescentOptimizer(0.1).minimize(cost)

init = tf.global_variables_initializer()

X = [[0, 0], [1, 0], [0, 1], [1, 1]]
Y_xor = [[0], [1], [1], [0]]

with tf.Session() as sess:
    sess.run(init)
    [sess.run(opt, feed_dict={x: X, y: Y_xor}) for _ in range(10000)]
    print(sess.run(o, feed_dict={x: X}))

# Simple regression with NN

# plot a sample
X, Y = get_dataset(100, 0.25)

draw_net(2, 1, [4], w=10)

print("最後一次出現 draw_net(")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import tensorflow as tf

# tensorflow2下使用tensorflow1的方法
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

x = tf.placeholder(tf.float32, [None, 1])
y = tf.placeholder(tf.float32, [None, 1])

w1 = tf.Variable(tf.random_normal([1, 3]), name="w1")
w2 = tf.Variable(tf.random_normal([3, 1]), name="w2")

b1 = tf.Variable(tf.random_normal([3]), name="b1")
b2 = tf.Variable(tf.random_normal([1]), name="b2")

h = tf.nn.sigmoid(tf.add(tf.matmul(x, w1), b1))
o = tf.add(tf.matmul(h, w2), b2)

xent = tf.losses.mean_squared_error(y, o)
cost = tf.reduce_mean(xent)

opt = tf.train.GradientDescentOptimizer(0.25).minimize(cost)

init = tf.global_variables_initializer()

X, Y = get_dataset(100, 0.25)
x_ = np.arange(-10, 10, 0.1)

# We need to reshape out training data

X_train = np.reshape(X, (-1, 1))
Y_train = np.reshape(Y, (-1, 1))

print("Original", X[:5], Y[:5], sep="\n\n")
print("\nReshaped", X_train[:5], Y_train[:5], sep="\n\n")

# And we can train the model

X_test = np.arange(-1, 1, 0.01).reshape(-1, 1)

with tf.Session() as sess:
    sess.run(init)
    [sess.run(opt, feed_dict={x: X_train, y: Y_train}) for _ in range(10000)]
    prediction = sess.run(o, feed_dict={x: X_test})

plt.scatter(X_test, prediction, color="C2", label="NN")
plt.scatter(X, Y, color="C1", label="Data")
plt.plot(x_, np.sin(np.pi * x_), "C0--", label="Truth")

plt.legend()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
MNIST
THE MNIST DATABASE of handwritten digits
The MNIST database of handwritten digits, available from this page, has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image.
It is a good database for people who want to try learning techniques and pattern recognition methods on real-world data while spending minimal efforts on preprocessing and formatting.
We can grab MNIST dataset using tensorflow.examples.tutorials.mnist
"""

import tensorflow as tf

# tensorflow2下使用tensorflow1的方法
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

from tensorflow.examples.tutorials.mnist import input_data

# to avoid warnings printed in the notebook
tf.logging.set_verbosity(tf.logging.ERROR)

# one hot -> label 0-9 -> 0...01, 0...10, ...
mnist = input_data.read_data_sets(
    "C:/_git/vcs/_4.python/ml/data/MNIST_data/", one_hot=True
)

print(mnist.train.images.shape)

# (55000, 784)

for i in range(4):
    plt.subplot(221 + i)

    # random training sample
    index = np.random.randint(len(mnist.train.images))

    # train.images contains images in a form of a vector
    # so we reshape it back to 28x28
    plt.imshow(mnist.train.images[index].reshape(28, 28), cmap="gray")

    # train.labels contains labels in one hot format
    plt.title(mnist.train.labels[index])

plt.tight_layout()
show()

x = tf.placeholder(tf.float32, [None, 784])  # img -> 28x28 -> 784
y = tf.placeholder(tf.float32, [None, 10])  # 10 classes

W = tf.Variable(tf.zeros([784, 10]))  # weights
b = tf.Variable(tf.zeros([10]))  # bias

out = tf.nn.softmax(tf.matmul(x, W) + b)

# Define the loss function and optimizer

cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=out)
)

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# Train the model

# create a session
sess = tf.Session()
# initialize weights
sess.run(tf.global_variables_initializer())

for _ in range(10000):
    # here instead of updating weights after the whole training set
    # we use batch size 100 (more about that in the next section)
    batch_xs, batch_ys = mnist.train.next_batch(100)

    # train_step is minimizing cross_entropy with learning rate 0.5 using GD
    # we pass small batches to placeholders x and y
    sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})

# Validate the model

# argmax returns the index of the heighest index in a tensor
# equal returns True / False if prediction is equal/not equal to true label
# cast would convert True/False to 1/0, so we can calculate the average
correct_prediction = tf.equal(tf.argmax(out, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print(sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels}))

sess.close()

# 0.9241

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import tensorflow as tf

# tensorflow2下使用tensorflow1的方法
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

# Gradient descent variations
# SGD on MNIST # stochastic gradient descent (SGD)

# create a session
sess = tf.Session()
# initialize weights
sess.run(tf.global_variables_initializer())

test_loss = []  # placeholder for loss value per iteration

for _ in range(10000):
    # SGD -> batch size = 1
    batch_xs, batch_ys = mnist.train.next_batch(1)
    # update weights
    sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})
    # calculate loss funtion on test samples
    loss = sess.run(
        cross_entropy, feed_dict={x: mnist.test.images, y: mnist.test.labels}
    )
    # save it
    test_loss.append(loss)

plt.plot(np.arange(0, 10000, 1), test_loss)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Regularization")

# plot a sample
X, Y = get_dataset(50)

x_ = np.arange(-1, 1, 0.01)

plt.scatter(X, Y, color="C1")
plt.plot(x_, np.sin(np.pi * x_), "C0--")
show()

print("------------------------------")  # 30個

# Lets fit data to polynomial of order 20

N = 20  # polynomial order

# add powers of x
X_train = [[x**i for i in range(1, N)] for x in X]

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(X_train, Y)
show()

# And plot prediction together with training data

X_test = np.linspace(-1, 1, 100)
Y_test = reg.predict([[x**i for i in range(1, N)] for x in X_test])

plt.ylim([-1.5, 1.5])

plt.scatter(X, Y, color="C1")
plt.plot(X_test, Y_test, "C0")
show()

# It is clearly overfitted

print("------------------------------")  # 30個

# Lets do the same using Ridge regression

from sklearn.linear_model import Ridge

reg_l2 = Ridge(alpha=0.1)
reg_l2.fit(X_train, Y)

Y_test = reg_l2.predict([[x**i for i in range(1, N)] for x in X_test])

plt.ylim([-1.5, 1.5])

plt.scatter(X, Y, color="C1")
plt.plot(X_test, Y_test, "C0")
show()

print(reg.coef_)

print(reg_l2.coef_)

print("------------------------------")  # 30個

# Lets repeat the same for Lasso regression

from sklearn.linear_model import Lasso

reg_l1 = Lasso(alpha=0.001)
reg_l1.fit(X_train, Y)

Y_test = reg_l1.predict([[x**i for i in range(1, N)] for x in X_test])

plt.ylim([-1.5, 1.5])

plt.scatter(X, Y, color="C1")
plt.plot(X_test, Y_test, "C0")
show()

print(reg_l1.coef_)

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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
