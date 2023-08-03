list = [1, 3, 4, 6, 8]
item = 8


def bin_s(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess >= item:
            high = mid - 1
        else:
            low = mid + 1


print(bin_s(list, item))
