from random import choice


def main():
    global level
    level = get_level()
    a, b = generate_integer()
    c = a + b

    eee_count = 0
    yey_count = 0
    score = 10
    q_count = 0

    while True:
        try:
            if q_count == 10:
                print("Score:", score)
                break
            else:
                print(a, " + ", b, " = ", sep="", end="")
                userguess = int(input(""))

                if userguess == (c):
                    a, b = generate_integer()
                    c = a + b
                    eee_count = 0
                    yey_count = yey_count + 1
                    q_count = q_count + 1



                elif eee_count < 3:
                    print("EEE")
                    eee_count = eee_count + 1

                    if eee_count == 3:
                        print(a, " + ", b, " = ", c, sep="")
                        score = score - 1
                        q_count = q_count + 1
                        a, b = generate_integer()
                        c = a + b
                        eee_count = 0

        except ValueError:
            print("ValueError", end="")







def get_level():
    levelinp = input("Level: ")
    while True:
        if levelinp == "1" or levelinp == "2" or levelinp == "3":
            level = int(levelinp)
            return level
        else:
            levelinp = input("Level: ")



def generate_integer():

    if level == 1:
            numbers = range(10)
            a = choice(numbers)
            b = choice(numbers)
    elif level == 2:
            numbers = range(10, 99)
            a = choice(numbers)
            b = choice(numbers)
    elif level == 3:
            numbers = range(100, 999)
            a = choice(numbers)
            b = choice(numbers)

    a = int(a)
    b = int(b)
    return a, b





if __name__ == "__main__":
    main()
