l = eval(input())
remove_duplicate = list(set(l))
remove_duplicate.sort(reverse=True)
print(remove_duplicate[1])