l = list(map(int,input("Enter the list of numbers:").split()))
target = int(input("Enter the target number:"))
for i ,val in enumerate(l):
    if target - val in l:
        print([i,l.index(target-val)])
        break
