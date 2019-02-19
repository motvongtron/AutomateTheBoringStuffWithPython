def collatz(number):
  if (number % 2) == 0:
    print(str(number) + ' // 2')
    return number // 2
  else:
    print('3 * ' + str(number) + ' + 1')
    return 3 * number + 1
print('Enter number:')
try:
  number = int(input())
except ValueError:
  print('Error: Noninteger input.')
  exit()
while number != 1:
  number = collatz(number)
  print(str(number))
