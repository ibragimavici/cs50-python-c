input = str(input("Greeting: "))
input = input.casefold().strip()



if input[:5] == "hello":
    print("$0")
elif input[0] == "h":
    print("$20")
else:
    print("$100")

