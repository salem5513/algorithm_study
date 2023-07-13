list = [1, 2, 3, 4, 5, 7, 9, 12, 14, 15]
item = 3


def bin_search(item, list):
    min = 0
    max = len(list) - 1
    while min <= max:
        print('Try n')
        midd = (min + max) // 2
        guess = list[midd]
        if guess == item:
            return midd
        if guess > item:
            max = midd + 1
        else:
            min = midd - 1
    return None


print(bin_search(item,list))
