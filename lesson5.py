try:
    a = 10
    b = int(input("Введіть число: "))
    print(a / b)
except ValueError:
    print("Ви ввели не число: " )
except ZeroDivisionError:
    print("На нуль ділити не можна: ")