def factorial(number):
    if number == 1:
        print('Base case reached!')
        return 1
    else:
        print('Finding ', number, ' * ', number - 1, '!', sep='')
        result = number * factorial(number - 1)
        print(number, ' * ', number -1, '! = ', result, sep='')
        return result

print('5! is', factorial(5))