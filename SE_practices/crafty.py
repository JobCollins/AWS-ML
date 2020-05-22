"""
In this case you are boostng test_scores because the test was too hard
and/or unfair. The code is not modular.
"""

s = [88, 92, 74, 48, 73]
print(sum(s)/len(s))

s1 = []
for x in s:
    s1.append(x + 5)

print(sum(s1)/len(s1))

s2 = []
for x in s:
    s2.append(x + 10)

print(sum(s2)/len(s2))

s3 = []
for x in s:
    s3.append(x ** 0.5 * 10)

print(sum(s3)/len(s3))


#the code is not clear to understand, and it's very repetitive - spaghetti code common in DS 