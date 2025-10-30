while True:
    try:
        fraction = str(input("fraction: "))
        x_and_y = fraction.split("/")
        x = int(x_and_y[0])
        y = int(x_and_y[1])
        percentage = round((x/y)*100)
        if x > y:
            raise ValueError

    except ValueError:
        print("value is not correct")
    except ZeroDivisionError:
        print("Cant divide by zero")
    else:
        break

if percentage == 100 or percentage == 99:
    print("F")
elif percentage == 0 or percentage == 1:
    print("E")
else:
    print(percentage, "%", sep='')
