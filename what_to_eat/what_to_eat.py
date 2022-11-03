import random

# print(random.randint(1, 14))
# print(random.sample(['a', 'b', 'c', 'd'], 1))
# print(random.choices(['a', 'b', 'c', 'd'], k=1))

a = list(range(1, 6))
print(a)
# weight = [0, 1, 2, 0, 0]
weight = [0, 1, 1, 1, 1]
# print(random.choices(a, k=2))  # output: "[9, 7]"
print(random.choices(a, cum_weights=weight, k=10))  # output: "[9, 7]"
