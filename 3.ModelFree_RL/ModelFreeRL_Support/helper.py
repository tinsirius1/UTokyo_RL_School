import numpy as np
from collections import defaultdict
from copy import deepcopy
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

def animate(frame_buffer):
    fig, ax = plt.subplots(1, 1, figsize=(9,3.25), dpi=90)
    img = ax.imshow(frame_buffer[0])
    plt.tight_layout()
    def update(frame):
        img.set_data(frame_buffer[frame])
        return img,
    anim = animation.FuncAnimation(fig, update, frames=len(frame_buffer), interval=1000/60, blit=True)
    plt.close(fig)
    return HTML(anim.to_jshtml())

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

        policy_matrix = np.array([[3,      3,  3,  -1],
                                  [0, np.NaN,  0,  -1],
                                  [0,      2,  0,   2]])

    result_policy = defaultdict(lambda: defaultdict(float))

    for i in range(height):
        for j in range(width):
            s = grid_env.grid[i, j]
            if np.isnan(s) or grid_env.is_terminal_state(i, j):
                continue

            for a, _ in grid_env.ACTIONS.items():
                result_policy[int(s)][int(a)] = 0.0

            if policy_matrix[i, j] >= 0 or not np.isnan(policy_matrix[i, j]):
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


def decode_policy(grid_env, policy=None):
    """
     Convert stochastic policy representation (dict of dict) to deterministic policy matrix

     :param grid_env: MDP environment
     :param policy: stochastic policy (probability of each action at each state)

     :return: (matrix) Deterministic policy matrix (one action per state)
     """

    height, width = grid_env.grid.shape
    policy_matrix = np.full((height, width), -1)

    for s, actions in policy.items():
        x, y = np.argwhere(grid_env.grid == s)[0]

        if not grid_env.is_terminal_state(x,y):
          action_keys = list(actions.keys())
          policy_matrix[x, y] = action_keys[np.argmax(list(actions.values()))]

    return policy_matrix
