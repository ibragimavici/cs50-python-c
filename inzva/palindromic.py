import sys

time= input("").split(" ")
time_1 = time[0].split(":")
time_2 = time[1].split(":")


how_many = 0

time_1[0] = int(time_1[0])
time_1[1] = int(time_1[1])
time_1[2] = int(time_1[2])

time_2[0] = int(time_2[0])
time_2[1] = int(time_2[1])
time_2[2] = int(time_2[2])


while True:
    if (int(time_1[0]) == int(time_2[0]) and int(time_1[1]) == int(time_2[1]) and int(time_1[2]) == int(time_2[2])) == True:
        print(how_many)
        sys.exit()

    while time_1[0] < 23:

        while time_1[1] < 59:

            while time_1[2] < 59:
                
                time_1[2] = time_1[2] + 1
                

                
                if len(str(time_1[2])) == 2:
                    second_str = str(time_1[2])
                else:
                    second_str = "".join(["0", str(time_1[2])])


                if len(str(time_1[1])) == 2:
                    minute_str = str(time_1[1])
                else:
                    minute_str = "".join(["0", str(time_1[1])])

                if len(str(time_1[0])) == 2:
                    hour_str = str(time_1[0])
                else:
                    hour_str = "".join(["0", str(time_1[0])])

                if (str(time_1[0]))[:0] == (str(time_1[2]))[0:] and (str(time_1[0]))[0:] == (str(time_1[2]))[:0] and (str(time_1[1]))[:0] == (str(time_1[1]))[0:]:
                    how_many = how_many + 1

                print(time_1)

                    
            if time_1[2] == 59:
                time_1[2] = -1
                time_1[1] = time_1[1] + 1


        if time_1[1] == 59:
            time_1[1] = 0
            time_1[0] = time_1[0] + 1

    if time_1[0] == 23:
        time_1[0] = 0

