how_many = int(input(""))

inp = []

while how_many > 0:
    how_many = how_many - 1
    inp.append(input(""))



string = ""

for i in inp:
    string = string + i

number = int(string)
print(number*2)
