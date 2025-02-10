string = input()
vowels =""
consonant = ""
num = ""
for i in string:
    if ord(i) in range(65,91) or ord(i) in range(97,122):
        if i in ('a','e','i','o','u','A','E','I','O','U'):
             vowels += i
        else:
            consonant += i
    else:
        num += i
print(f"Number of vowels:{len(vowels)}")
print(f"Number of consonant:{len(consonant)}")
print(f"Number of digits:{len(num)}")
