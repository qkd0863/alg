import random

random.seed('class_04')
array = [random.randrange(100) for _ in range(30)]
l_arr = len(array)

words = [
    '2018180022', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody',

    'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy',

    'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity',
    'loft',

    'temporize', 'speedboat', 'agenda', 'delusion', 'class04', 'idolize', 'romance', 'overestimate', 'revive', 'smell',

    'modem', 'splat', 'snaky', 'drawn', 'smoke', 'darky', 'lotus', 'mufti', 'pithy', 'jewel', 'nexus',

    'fluff', 'piton', 'finis', 'drake', 'caulk', 'pussy', 'bless', 'weeds', 'realm', 'swoon', 'thorn',

    'plant', 'aorta', 'cupid', 'wafer', 'jewry', 'sinus', 'proud', 'grape', 'cable', 'carer', 'pearl',

    'piece', 'party', 'sleet', 'palmy', 'oiled', 'synod', 'trove', 'voice', 'chest', 'story', 'range',

    'scout', 'sewer', 'lowly', 'usher', 'seine', 'gulch', 'fever', 'frith', 'pylon', 'wager', 'banns',

    'merit', 'cheap', 'booby', 'truss', 'codex', 'sepia', 'totem', 'poult', 'dregs', 'giddy', 'umber',

    'mooch', 'smarm', 'loath', 'spoil', 'drink', 'wrick', 'awake', 'mural', 'glide', 'pinch', 'thine',

    'tawny', 'swede', 'shier', 'satan', 'triad', 'splay', 'tacit',

]
w_arr = len(words)


# array = list(map(lambda e: (-e,e), array))
# print(array)
# import heapq
# heapq.heapify(array)
# print(array)

def downheap(root, size):
    ch = root * 2 + 1
    if ch >= size: return
    # 정렬

    if ch + 1 < size and words[ch] < words[ch + 1]:
        ch = ch + 1

    if words[root] >= words[ch]: return  # 교환

    words[root], words[ch] = words[ch], words[root]
    downheap(ch, size)


for i in range(w_arr // 2 - 1, -1, -1):
    downheap(i, w_arr)
print('정렬 전:')
print(words)

heapSize = w_arr
for i in range(w_arr - 1, 0, -1):
    heapSize -= 1
    words[0], words[heapSize] = words[heapSize], words[0]
    downheap(0, heapSize)
print('정렬 후:')
print(words)
