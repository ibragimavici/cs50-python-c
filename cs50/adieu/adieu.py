#name at a time
names = []

try:
    while True:
        int = input("name: ")
        names.append(int)
        # Process the user input here
except EOFError:
    print("")
    print("Adieu, adieu, to ", end="")
    namecount = 0
    for name in names:
        if len(names) == 1:
            print(names[namecount])

        elif len(names) == 2:
            if namecount == (len(names) - 1):
                print("and", names[namecount])

            else:
                print(names[namecount], " ", end="", sep="")
                namecount = namecount + 1


        else:
            if namecount == (len(names) - 1):
                print("and", names[namecount])

            else:
                print(names[namecount], ", ", end="", sep="")
                namecount = namecount + 1

