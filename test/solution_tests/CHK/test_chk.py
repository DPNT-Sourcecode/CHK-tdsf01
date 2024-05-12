import pytest

from lib.solutions.CHK.checkout_solution import checkout


@pytest.mark.parametrize("bucket, expected", [
    # ("AAABBCDE", 250),
    # ("AAAAAAAA", 330),
    # ("AAAAAAAAA", 380),
    # ("AAAAAAAAAA", 400),
    ("EEEB", 120),
    # ("EEEEBB", 160),
    # ("EE", 80),
    # ("AAABBCDEE", 260),
    # ("AAABBCDEE", 260),
    # ("AAAAABBCDEE", 330),
    # ("aBCD", -1),
    # ("ABBCD", 130),
    # ("ABCDE", 155)
])
def test_checkout_success(bucket, expected):

    actual = checkout(bucket)

    assert actual == expected


