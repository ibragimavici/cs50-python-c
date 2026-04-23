import sys
how_many = int(input(""))
cardlist = []

while how_many > 0:
    how_many = how_many - 1
    cardlist.append(input(""))


length = len(cardlist)
sıra = 1




while length > sıra:
    sıra = sıra + 1

    if length > 2:
        if cardlist[sıra] == cardlist[sıra-1]:
            mirrored = 1
            if cardlist[sıra] == cardlist[sıra+1]:
                print("INVALID")
                sys.exit()
    mirrored = 0

    if length == 2:
        if cardlist[0] == cardlist[1]:
            mirrored = 1


    
    if cardlist[sıra] == cardlist[sıra+2] and mirrored == 0:
        print("INVALID")
        sys.exit()
    
    if cardlist[sıra] == cardlist[sıra+3] and mirrored == 0:
        print("INVALID")
        sys.exit()

print("VALID")

    


