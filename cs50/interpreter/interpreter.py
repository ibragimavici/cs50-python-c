xyzfirst = (input("Expression? "))
xyzsplitted = xyzfirst.split()
x = int(xyzsplitted[0])
y = xyzsplitted[1]
z = int(xyzsplitted[2])

if y == "*" :
    print(float(x * z))
elif y == "/" :
    print(float(x / z))
elif y == "+" :
    print(float(x + z))
elif y == "-" :
    print(float(x - z))
else:
    print("wrong input")
