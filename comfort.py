import sys

number_of_seats = int(input(""))
comforts = input("")
comforts = comforts.split()
inp = []
inp.append(number_of_seats)
for i in comforts:
    inp.append(i)



tries = number_of_seats - 2



toplamlar = []
k = 1
coin_counter = 0
while tries > 0:
    toplam = int(inp[k]) + int(inp[k+1]) + int(inp[k+2])
    
    if toplam < 0:
        inp[k+2] = int(inp[k+2]) - toplam
        coin_counter = coin_counter - toplam
        toplam = 0


    tries = tries - 1
    k = k+1



print(coin_counter)