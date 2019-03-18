def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e

result = divide(1,0)
print(result)