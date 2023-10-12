import random

random.seed('class_04')
array = [random.randrange(15) for _ in range(100)]
l_arr = len(array)
maxv = max(array)
print(array, maxv)
counts = [0 for _ in range(maxv + 1)]
print(counts, len(counts))
for v in array:
    counts[v] += 1
print(counts, len(counts))

for i in range(len(counts) - 1):
    counts[i + 1] += counts[i]
print(counts, len(counts))

# results = array[:]
results = [None] * l_arr
for i in range(l_arr - 1, -1, -1):
    v = array[i]
    counts[v] -= 1
    ri = counts[v]
    results[ri] = v
    print(results)
