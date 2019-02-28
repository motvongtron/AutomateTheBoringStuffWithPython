def bubbleSort(list):
  for i in range(len(list) - 1):
    swapped = False
    for j in range(len(list) - 1 - i):
      if list[j] > list[j + 1]:
        list[j], list[j + 1] = list[j + 1], list[j]
        swapped = True
    print('\nStep ' + str(i + 1) + ': ')
    for element in list:
      print(str(element), end=' ')
    if not swapped:
      break
list = [3, 5, 254, 15, 23, 556, 123, 321, 1, 8, 19, 10]
bubbleSort(list)