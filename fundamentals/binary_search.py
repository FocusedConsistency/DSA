def binary_search(collection, item):
    lower = 0
    higher = len(some_list) - 1
    search_count = 0
    while lower <= higher:
        search_count += 1
        mid = (lower + higher) // 2
        if collection[mid] == item:
            return mid, search_count
        if collection[mid] > item:
            higher = mid - 1
        elif collection[mid] < item:
            lower = mid + 1
    return None

some_list = [1, 3, 5, 8, 14, 20, 32, 40, 89]
index, count = binary_search(some_list, 89)
print(f'Found at index: {index}, Search depth: {count}')
