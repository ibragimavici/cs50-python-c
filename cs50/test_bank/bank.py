def main():
    giris = input("Greeting: ")
    valued_input = value(giris)
    print("$", valued_input, sep="")



def value(giris):

    greeting = str(giris)
    greeting = greeting.casefold().strip()


    if greeting[:5] == "hello":
        return 0

    elif greeting[0] == "h":
        return 20

    else:
        return 100



if __name__ == "__main__":
    main()
