year = int(input())
if year % 4 and year % 100!=0 or year % 400 ==0:
    print("Leap Year")
else:
    print("Not Leap Year")