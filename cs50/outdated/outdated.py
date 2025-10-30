month_mapping ={
                'January' : '1',
                'February' : '2',
                'March' : '3',
                'April' : '4',
                'May' : '5',
                'June' : '6',
                'July' : '7',
                'August' : '8',
                'September' : '9',
                'October' : '10',
                'November' : '11',
                'December' : '12'
                }




run_program = 1
correctness = 1


while run_program == 1:

    date_input = input("Date: ").strip()

    if "/" in date_input and "-" not in date_input and "," not in date_input:
        if any(char.isalpha() for char in date_input):
            correctness = 0
        else:
            date = date_input.split("/")

            month = date[0]
            day = date[1]
            year = date[2]


    elif "-" in date_input and "/" not in date_input and "," not in date_input:
        if any(char.isalpha() for char in date_input):
            correctness = 0
        else:
            date = date_input.split("-")

            month = date[0]
            day = date[1]
            year = date[2]


    elif "," in date_input and "-" not in date_input and "/" not in date_input:
        date_first = date_input[:-8]
        month_letter = date_first.replace(" ", "")

        date_last = date_input[-8:]
        date_last = date_last.split(",")

        if month_letter in month_mapping:
            month = month_mapping[month_letter]
        else:
            correctness = 0

        day = date_last[0].replace(" ","")
        year = date_last[1].replace(" ","")




    else:
        correctness = 0

    if correctness == 1:
        if int(day) > 31 or int(month) > 12 or len(year) > 4 or len(month) > 2 or len(day) > 2:
            correctness = 0


        elif correctness == 1:
            run_program = 0
            if len(month) == 2 and len(day) == 1:
                print(year, "-", month, "-", "0", day, sep="")

            if len(month) == 1 and len(day) == 2:
                print(year, "-", "0", month, "-", day, sep="")

            if len(month) == 2 and len(day) == 2:
                print(year, "-", month, "-", day, sep="")

            if len(month) == 1 and len(day) == 1:
                print(year, "-", "0", month, "-", "0", day, sep="")









