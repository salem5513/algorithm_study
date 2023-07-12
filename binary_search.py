list = [1, 2, 5, 7, 9, 12, 33]  # лист среди которого ищем
item = 5  # искомое значение


def binary_search(list, item):  # бинарный поиск
    low = 0                     #устанавливаем границы
    high = len(list) - 1
    counter = 0

    ##Когда low становится больше high, это означает, что
    # интервал для поиска сужается до пустого множества и искомый элемент не найден

    while low <= high:          #циклом пока не дошли до значения или не встретились
        mid = (low+high) // 2   #берем среднюю позицию
        print('+1 спроба')
        guess = list[mid]      #берем элемент под ней
        if guess == item:      #проверяем
            return mid
        if guess > item:
            high = mid-1       #если нет то сужаем круг поиска
        else:
            low = mid+1        #если нет то сужаем круг поиска
    return None

print(binary_search(list,item))

