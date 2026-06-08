   #  Let's  Built a calculator

first = input("Enter first number  : ")
operator = input("Enter operator (+,-,*,/,%)  : ")
second = input("Enter second number  : ")

first = int(first)  # convert into number form
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)

else:
    print("invaled operation")