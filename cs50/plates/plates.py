
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(plate):

    word_count = len(plate)
    if word_count == 2:
        if plate.isalpha() == True:
            return True
        else:
            return False
    elif word_count == 3:
        if plate[0:2].isalpha() == True:
            if plate[2].isalpha():
                return True
            elif plate[2].isdigit():
                if plate[2] == "0":
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False
    elif word_count == 4:
        if plate[0:2].isalpha() == True:
            if plate[2].isalpha():
                if plate[3].isalpha():
                    return True
                elif plate[3].isdigit():
                    if plate[3] == "0":
                        return False
                    else:
                        return True
                else:
                    return False
            elif plate[2].isdigit():
                if plate[2] == "0":
                    return False
                else:
                    if plate[3].isdigit():
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False
    elif word_count == 5:
        if plate[0:2].isalpha() == True:
             if plate[2].isalpha():
                if plate[3].isalpha():
                    if plate[4].isalpha():
                        return True
                    elif plate[4].isdigit():
                        if plate[4] == "0":
                            return False
                        else:
                            return True
                    else:
                        return False
                elif plate[3].isdigit():
                        if plate[3] == "0":
                            return False
                        elif plate[3:5].isdigit():
                            return True
                        else:
                            return False
             elif plate[2].isdigit():
                if plate[2] == "0":
                    return False
                elif plate[2:6].isdigit():
                    return True
                else:
                    return False

    elif word_count == 6:
        if plate[0:2].isalpha() == True:
             if plate[2].isalpha():
                if plate[3].isalpha():
                    if plate[4].isalpha():
                        if plate[5].isalpha():
                            return True
                        elif plate[5].isdigit():
                            if plate[5] == "0":
                                return False
                            else:
                                return True
                        else:
                            return False
                    elif plate[4].isdigit():
                        if plate[4] == "0":
                            return False
                        elif plate[4:6].isdigit():
                            return True
                        else:
                            return False
                elif plate[3].isdigit():
                    if plate[3] == "0":
                        return False
                    elif plate[3:6].isdigit():
                        return True
                    else:
                        return False
             elif plate[2].isdigit():
                if plate[2] == "0":
                    return False
                elif plate[2:6].isdigit():
                    return True
                else:
                    return False
        else:
            return False

    else:
        return False

main()
