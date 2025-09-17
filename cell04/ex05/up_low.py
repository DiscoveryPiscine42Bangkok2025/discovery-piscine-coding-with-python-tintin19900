user = input("")

for i in user:
    if i.islower():
        print(i.upper(), end="")
    else:
        print(i.lower(), end="")