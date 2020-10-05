def fib(number):
    if number == 1 or number == 2:
        print(f'Found fib({number}): returning 1!')
        return 1
    else:
        print(f'Finding fib({number}): fib({number - 1}) + fib({number - 2})')
        result = fib(number - 1) + fib(number - 2)
        print(f'Found fib({number}): {result}')
        return result
print('fib(5) is', fib(5))
# print('fib(10) is', fib(10))