month_mapping = {
    'January': '1',
    'February': '2',
    'March': '3',
    'April': '4',
    'May': '5',
    'June': '6',
    'July': '7',
    'August': '8',
    'September': '9',
    'October': '10',
    'November': '11',
    'December': '12'
}

while True:
    date_input = input("Date: ")

    if "/" in date_input and "-" not in date_input and "," not in date_input:
        if not any(char.isalpha() for char in date_input):
            date = date_input.split("/")
            month, day, year = date

    elif "-" in date_input and "/" not in date_input and "," not in date_input:
        if not any(char.isalpha() for char in date_input):
            date = date_input.split("-")
            month, day, year = date

    elif "," in date_input and "-" not in date_input and "/" not in date_input:
        date_first = date_input[:-8]
        month_letter = date_first.replace(" ", "")
        date_last = date_input[-8:]
        date_last = date_last.split(",")

        if month_letter in month_mapping:
            month = month_mapping[month_letter]
            day = date_last[0].replace(" ", "")
            year = date_last[1].replace(" ", "")

            if int(day) <= 31 and int(month) <= 12 and len(year) == 4 and len(month) <= 2 and len(day) <= 2:
                break


print(year, (month.zfill(2)), (day.zfill(2)), sep='-')
