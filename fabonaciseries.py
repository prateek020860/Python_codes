num = int(input("Enter the value:"))
a,b = 0,1
l = []
for _ in range(num):
    l.append(a)
    a,b = b,a+b
print(l)