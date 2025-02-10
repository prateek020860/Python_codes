c=int(input("Enter the cost price:"))
s=int(input("Enter the selling price"))
if s > c:
    profit=s-c
    pro_per=((profit/c)*100)
    print("Profit")
    per=(round(pro_per,2))
    print("{}%".format(per))
if c>s:
    loss=c-s
    loss_per=(loss/c)*100
    lot=(round(loss_per,2))
    print("Loss")
    print("{}%".format(lot))