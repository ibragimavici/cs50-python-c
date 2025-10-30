due = 50

while due > 0:
    print("Amount Due: ", end='')
    print(due)
    insertedcoin = int(input(("Insert coin: ")))

    if insertedcoin == 50 or insertedcoin == 25 or insertedcoin == 10 or insertedcoin == 5 or insertedcoin == 0:
        due = (due - insertedcoin)
        insertedcoin = 0


if due <= 0:
    due = abs(due)
    print("Change Owed: ", end="")
    print(due)

else:
    insertedcoin = int(input("Amount Due: 50\n"))


