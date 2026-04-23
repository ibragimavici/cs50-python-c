time= input("").split(" ")
time_1 = time[0].split(":")
time_2 = time[1].split(":")




h1 = int(time_1[0])
m1 = int(time_1[1])
s1 = int(time_1[2])

h2 = int(time_2[0])
m2 = int(time_2[1])
s2 = int(time_2[2])








def hours_between (h1, m1, s1, h2, m2, s2):

    if len(str(s1)) == 1:
        cfs1 = "".join(["0", str(s1)])
    else:
        cfs1 = str(s1)


    if len(str(m1)) == 1:
        cfm1 = "".join(["0", str(m1)])
    else:
        cfm1 = str(m1)
                

    if len(str(h1)) == 1:
        cfh1 = "".join(["0", str(h1)])
    else:
        cfh1 = str(h1)

    if cfh1[:1] == cfs1[1:] and cfh1[1:] == cfs1[:1] and cfm1[:1] == cfm1[1:]:
        how_many = 1
    else:
        how_many = 0
    

    second_count = 0
    second_while_counting = s1
    minute_while_counting = m1
    hour_while_counting = h1

    while not (second_while_counting, minute_while_counting, hour_while_counting) == (s2, m2, h2):
        

        second_while_counting = second_while_counting + 1
        if second_while_counting > 59:
            second_while_counting = 0
            minute_while_counting = minute_while_counting + 1
            if minute_while_counting > 59:
                minute_while_counting = 0
                hour_while_counting = hour_while_counting + 1
                if hour_while_counting > 23:
                    hour_while_counting = 0




        if len(str(second_while_counting)) == 1:
            cs1 = "".join(["0", str(second_while_counting)])
        else:
            cs1 = str(second_while_counting)


        if len(str(minute_while_counting)) == 1:
            cm1 = "".join(["0", str(minute_while_counting)])
        else:
            cm1 = str(minute_while_counting)
                

        if len(str(hour_while_counting)) == 1:
            ch1 = "".join(["0", str(hour_while_counting)])
        else:
            ch1 = str(hour_while_counting)
            
        #print(":".join([ch1, cm1, cs1]))

        if ch1[:1] == cs1[1:] and ch1[1:] == cs1[:1] and cm1[:1] == cm1[1:]:
            how_many = how_many + 1

    return(how_many)

print(hours_between(h1, m1, s1, h2, m2, s2))