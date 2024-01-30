test = {
    "name": "state_transitions",
    "points": 2,
    "suites": [ 
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> import pickle
                    >>> with open("IntroRL_Support/pickle/st.pkl", "rb") as f:
                    ...     data = pickle.load(f)
                    >>> grid_world = GridEnv(gamma=0.9, noise=0.2, living_reward=-0.04)
                    >>> st = generate_transition_LUT(grid_world, data["value"])
                    >>> np.allclose(st, data["st"])
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                    "success_message": "Good Job",
                    "failure_message": "Wrong implementation of generate_transition_LUT",
                }
            ],
            "scored": False,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}