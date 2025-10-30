names = []

with open("text.txt") as file:
    for _ in file:
        names.append(_.rstrip())

    for _ in sorted(names):
        print(f"hello, {_}")
