#inp = input("").split()

how_many = int(input(""))

inp = [how_many]


while how_many > 0:
    current = input("").split()
    for i in current:
        inp.append(i)

    how_many = how_many - 1

def posy(number):
    if number <= 0:
        return (number) * (-1)
    else:
        return number
    
def bigger(k, l, m, n):
    if k>=l and k>=m and k>=n:
        return k
    elif l>=k and l>=m and l>=n:
        return l
    elif m>=k and m>=l and m>=n:
        return m
    else:
        return n
    
    

k = 0
m = ((len(inp))-1)/4


while m>0:
    a = int(inp[k+1])
    b = int(inp[k+2])

    x = int(inp[k+3])
    y = int(inp[k+4])
    
    k = k+4
    m = m-1

    b_y = posy(b - (y+1))
    zero_x = posy(0 - x)

    a_x = posy(a - (x+1))
    zero_y = posy(0 - y)


    final_result = bigger(  (b_y * a), (a_x * b), (b * zero_x), (a * zero_y)    )
    print(final_result)

