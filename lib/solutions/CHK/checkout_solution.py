# noinspection PyUnusedLocal
# skus = unicode string


PRICES = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
SPECIAL_OFFER = {"A": [(3, 130), (5, 200)], "B": [(2, 45)], "E": [(2, "B")]}


def checkout(skus: str) -> int:
    total = 0
    bucket = {}
    skus = sorted(skus)
    for item in skus:
        if item not in PRICES:
            return -1
        num = bucket.get(item, 0) + 1
        bucket[item] = num

    for item, cnt in bucket.items():
        if item in SPECIAL_OFFER:
            for offer in SPECIAL_OFFER[item]:
                special_quantity, special_price = offer
                while cnt >= special_quantity:
                    print(f"\nspecial_price: {special_price}")
                    total += special_price
                    cnt -= special_quantity
        total += cnt * PRICES[item]

    return total




