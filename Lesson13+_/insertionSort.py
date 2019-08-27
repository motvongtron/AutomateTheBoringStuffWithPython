def insertionSort(list):
    for i in range(len(list)):
        valueToInsert = list[i]
        holePosition = i
        while holePosition > 0 and list[holePosition - 1] > valueToInsert:
            list[holePosition] = list[holePosition -1]
            holePosition = holePosition - 1
        list[holePosition] = valueToInsert
        print('\nStep ' + str(i + 1) + ': ')
        for element in list:
            print(str(element), end=' ')
list = [14, 33, 27, 10, 35, 19, 42, 44]
insertionSort(list)
