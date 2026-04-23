letters = list(input(""))
count = 0
current = 1
biggest = 1


while len(letters) - 1 > count:
    if letters[count] == letters[count+1]:
        current +=1
    else:
        current = 1

    if current > biggest:
        biggest = current
    
    count +=1
print(biggest)