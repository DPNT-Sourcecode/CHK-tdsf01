import pytest

from lib.solutions.CHK.checkout_solution import checkout


@pytest.mark.parametrize("bucket, expected", [
    ("AAABBCD", 210),
    ("aBCD", -1),
    ("ABBCD", 130),
    ("ABCD", 115)
])
def test_checkout_success(bucket, expected):

    actual = checkout(bucket)

    assert actual == expected


