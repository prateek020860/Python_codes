a,b,operator = input().split()
a,b = float(a),float(b)
if operator == '+':
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator == '/':
    if b == 0:
        print('Error: Division by zero')
    else:
        print(a/b)