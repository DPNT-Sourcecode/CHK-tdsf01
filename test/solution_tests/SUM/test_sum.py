from lib.solutions.HLO.hello_solution import hello


def test_hello():
    name = "francis"
    expected = f"hello {name}"

    actual = hello(name)

    assert actual == expected


