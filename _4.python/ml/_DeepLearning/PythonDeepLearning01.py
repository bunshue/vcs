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

from sklearn import datasets

from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料


def show():
    plt.show()
    pass


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
