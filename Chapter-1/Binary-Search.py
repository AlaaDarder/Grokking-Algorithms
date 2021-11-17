def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = int((low + high/2))
        print(mid)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 5, 9, 10, 20,60]
print (binary_search(my_list, 20))  # => 4
print('Output',binary_search(my_list, 1))  # => None
