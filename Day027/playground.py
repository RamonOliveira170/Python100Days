def sum(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

sum(2, 4, 6, 8)

def calculate(number, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    number += kwargs["add"]
    print(number)
    number *= kwargs["multiply"]
    print(number)

calculate(5, add=3, multiply=9)
