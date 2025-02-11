l = eval(input())
missing_val = l[0]
for i in l:
    if i != missing_val:
        print(missing_val)
        break
    missing_val += 1
else:
    print("Not any missing value is found:")