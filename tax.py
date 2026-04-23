import sys

number_of_seats = int(input(""))
comforts = input("")
comforts = comforts.split()
inp = []
inp.append(number_of_seats)
for i in comforts:
    inp.append(i)

if number_of_seats < 3:
    sys.exit()
if number_of_seats != (len(inp) - 1):
    sys.exit()


tries = number_of_seats - 2



toplamlar = []
k = 1
while tries > 0:
    toplam = int(inp[k]) + int(inp[k+1]) + int(inp[k+2])
    k = k+1
    toplamlar.append(toplam)

    tries = tries - 1



coins = (min(toplamlar)) * -1

if min(toplamlar) >= 0:
    print("0")
else:
    print(coins)

