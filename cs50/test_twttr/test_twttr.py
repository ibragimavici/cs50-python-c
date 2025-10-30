from twttr import shorten


def main():
    test_vowel_rmv()

def test_vowel_rmv():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("klmnprsAEIOU") == "klmnprs"
    assert shorten("KLMNPRSAEIOU") == "KLMNPRS"
    assert shorten("!#$%&'()*+,-./:;<=>?@[\]^_`{|}~") == "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    assert shorten("1234567890") == "1234567890"



if __name__ == "__main__":
    main()
