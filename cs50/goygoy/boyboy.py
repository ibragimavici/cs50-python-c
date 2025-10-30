
for _ in range(5):

    name = input("name: ")

    with open("text.txt", "a") as file:
        file.write(f"{name}\n")
