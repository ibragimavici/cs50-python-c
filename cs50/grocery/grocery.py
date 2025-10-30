#keep asking for values - create values - update values - and print the amount
shopping_list = {}


while True:
    try:
        item = (input("")).upper()

        if item in shopping_list:
            value = value + 1
            shopping_list[item] = value

        else:
            value = 1
            shopping_list[item] = value

    except EOFError:

        for x, value in sorted(shopping_list.items()):
            print(value, x)
        exit(0)

