num1 = input("Write the first number\n")

num2 = input("Write the second number\n")

action = input("Write one of the actions: *, **, /, +, -, %\n")

if num1.isdigit() and num2.isdigit():
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
            print("Wrong action.")
else:
    print("You've made a typo or wrote a text instead of number.")