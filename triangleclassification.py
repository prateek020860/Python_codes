a,b,c = map(int,input("Enter the side of triangle:").split(","))
if a!=b and b!=c and a!=c:
    print("scalen Triangle.")
elif a==b and a==c and b==c:
    print("Equilateral Triangle.")
elif a==b or b==c or a==c:
    print("Isoceles Trinagle")