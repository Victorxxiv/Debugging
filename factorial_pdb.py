# factorial.py

import pdb

def factorial(n):
    pdb.set_trace()  # This will start the debugger
    if n == 0:
        return 1
    return n + factorial(n - 1)