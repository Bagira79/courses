def fibonacci(number):
    list_fibonacci = []
    if number == 0:
        return list_fibonacci
    elif number == 1:
        list_fibonacci.append(0)
    else:
        next_number = 1
        previous_number = 0
        for i in range(number + 1):
            if i == 0:
                list_fibonacci.append(0)
            elif i == 1:
                list_fibonacci.append(1)
            else:
                previous_number, next_number = next_number, previous_number + next_number
                if next_number < number:
                    list_fibonacci.append(next_number)

    return list_fibonacci


def fibonacci_dict(num):
    dict_fibonacci = {j: fibonacci(j) for j in range(num + 1)}
    return dict_fibonacci


digit = int(input('Введите натуральное число: '))
dict_fib = fibonacci_dict(digit)
print(dict_fib)
