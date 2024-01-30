test = {
    "name": "policy",
    "points": 2,
    "suites": [ 
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> import pickle
                    >>> with open("IntroRL_Support/pickle/p.pkl", "rb") as f:
                    ...     data = pickle.load(f)
                    >>> results = []
                    >>> np.random.seed(42)
                    >>> for row in data["chances"]:
                    ...     result = policy(*row)
                    ...     results.append(result)
                    >>> np.allclose(results, data["p"])
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