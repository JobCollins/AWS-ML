import math
import numpy as numpy

test_scores = [88, 92, 74, 48, 73]
print(np.mean(test_scores))


curved_test_scores = [math.sqrt(score) * 10 for score in test_scores]
print(np.mean(curved_test_scores))


# even without comments one can understand what is going on 