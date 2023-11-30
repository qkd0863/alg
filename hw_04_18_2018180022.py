import random

random.seed('class_04')
BIN_SIZE = 25
nums = [ random.randint(2, 9) for _ in range(30) ]
print(nums)

#bin = [ 1, 2, 3 ]
#bins = [ bin ]

def bin_free(bin):
    return BIN_SIZE - sum(bin)

def bin_can_hold(bin, size):
    return bin_free(bin) >= size

def new_bin():
    nb = []
    bins.append(nb)
    return nb

def first_fit(size):
    for b in bins:
        if bin_can_hold(b,size):
            return b
    return new_bin()

def next_fit(size):
    if len(bins)>0 and bin_can_hold(bins[-1],size):
        return bins[-1]
    return new_bin()

def best_fit(size):
    smallest_bin = None
    smallest_size = BIN_SIZE

    return new_bin()

def worst_fit(size):
    largest_bin = None
    return new_bin()


for fit_func in [first_fit,next_fit,best_fit,worst_fit]:
    bins=[]
    for num in nums:
        bin=fit_func(num)
        bin.append(num)

    print(f'Function: <<{fit_func.__name__}>>')
    print(bins)
