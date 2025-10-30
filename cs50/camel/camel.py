c = str(input("your input: "))
for n in c:
    if n.isupper() == True:
        n = n.casefold()
        print("_" + n, end='')

    else:
        print(n, end='')

print("")
