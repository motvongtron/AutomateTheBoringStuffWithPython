def bubbleSortRecur(list, num):
  swapped = False
  if len(list) - num == 1:
    return
  for i in range(len(list) - (num + 1)):
    if list[i] > list[i + 1]:
        list[i], list[i + 1] = list[i + 1], list[i]
        swapped = True
  print('\n' + str(swapped) + ': ')
  if swapped:
    for element in list:
      print(str(element), end=' ')
    bubbleSortRecur(list, num + 1)
list = [3, 5, 254, 15, 23, 556, 123, 321, 1, 8, 19, 10]
bubbleSortRecur(list, 0)
print('Final: ', end='')
for element in list:
  print(str(element), end=' ')