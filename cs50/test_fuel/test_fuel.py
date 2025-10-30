from fuel import convert
from fuel import gauge



def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/10") == 10

    try:
        convert("1/0")
    except ZeroDivisionError:
        pass
    else:
        assert False

    try:
        convert("50/1")
    except ValueError:
        pass
    else:
        assert False

    try:
        convert("5/1")
    except ValueError:
        pass
    else:
        assert False



def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(35) == "35%"
    assert gauge(80) == "80%"
    assert gauge(41) == "41%"













