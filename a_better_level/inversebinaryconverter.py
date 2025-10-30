def bin2dec(binary):

    sum = 0
    listOfNumber = []
    currentPosition = len(binary)

    for i in range(len(binary)):
        currentPosition = currentPosition - 1
        singlebinary = int(binary[i])
        if singlebinary != 1 and singlebinary != 0:
            print("invalid binary")
            exit()
        listOfNumber.append((2 ** currentPosition) * singlebinary)

    for i in listOfNumber:
        sum = sum + i

    print(sum)

bin2dec("100000101010")

#do a loop that sums numbers from start to finish
