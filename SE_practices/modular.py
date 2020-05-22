"""
In this case you are boostng test_scores because the test was too hard
and/or unfair. The code is modular.
"""

import math
import numpy as np

def flat_curve(arr, n):
    return [i + n for i in arr]

def square_root_curve(arr):
    return [math.sqrt(i) * 10 for i in arr]


test_scores = [88, 92, 74, 48, 73]
curved_5 = flat_curve(test_scores, 5)
curved_10 = flat_curve(test_scores, 10)
curved_sqrt = square_root_curve(test_scores)


for score_list in test_scores, curved_5, curved_10, curved_sqrt:
    print(np.mean(score_list))