list = [1, 2, 3, 4, 5, 6, 7, 8, 12, 15]
item = 8


def search(list, item):
    min = 0
    max = len(list) - 1
    while min <= max:
        middle = (min + max) // 2
        guess = list[middle]
        if guess == item:
            return middle
        if guess < item:
            min = middle + 1
        else:
            max = middle - 1
    return None


print(search(list, item))
