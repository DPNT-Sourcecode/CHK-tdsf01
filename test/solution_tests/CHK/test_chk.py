from lib.solutions.CHK.checkout_solution import checkout


def test_checkout_success():
    bucket = "AAABBCD"

    actual = checkout(bucket)
    expected = 210

    assert actual == expected
