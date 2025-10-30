menu_mapping = {
                    'baja taco' : '4.25',
                    'burrito' : '7.50',
                    'bowl' : '8.50',
                    'nachos' : '11.00',
                    'quesadilla' : '8.50',
                    'super burrito' : '8.50',
                    'super quesadilla' : '9.50',
                    'taco' : '3.00',
                    'tortilla salad' : '8.00'
                }
total_price = 0

while True:
    while True:
        try:
            item = input("Item: ")
            if not item:
                raise EOFError

            item = item.casefold()
            price = float(menu_mapping[item])
        except KeyError:
            pass
        except EOFError:
            exit(0)
        else:
            break


    total_price = total_price + price
    if item == "super burrito":
        print("Total: $", total_price, sep='')
    else:
        print("Total: $", total_price, "0", sep='')



