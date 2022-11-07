#task-1

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
x = input("Enter any of these char for specific operation (+,-,*,/,%): ")

result = 0
if x == '+':
    result = num1 + num2
elif x == '-':
    result = num1 - num2
elif x == '*':
    result = num1 * num2
elif x == '/':
    result = num1 / num2
elif x == '%':
    result = num1 % num2
else:
    print("Input character is not recognized!")

print(num1, x , num2, "=", result)


y = input("Enter any of these char for specific operation ('hex','oct','bin','dec'): ")

if y == 'hex':
    print(result, 'in hex =', hex(result))
elif y == 'oct':
    print(result, 'in oct =', oct(result))
elif y == 'bin':
    print(result, 'in bin =', bin(result))
elif y == 'dec':
    print(result, 'in dec =', result)
else:
    print("Input character is not recognized!")