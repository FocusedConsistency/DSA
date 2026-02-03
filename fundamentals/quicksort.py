def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less_than_pivot = [i for i in array[1:] if i <= pivot]
        greater_than_pivot = [i for i in array[1:] if i > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
print(quicksort([30, 20, 26, 4, 19, 50]))  # [4, 19, 20, 26, 30, 50]
