y = 8
def z(x): return x * y


print(z(2))
a = ('34.9',)
print(type(a))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))
