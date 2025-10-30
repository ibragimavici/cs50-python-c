def turnIntoBinary(listOfPowers):
    binarystr = ""
    for i in range (listOfPowers[0], -1, -1):
        if i in listOfPowers:
            binarystr = binarystr + "1"
        if not i in listOfPowers:
            binarystr = binarystr + "0"
    return binarystr



def sumList(List):
    sum = 0
    for i in List:
        sum = sum + i
    return sum


def dec2bin(Int):

    listOfPowers = []
    listOfPowersOfTwo = []
    currentInt = Int

    while not sumList(listOfPowersOfTwo) == Int:
        twoOverCounter = 0
        while currentInt >= (2 ** twoOverCounter):
            twoOverCounter = twoOverCounter + 1

        listOfPowersOfTwo.append(2 ** (twoOverCounter-1))
        listOfPowers.append(twoOverCounter-1)

        currentInt = currentInt - 2 ** (twoOverCounter-1)

    print(turnIntoBinary(listOfPowers))





dec2bin(6434)


# find the biggest power of 2 that is smaller than the number itself
