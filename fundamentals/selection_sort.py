def find_smallest(li):
    smallest = li[0]
    index_of_smallest = 0
    for i in range(1, len(li)):
        if li[i] < smallest:
            smallest = li[i]
            index_of_smallest = i
    return index_of_smallest

def selection_sort(li):
    sorted_list = []
    copied_list = list(li)
    for i in range(len(li)):
        index_of_smallest = find_smallest(copied_list)
        sorted_list.append(copied_list.pop(index_of_smallest))
    return sorted_list

my_li = [4, 2, 10, 3, 1]
print(f'Index of smallest {find_smallest(my_li)}')     # Index of smallest 4
print(selection_sort(my_li))                           # [1, 2, 3, 4, 10]
