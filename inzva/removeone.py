import math

count = int(input(""))
numbers = input("").split(" ")


newnumberlist = []
toplam = 0
for i in numbers:
    i = int(i)
    toplam = toplam + i
    newnumberlist.append(i)

closeness_list = []

for i in numbers:
    closeness_list.append(math.fabs(int(toplam) - int(i)))
which = closeness_list.index(min(closeness_list))
closest = newnumberlist[which]
newnumberlist.remove(closest)

print(int(math.fabs(sum(newnumberlist))))