from plates import is_valid


def main():
    test_is_valid()

def test_is_valid():
    assert is_valid("HELLO") == True
    assert is_valid("GOODBYE") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("50") == False
    assert is_valid("*21*2") == False
    assert is_valid("ADAM31") == True
    assert is_valid("AD31AM") == False
    assert is_valid("KLMNO") == True
    assert is_valid("KLMN*") == False





if __name__ == "__main__":
    main()
