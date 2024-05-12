from lib.solutions.HLO.hello_solution import hello


def test_hello():
    expected = "Hello, World!"

    actual = hello("francis")

    assert actual == expected
