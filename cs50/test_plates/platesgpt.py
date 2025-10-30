def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Check the length of the plate
    if not 2 <= len(plate) <= 6:
        return False

    # The first two characters must be alphabetic
    if not plate[:2].isalpha():
        return False

    # Check the rest of the characters
    for i, char in enumerate(plate[2:], start=2):
        if not (char.isalpha() or char.isdigit()):
            return False
        if char.isdigit() and char == '0' and (i == 2 or not plate[i-1].isdigit()):
            return False

    return True



main()
