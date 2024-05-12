import pytest

from lib.solutions.CHK.checkout_solution import checkout


@pytest.mark.parametrize("bucket, expected", [
    ("AAABBCDE", 250),
    ("AAABBCDEE", 260),
    ("AAAAABBCDEE", 330),
    ("aBCD", -1),
    ("ABBCD", 130),
    ("ABCDE", 155)
])
def test_checkout_success(bucket, expected):

    actual = checkout(bucket)

    assert actual == expected


