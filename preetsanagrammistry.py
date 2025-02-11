string,substring = map(eval,input("Enter the string and substring:").split())
count = 0
if len(string) == len(substring):
    for i in substring:
        if i in string:
            count += 1
    if len(string) == count:
        print("True")
    else:
        print("False")
else:
    print("False")     
