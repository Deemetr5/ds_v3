import numpy as np

count_ls = []
for i in range(1, 100):
    tre = np.random.randint(1, 101)
    count_ls.append(tre)

print(max(count_ls))
print(min(count_ls))

print(np.random.randint(1, 10))