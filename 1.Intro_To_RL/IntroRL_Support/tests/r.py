test = {
    "name": "rewards",
    "points": 3,
    "suites": [ 
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> import pickle
                    >>> with open("IntroRL_Support/pickle/r_1.pkl", "rb") as f:
                    ...     data = pickle.load(f)
                    >>> grid_world = GridEnv(gamma=0.9, noise=0.2, living_reward=-0.04)
                    >>> r = generate_state_action_reward_LUT(grid_world, data["value"])
                    >>> np.allclose(r, data["rewards"])
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "success_message": "Good Job",
                    "failure_message": "Wrong implementation of generate_state_action_reward_LUT",
                },
                {
                    "code": r"""
                    >>> import pickle
                    >>> with open("IntroRL_Support/pickle/r_2.pkl", "rb") as f:
                    ...     data = pickle.load(f)
                    >>> grid_world = GridEnv(gamma=0.9, noise=0.2, living_reward=-0.04)
                    >>> r = generate_state_action_reward_LUT(grid_world, data["value"])
                    >>> np.allclose(r, data["rewards"])
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "success_message": "Good Job",
                    "failure_message": "Wrong implementation of generate_state_action_reward_LUT",
                },
                {
                    "code": r"""
                    >>> import pickle
                    >>> with open("IntroRL_Support/pickle/r_3.pkl", "rb") as f:
                    ...     data = pickle.load(f)
                    >>> grid_world = GridEnv(gamma=0.9, noise=0.2, living_reward=-0.04)
                    >>> r = generate_state_action_reward_LUT(grid_world, data["value"])
                    >>> np.allclose(r, data["rewards"])
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "success_message": "Good Job",
                    "failure_message": "Wrong implementation of generate_state_action_reward_LUT",
                }
            ],
            "scored": False,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}