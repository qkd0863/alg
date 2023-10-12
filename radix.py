import random

random.seed('class_04')
array = [random.randrange(1000) for _ in range(10)]
l_arr = len(array)
maxv = max(array)
print(array, maxv)

div = 1
results = [None] * l_arr
while div <= maxv:
    counts = [0 for _ in range(10)]
    for v in array:
        digit = v // div % 10
        counts[digit] += 1

    for i in range(len(counts) - 1):
        counts[i + 1] += counts[i]

    # results = [None] * l_arr

    for i in range(l_arr - 1, -1, -1):
        v = array[i]
        digit = v // div % 10
        counts[digit] -= 1
        ri = counts[digit]
        results[ri] = v
    array = results[:]
    print(results, div)
    div *= 10

exit()
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
