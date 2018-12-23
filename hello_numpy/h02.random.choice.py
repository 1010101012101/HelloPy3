import numpy as np

print(np.random.choice(20, (3,2)))

print(np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0]))

print(np.random.choice(5, 3, replace=False))

print(np.random.choice(5, 3, replace=False))

print(np.random.choice(5, 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0]))

print(np.random.choice(5, 3, replace=True, p=[0.1, 0, 0.3, 0.6, 0]))

aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
print(np.random.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3]))