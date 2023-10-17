import random

random.seed('class_04')



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
print("정렬전 - merge")
print(words)
print("정렬후 - merge")

def merge(start, mid, end):  # mid is in left, and is inclusive
    merged = []
    l, r = start, mid + 1
    while l <= mid and r <= end:
        if words[l] <= words[r]:
            merged.append(words[l])
            l += 1
        else:
            merged.append(words[r])
            r += 1

    if l <= mid:
        merged += words[l:mid + 1]
        words[start:end + 1] = merged
    else:
        # merged += array[r:mid + 1]
        words[start:r] = merged

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


mergeSort(0, w_arr - 1)
print(words)
