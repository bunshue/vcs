"""
tic_tac_toe_test


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


# min_max.py

from tic_tac_toe import available_moves, apply_move, has_winner


def _score_line(line):
    minus_count = line.count(-1)
    plus_count = line.count(1)
    if minus_count + plus_count < 3:
        if minus_count == 2:
            return -1
        elif plus_count == 2:
            return 1
    return 0


def evaluate(board_state):
    """Get a rough score for how good we think this board position is for the plus_player. Does this based on number of
    2 in row lines we have.

    Args:
        board_state (3x3 tuple of int): The board state we are evaluating

    Returns:
        int: evaluated score for the position for the plus player, posative is good for the plus player, negative good
            for the minus player
    """
    score = 0
    for x in range(3):
        score += _score_line(board_state[x])
    for y in range(3):
        score += _score_line([i[y] for i in board_state])

    # diagonals
    score += _score_line([board_state[i][i] for i in range(3)])
    score += _score_line([board_state[2 - i][i] for i in range(3)])

    return score


def min_max(board_state, side, max_depth, evaluation_func=evaluate):
    """Runs the min_max_algorithm on a given board_sate for a given side, to a given depth in order to find the best
    move

    Args:
        board_state (3x3 tuple of int): The board state we are evaluating
        side (int): either +1 or -1
        max_depth (int): how deep we want our tree to go before we use the evaluate method to determine how good the
        position is.
        evaluation_func (board_state -> int): Function used to evaluate the position for the plus player

    Returns:
        (best_score(int), best_score_move((int, int)): the move found to be best and what it's min-max score was
    """
    best_score = None
    best_score_move = None

    moves = list(available_moves(board_state))
    if not moves:
        # this is a draw
        return 0, None

    for move in moves:
        new_board_state = apply_move(board_state, move, side)
        winner = has_winner(new_board_state)
        if winner != 0:
            return winner * 10000, move
        else:
            if max_depth <= 1:
                score = evaluation_func(new_board_state)
            else:
                score, _ = min_max(new_board_state, -side, max_depth - 1)
            if side > 0:
                if best_score is None or score > best_score:
                    best_score = score
                    best_score_move = move
            else:
                if best_score is None or score < best_score:
                    best_score = score
                    best_score_move = move
    return best_score, best_score_move


def min_max_alpha_beta(
    board_state,
    side,
    max_depth,
    evaluation_func=evaluate,
    alpha=-sys.float_info.max,
    beta=sys.float_info.max,
):
    """Runs the min_max_algorithm on a given board_sate for a given side, to a given depth in order to find the best
    move

    Args:
        board_state (3x3 tuple of int): The board state we are evaluating
        side (int): either +1 or -1
        max_depth (int): how deep we want our tree to go before we use the evaluate method to determine how good the
        position is.
        evaluation_func (board_state -> int): Function used to evaluate the position for the plus player
        alpha (float): Used when this is called recursively, normally ignore
        beta (float): Used when this is called recursively, normally ignore

    Returns:
        (best_score(int), best_score_move((int, int)): the move found to be best and what it's min-max score was
    """
    best_score_move = None
    moves = list(available_moves(board_state))
    if not moves:
        return 0, None

    for move in moves:
        new_board_state = apply_move(board_state, move, side)
        winner = has_winner(new_board_state)
        if winner != 0:
            return winner * 10000, move
        else:
            if max_depth <= 1:
                score = evaluation_func(new_board_state)
            else:
                score, _ = min_max_alpha_beta(
                    new_board_state, -side, max_depth - 1, alpha, beta
                )

        if side > 0:
            if score > alpha:
                alpha = score
                best_score_move = move
        else:
            if score < beta:
                beta = score
                best_score_move = move
        if alpha >= beta:
            break

    return alpha if side > 0 else beta, best_score_move


def min_max_player(board_state, side):
    return min_max(board_state, side, 5)[1]


print("------------------------------------------------------------")  # 60個

# monte_carlo.py

import collections
from tic_tac_toe import has_winner, available_moves, apply_move


def monte_carlo_sample(board_state, side):
    """Sample a single rollout from the current board_state and side. Moves are made to the current board_state until we
     reach a terminal state then the result and the first move made to get there is returned.

    Args:
        board_state (3x3 tuple of int): state of the board
        side (int): side currently to play. +1 for the plus player, -1 for the minus player

    Returns:
        (result(int), move(int,int)): The result from this rollout, +1 for a win for the plus player -1 for a win for
            the minus player, 0 for a draw
    """
    result = has_winner(board_state)
    if result != 0:
        return result, None
    moves = list(available_moves(board_state))
    if not moves:
        return 0, None

    # select a random move
    move = random.choice(moves)
    result, next_move = monte_carlo_sample(apply_move(board_state, move, side), -side)
    return result, move


def monte_carlo_tree_search(board_state, side, number_of_samples):
    """Evaluate the best from the current board_state for the given side using monte carlo sampling.

    Args:
        board_state (3x3 tuple of int): state of the board
        side (int): side currently to play. +1 for the plus player, -1 for the minus player
        number_of_samples (int): number of samples rollouts to run from the current position, the higher the number the
            better the estimation of the position

    Returns:
        (result(int), move(int,int)): The average result for the best move from this position and what that move was.
    """
    move_wins = collections.defaultdict(int)
    move_samples = collections.defaultdict(int)
    for _ in range(number_of_samples):
        result, move = monte_carlo_sample(board_state, side)
        # store the result and a count of the number of times we have tried this move
        if result == side:
            move_wins[move] += 1
        move_samples[move] += 1

    # get the move with the best average result
    move = max(move_wins, key=lambda x: move_wins.get(x) / move_samples[move])

    return move_wins[move] / move_samples[move], move


def _upper_confidence_bounds(payout, samples_for_this_machine, log_total_samples):
    return payout / samples_for_this_machine + math.sqrt(
        (2 * log_total_samples) / samples_for_this_machine
    )


def monte_carlo_tree_search_uct(board_state, side, number_of_samples):
    """Evaluate the best from the current board_state for the given side using monte carlo sampling with upper
    confidence bounds for trees.

    Args:
        board_state (3x3 tuple of int): state of the board
        side (int): side currently to play. +1 for the plus player, -1 for the minus player
        number_of_samples (int): number of samples rollouts to run from the current position, the higher the number the
            better the estimation of the position

    Returns:
        (result(int), move(int,int)): The average result for the best move from this position and what that move was.
    """
    state_results = collections.defaultdict(float)
    state_samples = collections.defaultdict(float)

    for _ in range(number_of_samples):
        current_side = side
        current_board_state = board_state
        first_unvisited_node = True
        rollout_path = []
        result = 0

        while result == 0:
            move_states = {
                move: apply_move(current_board_state, move, current_side)
                for move in available_moves(current_board_state)
            }

            if not move_states:
                result = 0
                break

            if all((state in state_samples) for _, state in move_states):
                log_total_samples = math.log(
                    sum(state_samples[s] for s in move_states.values())
                )
                move, state = max(
                    move_states,
                    key=lambda _, s: _upper_confidence_bounds(
                        state_results[s], state_samples[s], log_total_samples
                    ),
                )
            else:
                move = random.choice(list(move_states.keys()))

            current_board_state = move_states[move]

            if first_unvisited_node:
                rollout_path.append((current_board_state, current_side))
                if current_board_state not in state_samples:
                    first_unvisited_node = False

            current_side = -current_side

            result = has_winner(current_board_state)

        for path_board_state, path_side in rollout_path:
            state_samples[path_board_state] += 1.0
            result *= path_side
            # normalize results to be between 0 and 1 before this it between -1 and 1
            result /= 2.0
            result += 0.5
            state_results[path_board_state] += result

    move_states = {
        move: apply_move(board_state, move, side)
        for move in available_moves(board_state)
    }

    move = max(
        move_states,
        key=lambda x: state_results[move_states[x]] / state_samples[move_states[x]],
    )

    return state_results[move_states[move]] / state_samples[move_states[move]], move


if __name__ == "__main__":
    board_state = ((1, 0, -1), (1, 0, 0), (0, -1, 0))

    print(monte_carlo_tree_search_uct(board_state, -1, 10000))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# policy_gradient.py

import collections
import tensorflow as tf
from tic_tac_toe import play_game, random_player

import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()  # tensorflow2下使用tensorflow1的方法

HIDDEN_NODES = (100, 100, 100)  # number of hidden layer neurons
INPUT_NODES = 3 * 3  # board size
BATCH_SIZE = 100  # every how many games to do a parameter update?
LEARN_RATE = 1e-4
OUTPUT_NODES = INPUT_NODES
PRINT_RESULTS_EVERY_X = 1000  # every how many games to print the results

input_placeholder = tf.placeholder("float", shape=(None, INPUT_NODES))
reward_placeholder = tf.placeholder("float", shape=(None,))
actual_move_placeholder = tf.placeholder("float", shape=(None, OUTPUT_NODES))

hidden_weights_1 = tf.Variable(
    tf.truncated_normal(
        (INPUT_NODES, HIDDEN_NODES[0]), stddev=1.0 / np.sqrt(INPUT_NODES)
    )
)
hidden_weights_2 = tf.Variable(
    tf.truncated_normal(
        (HIDDEN_NODES[0], HIDDEN_NODES[1]), stddev=1.0 / np.sqrt(HIDDEN_NODES[0])
    )
)
hidden_weights_3 = tf.Variable(
    tf.truncated_normal(
        (HIDDEN_NODES[1], HIDDEN_NODES[2]), stddev=1.0 / np.sqrt(HIDDEN_NODES[1])
    )
)
output_weights = tf.Variable(
    tf.truncated_normal(
        (HIDDEN_NODES[-1], OUTPUT_NODES), stddev=1.0 / np.sqrt(OUTPUT_NODES)
    )
)

hidden_layer_1 = tf.nn.relu(
    tf.matmul(input_placeholder, hidden_weights_1)
    + tf.Variable(tf.constant(0.01, shape=(HIDDEN_NODES[0],)))
)
hidden_layer_2 = tf.nn.relu(
    tf.matmul(hidden_layer_1, hidden_weights_2)
    + tf.Variable(tf.constant(0.01, shape=(HIDDEN_NODES[1],)))
)
hidden_layer_3 = tf.nn.relu(
    tf.matmul(hidden_layer_2, hidden_weights_3)
    + tf.Variable(tf.constant(0.01, shape=(HIDDEN_NODES[2],)))
)
output_layer = tf.nn.softmax(
    tf.matmul(hidden_layer_3, output_weights)
    + tf.Variable(tf.constant(0.01, shape=(OUTPUT_NODES,)))
)

policy_gradient = tf.reduce_sum(
    tf.reshape(reward_placeholder, (-1, 1)) * actual_move_placeholder * output_layer
)
train_step = tf.train.RMSPropOptimizer(LEARN_RATE).minimize(-policy_gradient)

sess = tf.Session()
sess.run(tf.initialize_all_variables())

board_states, actual_moves, rewards = [], [], []
episode_number = 1
results = collections.deque()


def make_move(board_state, side):
    board_state_flat = np.ravel(board_state)
    board_states.append(board_state_flat)
    probability_of_actions = sess.run(
        output_layer, feed_dict={input_placeholder: [board_state_flat]}
    )[0]

    try:
        move = np.random.multinomial(1, probability_of_actions)
    except ValueError:
        # sometimes because of rounding errors we end up with probability_of_actions summing to greater than 1.
        # so need to reduce slightly to be a valid value
        move = np.random.multinomial(
            1, probability_of_actions / (sum(probability_of_actions) + 1e-7)
        )

    actual_moves.append(move)

    move_index = move.argmax()
    return move_index / 3, move_index % 3


while True:
    reward = play_game(make_move, random_player)

    results.append(reward)
    if len(results) > PRINT_RESULTS_EVERY_X:
        results.popleft()

    last_game_length = len(board_states) - len(rewards)

    # we scale here so winning quickly is better winning slowly and loosing slowly better than loosing quick
    reward /= float(last_game_length)

    rewards += [reward] * last_game_length

    episode_number += 1

    if episode_number > 10000:
        break

    if episode_number % BATCH_SIZE == 0:
        normalized_rewards = rewards - np.mean(rewards)
        normalized_rewards /= np.std(normalized_rewards)

        sess.run(
            train_step,
            feed_dict={
                input_placeholder: board_states,
                reward_placeholder: normalized_rewards,
                actual_move_placeholder: actual_moves,
            },
        )

        # clear batches
        del board_states[:]
        del actual_moves[:]
        del rewards[:]

    if episode_number % PRINT_RESULTS_EVERY_X == 0:
        print(
            "episode: %s win_rate: %s"
            % (episode_number, 0.5 + sum(results) / (PRINT_RESULTS_EVERY_X * 2.0))
        )

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# tic_tac_toe_x.py

"""
Full code for running a game of tic-tac-toe on a board of any size with a specified number in a row for the win. This is
similar to tic_tac_toe.py but all relevent moves are paramiterized by board_size arg that sets how big the board is and
winning_length which determines how many in a row are needed to win. Defaults are 5 and 4. This allows you to play games
in a more complex environment than standard tic-tac-toe.

Two players take turns making moves on squares of the board, the first to get winning_length in a row, including
diagonals, wins. If there are no valid moves left to make the game ends a draw.

The main method to use here is play_game which simulates a game to the end using the function args it takes to determine
where each player plays.
The board is represented by a board_size x board_size tuple of ints. A 0 means no player has played in a space, 1 means
player one has played there, -1 means the seconds player has played there. The apply_move method can be used to return a
copy of a given state with a given move applied. This can be useful for doing min-max or monte carlo sampling.
"""

import itertools


def _new_board(board_size):
    """Return a emprty tic-tac-toe board we can use for simulating a game.

    Args:
        board_size (int): The size of one side of the board, a board_size * board_size board is created

    Returns:
        board_size x board_size tuple of ints
    """
    return tuple(tuple(0 for _ in range(board_size)) for _ in range(board_size))


def apply_move(board_state, move, side):
    """Returns a copy of the given board_state with the desired move applied.

    Args:
        board_state (2d tuple of int): The given board_state we want to apply the move to.
        move (int, int): The position we want to make the move in.
        side (int): The side we are making this move for, 1 for the first player, -1 for the second player.

    Returns:
        (2d tuple of int): A copy of the board_state with the given move applied for the given side.
    """
    move_x, move_y = move

    def get_tuples():
        for x in range(len(board_state)):
            if move_x == x:
                temp = list(board_state[x])
                temp[move_y] = side
                yield tuple(temp)
            else:
                yield board_state[x]

    return tuple(get_tuples())


def available_moves(board_state):
    """Get all legal moves for the current board_state. For Tic-tac-toe that is all positions that do not currently have
    pieces played.

    Args:
        board_state: The board_state we want to check for valid moves.

    Returns:
        Generator of (int, int): All the valid moves that can be played in this position.
    """
    for x, y in itertools.product(range(len(board_state)), range(len(board_state[0]))):
        if board_state[x][y] == 0:
            yield (x, y)


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


def has_winner(board_state, winning_length):
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
    for d in range(diagonals_start, diagonals_end + 1):
        winner = _has_winning_line(
            (
                board_state[i][i + d]
                for i in range(max(-d, 0), min(board_width, board_height - d))
            ),
            winning_length,
        )
        if winner != 0:
            return winner
    for d in range(diagonals_start, diagonals_end + 1):
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
    plus_player_func, minus_player_func, board_size=5, winning_length=4, log=False
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
        board_size (int): The size of a single side of the board. Game is played on a board_size*board_size sized board
        winning_length (int): The number of pieces in a row needed to win a game.
        log (bool): If True progress is logged to console, defaults to False

    Returns:
        int: 1 if the plus_player_func won, -1 if the minus_player_func won and 0 for a draw
    """
    board_state = _new_board(board_size)
    player_turn = 1

    while True:
        _available_moves = list(available_moves(board_state))
        if len(_available_moves) == 0:
            # draw
            if log:
                print("no moves left, game ended a draw")
            return 0.0
        if player_turn > 0:
            move = plus_player_func(board_state, 1)
        else:
            move = minus_player_func(board_state, -1)

        if move not in _available_moves:
            # if a player makes an invalid move the other player wins
            if log:
                print("illegal move ", move)
            return -player_turn

        board_state = apply_move(board_state, move, player_turn)
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
    play_game(random_player, random_player, log=True, board_size=10, winning_length=4)

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
