num1 = int(input("Enter your First number: "))
num2 = int(input("Enter your Second number: "))
operator = input("Enter your Operator: ")

if operator =="+":
    print(num1 + num2)
elif operator == "-":
    print(num1-num2)
elif operator =="*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
elif operator == "**":
    print(num1**num2)
else:
    print("Invalid Operators...")
