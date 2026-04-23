import sys

number_of_kids = int(input(""))


if number_of_kids > 50 or number_of_kids < 2:
    sys.exit()

weights = input("")
weights = (weights.split(" "))
newlist = []
for i in weights:
    i = int(i)
    if i > 100 or i < 1:
        sys.exit()
    newlist.append(i)
dif = max(newlist) - min(newlist)

if len(newlist) != number_of_kids:
    sys.exit()
 

print(dif)