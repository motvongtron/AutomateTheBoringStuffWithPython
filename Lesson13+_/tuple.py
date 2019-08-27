def inc(a, b, c):
    return a+1, b+2, c+3
a, b, c = 1, 2, 3
a, b, c = inc(a, b, c)
print(a)
print(b)
print(c)