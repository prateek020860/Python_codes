secret_code =list(map(int,input("Enter the sectet code:").split()))
code_converter = ""
for code in secret_code:
    if 1<= code <=26:
        code_converter += chr(code+64)
    elif 27<= code <=52:
        code_converter += chr(code+70)
print(code_converter)