num1 = int(input("what is your first number? "))
num2 = int(input("what is yor second number? "))
operation = input("what is your operation +,-,*,/)? ")
if operation =="+":
    print(num1+num2)
elif operation =="-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation =="/":
    print(num1/num2)
else:
    print("you did not enter a valied operation")
    