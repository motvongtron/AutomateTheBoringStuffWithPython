def doIt(list, left, right, key):
    if left > right:
        return False
    else:
        mid = (right + left) // 2
        if list[mid] == key:
            return True
        elif list[mid] < key:
            return doIt(list, mid + 1, right, key)
        elif list[mid] > key:
            return doIt(list, left, mid - 1, key)
list = [10, 14, 19, 27, 33, 35, 42, 49]
print(doIt(list, 0, len(list) - 1, 49))