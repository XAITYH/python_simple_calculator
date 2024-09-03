num1 = input("Введите первое число\n")

num2 = input("Введите второе число\n")

action = input("Введите действие из приведенных: *, **, /, +, -, %\n")


match action:
    case "*":
        print(float(num1) * float(num2))
    case "**":
        print(float(num1) ** float(num2))
    case "/":
        print(float(num1) / float(num2))
    case "+":
        print(float(num1) + float(num2))
    case "-":
        print(float(num1) - float(num2))
    case "%":
        print(float(num1) % float(num2))
    case _:
        print("Something is wrong")