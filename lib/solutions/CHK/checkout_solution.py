

# noinspection PyUnusedLocal
# skus = unicode string

SPECIAL_A = {
    3: 130
}

SPECIAL_B = {
    2: 45
}

PRODUCTS = {
    "A": {"regular": 50, "special": {"cnt": 3, "price": 130}},
    "B": {"regular": 30, "special": {"cnt": 2, "price": 45}},
    "C": {"regular": 20},
    "D": {"regular": 15}
}


def checkout(skus: str) -> int:
    total = 0
    bucket = {}
    for item in skus:
        if item not in PRODUCTS:
            return -1
        num = bucket.get(item, 0) + 1
        bucket[item] = num

    for item, num in bucket.items():
        special = PRODUCTS.get(item, {}).get("special")
        if special:
            cnt = special["cnt"]
            price = special["price"]
            if num > cnt:
                discount_cnt = num // cnt
                item_price = (discount_cnt * price) + (num - discount_cnt)
                total += (discount_cnt * price)
