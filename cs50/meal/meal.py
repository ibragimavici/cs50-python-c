def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")

    elif 12 <= time <= 13:
        print("lunch time")

    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    time = time.split(":")
    minute = int(time[1])/60
    hour = int(time[0])
    time = float(hour + minute)
    return time


if __name__ == "__main__":
    main()
