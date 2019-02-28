def linearSort(list):
  for i in range(len(list[0:-1])):
    for j in range(len(list[i + 1:])):
      if list[i] > list[j + i + 1]:
        list[i], list[j + i + 1] = list[j + i + 1], list[i]

list = [3, 5, 254, 15, 23, 556, 123, 321, 1, 8, 19, 10]
linearSort(list)
for element in list:
  print(str(element), end=' ')