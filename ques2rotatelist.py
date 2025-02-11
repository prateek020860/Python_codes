l,k = eval(input())
l.reverse()
p,s = l[0:k],l[k:]
p.reverse(),s.reverse()
print(p+s)