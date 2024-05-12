from lib.solutions.HLO.hello_solution import hello


def test_hello():
    name = "francis"
    expected = f"Hello, {name}!"

    actual = hello("francis")

    assert actual == expected
