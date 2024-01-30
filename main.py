# trying to implement a fibonacci numbers using list and yield

def fib(number):
    a, b = 0, 1
    for i in range(number):
        yield a
        temp = a # not modify a until a + b (temp is a temporary variable)
        a = b
        b = temp + b

for x in fib(21):
    print(x)

# using list()

def fib2(number):
    f1, f2 = 0, 1
    result = []
    for i in range(number):
        result.append(f1)
        temp = f1
        f1 = f2
        f2 = temp + f2
    return result

print(fib2(21))

# note that with list() takes more time than with yield
# incrise the number of the fib and fib2 to see the difference
