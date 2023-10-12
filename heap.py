import random

random.seed('class_04')
array = [random.randrange(100) for _ in range(30)]
l_arr = len(array)
print(array)


# array = list(map(lambda e: (-e,e), array))
# print(array)
# import heapq
# heapq.heapify(array)
# print(array)

def downheap(root, size):
    ch = root * 2 + 1
    if ch >= size: return
    # 정렬

    if ch + 1 < size and array[ch] < array[ch + 1]:
        ch = ch + 1

    if array[root] >= array[ch]: return  # 교환

    array[root], array[ch] = array[ch], array[root]
    downheap(ch, size)


for i in range(l_arr // 2 - 1, -1, -1):
    downheap(i, l_arr)
print(array)

heapSize = l_arr
for i in range(l_arr - 1, 0, -1):
    heapSize -= 1
    array[0], array[heapSize] = array[heapSize], array[0]
    downheap(0, heapSize)

print(array)
