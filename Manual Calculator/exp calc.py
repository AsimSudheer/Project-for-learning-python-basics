fruits = ['peaches','apple']
operand1 = input("Enter the first number: ")
operand2 = input("enter the second number: ")
sign = input("Enter the sign: ")

try:
    operand1=float(operand1)
    operand2=float(operand2)
except:
    print("Enter a valid opernad")


if sign == "+":
    ans = float(operand1)+float(operand2)
elif sign == "-":
    ans = float(operand1)-float(operand2)
elif sign == "/":
    if operand2 != 0:
        ans = float(operand1)/float(operand2)
    else:
        print("Enter a number other than 0")
elif sign == "*":
    ans = float(operand1)*float(operand2)
else:
    print("ERROR")

print(f"The result is:{ans}")
for i in fruits:
    print(i)