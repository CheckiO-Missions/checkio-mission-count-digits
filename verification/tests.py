"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ["hi"],
            "answer": 0
        },
        {
            "input": ["who is 1st here"],
            "answer": 1
        },
        {
            "input": ["my numbers is 2"],
            "answer": 1
        },
        {
            "input": ["This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"],
            "answer": 8
        },
        {
            "input": ["5 plus 6 is"],
            "answer": 2
        },
        {
            "input": [""],
            "answer": 0
        }
    ],
    "Extra": [
        {
            "input": ["It is the natural number following 4 and preceding 6  and is a prime number"],
            "answer": 2
        }
    ]
}