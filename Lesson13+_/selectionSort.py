def selectionSort(list):
  for i in range(len(list[0:-1])):
    indexOfMin = i
    updated = False
    for j in range(len(list[i + 1:])):
      if list[indexOfMin] > list[j + i + 1]:
        indexOfMin = j + i + 1
        updated = True
    if updated:
      list[indexOfMin], list[i] = list[i], list[indexOfMin]
    print('\nStep ' + str(i + 1) + ': ')
    for element in list:
      print(str(element), end=' ')
list = [3, 5, 254, 15, 23, 556, 123, 321, 1, 8, 19, 10]
selectionSort(list)