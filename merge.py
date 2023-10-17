import random

random.seed('class_04')

array = [random.randrange(100) for _ in range(30)]
l_arr = len(array)
print(array, l_arr)

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


def merge(start, mid, end):  # mid is in left, and is inclusive
    merged = []
    l, r = start, mid + 1
    while l <= mid and r <= end:
        if array[l] <= array[r]:
            merged.append(array[l])
            l += 1
        else:
            merged.append(array[r])
            r += 1

    if l <= mid:
        merged += array[l:mid + 1]
        array[start:end + 1] = merged
    else:
        # merged += array[r:mid + 1]
        array[start:r] = merged

    # while l <= mid:
    #     merged.append(array[l])
    #     l += 1
    # while r <= end:
    #     merged.append(array[r])
    #     r += 1


def mergeSort(start, end):  # end:inclusive
    # size = end - start + 1
    # if size <= 1: return
    if start >= end: return

    mid = (start + end) // 2  # mid is in left
    mergeSort(start, mid)
    mergeSort(mid + 1, end)
    merge(start, mid, end)


mergeSort(0, l_arr - 1)
print(array)
