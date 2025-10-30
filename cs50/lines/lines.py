import sys

def main():

    if argvlencheck() and argvcheck(sys.argv[1]) == True:
        print("anan.com")

    else:
        print("bum")
        sys.exit(0)















def argvlencheck():
    if len(sys.argv) == 2:
        return True
    else:
        return False


def argvcheck(argv):
    if str(argv)[-3:] == ".py":
        try:
            with open(argv, "r") as file:
                return True
        except:
            return False

    else:
        return False






main()

