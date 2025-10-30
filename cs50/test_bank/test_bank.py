from bank import value


def main():
    test_value()

def test_value():
    assert value("H") == 20
    assert value("      Hello") == 0
    assert value("   kjfnd") == 100
    assert value("Hi") == 20
    assert value("mhello") == 100





if __name__ == "__main__":
    main()
