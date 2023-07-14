list = [1, 2, 4, 5, 7, 8, 9]
item = 4

def bin_search(list, item):
    min = 0
    max = len(list) - 1
    while min <= max:
        mid = (min+max)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            min = guess + 1
        else:
            max = guess - 1
    return None


print(bin_search(list, item))
