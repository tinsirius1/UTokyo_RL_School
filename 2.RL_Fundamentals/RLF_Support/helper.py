import numpy as np
from collections import defaultdict
from copy import deepcopy
from matplotlib import pyplot as plt


def encode_policy(grid_env, policy_matrix=None):
    """
     Convert deterministic policy matrix into stochastic policy representation

     :param grid_env: MDP environment
     :param policy_matrix: Deterministic policy matrix (one action per state)

     :return: (dict of dict) Dictionary of dictionaries where each element corresponds to the
             probability of selection an action a at a given state s
     """

    height, width = grid_env.grid.shape

    if policy_matrix is None:

        policy_matrix = np.array([[3,      3,  3,  np.NaN],
                                  [0, np.NaN,  0,  np.NaN],
                                  [0,      2,  0,       2]])

    result_policy = defaultdict(lambda: defaultdict(float))

    for i in range(height):
        for j in range(width):
            s = grid_env.grid[i, j]
            if np.isnan(s) or grid_env.is_terminal_state(i, j):
                continue

            for a, _ in grid_env.ACTIONS.items():
                result_policy[int(s)][int(a)] = 0.0

            if not np.isnan(policy_matrix[i, j]):
                result_policy[int(s)][int(policy_matrix[i, j])] = 1.0

    return result_policy

def define_random_policy(grid_env):
    """
    Define random deterministic policy for given environment

    :param grid_env: MDP environment
    :return: (matrix) Deterministic policy matrix
    """
    np.random.seed(grid_env.seed()[0])

    policy_matrix = np.array([np.random.choice(grid_env.get_actions(), 4).tolist(),
                              np.random.choice(grid_env.get_actions(), 4).tolist(),
                              np.random.choice(grid_env.get_actions(), 4).tolist()])

    for (x, y) in grid_env.terminal_states:
        policy_matrix[x, y] = -1

    for (x, y) in grid_env.obstacles:
        policy_matrix[x, y] = -1

    return policy_matrix
