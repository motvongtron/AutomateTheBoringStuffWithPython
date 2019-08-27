def binarySearch(list, key):
    left = 0
    right = len(list)
    while (left <= right):
        mid = (right + left) // 2
        if key == list[mid]:
            return True
        elif key < list[mid]:
            right = mid - 1
        elif key > list[mid]:
            left = mid + 1
    return False
list = [10, 14, 19, 27, 33, 35, 42, 49]
print(binarySearch(list, 49))




