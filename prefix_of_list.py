l = list(map(str,input().split()))
prefix = str(input("Enter the prefix:"))
count = 0
for i in l:
    if i.startswith(prefix)==True:
        count += 1
print(count)