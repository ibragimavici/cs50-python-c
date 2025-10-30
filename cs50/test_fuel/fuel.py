def main():
    while True:
        try:
            fraction = str(input("fraction: "))
            fracted = convert(fraction)

        except ValueError:
            print("value is not correct")
        except ZeroDivisionError:
            print("Cant divide by zero")
        else:
            break

    final = gauge(fracted)
    print(final)


def convert(fraction):
            x_and_y = fraction.split("/")
            x = int(x_and_y[0])
            y = int(x_and_y[1])
            fraction = round((x/y)*100)
            if x > y:
                raise ValueError

            return fraction


def gauge(percentage):
    if percentage == 100 or percentage == 99:
        percent = ("F")
        return percent
    elif percentage == 0 or percentage == 1:
        percent = ("E")
        return percent
    else:
        percent = (f"{percentage}%")
        return percent



if __name__ == "__main__":
    main()


