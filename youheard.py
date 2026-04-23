
import math
x_and_y = input("").split()
x = int(x_and_y[0])
y = int(x_and_y[1])
number = y-x+1
if number == 0 : 
    print(1)
else:
    n = math.ceil(math.log(number,2)) 
    print(n)

