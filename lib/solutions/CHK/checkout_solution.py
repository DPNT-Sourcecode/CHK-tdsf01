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
    skus = sorted(skus)
    for item in skus:
        if item not in PRODUCTS:
            return -1
        num = bucket.get(item, 0) + 1
        bucket[item] = num

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
                    if related in bucket:
                        related_cnt = bucket[related]
                        expected_to_deduct = related_cnt // cnt
                        discount_price = -(expected_to_deduct * 45 + (related_cnt - (expected_to_deduct * cnt)))
                    else:
                        discount_price = 0
                    item_price = discount_price + (discount_cnt * cnt * regular)


                else:
                    item_price = (discount_cnt * price)
                total += item_price
                num -= (discount_cnt * cnt)

            if not applied_special or num:
                total += (num * regular)

        else:
            total += (num * regular)
        print(f"\ntotal: {total}")
    return total


