# noinspection PyUnusedLocal
# skus = unicode string


PRICES = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
SPECIAL_OFFER = {"A": [(3, 130), (5, 200)], "B": [(2, 45)], "E": [(2, "B")]}


def checkout(skus: str) -> int:
    total_price = 0
    bucket = {}
    skus = sorted(skus)
    for item in skus:
        if item not in PRICES:
            return -1
        num = bucket.get(item, 0) + 1
        bucket[item] = num

    for item, count in bucket.items():
        if item in SPECIAL_OFFER:
            for offer in SPECIAL_OFFER[item]:
                special_quantity, special_price = offer
                if isinstance(special_price, str):
                    # Handle special case for item E
                    b_count = bucket.get(special_price, 0)
                    free_b_count = min(count // special_quantity, b_count)
                    count -= free_b_count * special_quantity
                    bucket[special_price] -= free_b_count

        total_price += count * PRICES[item]

    return total_price


