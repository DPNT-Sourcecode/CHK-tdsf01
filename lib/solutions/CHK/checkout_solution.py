# noinspection PyUnusedLocal
# skus = unicode string


PRODUCTS = {
    "A": {
        "regular": 50,
        "specials": [
            {
                "cnt": 3,
                "price": 130
            },
            {
                "cnt": 5,
                "price": 200
            }
        ]
    },
    "B": {
        "regular": 30,
        "specials": [
            {
                "cnt": 2,
                "price": 45
            }
        ]
    },
    "C": {
        "regular": 20
    },
    "D": {
        "regular": 15
    },
    "E": {
        "regular": 40,
        "specials": [
            {
                "cnt": 2,
                "related": "B",
                "price": 0
            }
        ]
    }
}


def checkout(skus: str) -> int:
    total = 0
    bucket = {}
    skus = sorted(skus, reverse=True)
    for item in skus:
        if item not in PRODUCTS:
            return -1
        num = bucket.get(item, 0) + 1
        bucket[item] = num
    print(f"\n{bucket}")
    for item, num in bucket.items():
        specials = PRODUCTS.get(item, {}).get("specials")
        regular = PRODUCTS.get(item, {}).get("regular")

        if specials:
            applied_special = False
            for special_offer in specials[::-1]:
                related = special_offer.get("related")
                cnt = special_offer["cnt"]
                if cnt > num:
                    continue
                applied_special = True
                price = special_offer["price"]
                discount_cnt = num // cnt
                if related:
                    related_price = PRODUCTS[related]["regular"]
                    discount_price = -(discount_cnt * related_price) if related in bucket else 0
                    print(f"discount_price: {discount_price}")
                    bucket[related] = bucket[related] - 1
                    print(f"bucket[related]: {bucket[related]}")
                    item_price = discount_price + (cnt * regular)
                    print(f"(cnt * regular): {(cnt * regular)}")
                    print(f"item_price: {item_price}")

                else:
                    item_price = (discount_cnt * price)
                total += item_price
                print(f"num before: {num}")
                num -= (discount_cnt * cnt)
                print(f"num after: {num}")

            if not applied_special or num:
                total += (num * regular)
            print(f"total: {total}")
        else:
            total += (num * regular)

    return total







