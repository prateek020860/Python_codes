string,sub_string = map(eval,input("Enter string and sub_string:").split())
count = 0
start = 0
while True:
    start = string.find(sub_string,start)
    if start == -1:
        break
    count += 1
    start += 1
print(count)