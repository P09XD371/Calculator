def menu():
    print("ГЛАВНОЕ МЕНЮ")
    print("1) Инструкция")
    print("2) Сложение")
    print("3) Умножение")
    print("4) Деление")
    print("5) Возведение в квадрат")
    print("6) Выход")
    print("7) Вывод привет")
    print("Введите число")

def calc():
    while True:
        menu()
        choice = input()
        if choice == "1":
            print("ИНСТУРКЦИЯ К ПРОГРАММЕ")
            print("1 открыть эту инструкцию")
            print("2 сложение двух чисел")
            print("3 умножение двух чисел")
            print("4 деление одного числа на другое")
            print("5 возведение числа в квадрат")
            print("6 завершение работы программы")
            print("7) Вывод привет")
            print("__________________________________________")
            input()

        elif choice == "2":
            print("СЛОЖЕНИЕ")
            try:
                print("Введите первое число:")
                a = float(input())
                print("Введите второе число:")
                b = float(input())
                c = a + b
                print(f"Результат = {c}")
                print("__________________________________________")
            except ValueError:
                print("Введите корректные значения")

        elif choice == "3":
            print("УМНОЖЕНИЕ")
            try:
                print("Введите первое число:")
                a = float(input())
                print("Введите второе число:")
                b = float(input())
                c = a * b
                print(f"Результат = {c}")
                print("__________________________________________")
            except ValueError:
                print("Введите корректные значения")

        elif choice == "4":
            print("ДЕЛЕНИЕ")
            try:
                print("Введите первое число:")
                a = float(input())
                print("Введите второе число:")
                b = float(input())
                c = a / b
                print(f"Результат = {c}")
                print("__________________________________________")
            except ValueError:
                print("Введите корректные значения")
            except Exception as e:
                print(e)


        elif choice == "5":
            print("ВОЗВЕДЕНИЕ В КВАДРАТ")
            try:
                print("Введите число:")
                a = float(input())
                c = a * a
                print(f"Результат = {c}")
                print("__________________________________________")
            except ValueError:
                print("Введите корректные значения")
        elif choice == "6":
            break
        elif choice == "7":
            print("Привет")
        else:
            print ("Выберете от 1 до 7")

if __name__ == "__main__":
    calc()
