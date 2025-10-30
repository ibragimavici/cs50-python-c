print("What is the answer to the Great Question of Life, the Universe and Everything?")
answer = str(input("Your answer: "))
answer = answer.casefold().replace(" ", "").replace("-", "")

if answer == "fortytwo" or answer == "42":
    print("yes")
else:
    print("no")
