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
        "specials": {
            "cnt": 2,
            "price": 45
        }
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
    for item in skus:
        if item not in PRODUCTS:
            return -1
        num = bucket.get(item, 0) + 1
        bucket[item] = num
    for item, num in bucket.items():
        specials = PRODUCTS.get(item, {}).get("specials")
        regular = PRODUCTS.get(item, {}).get("regular")
        if specials:
            for special_offer in specials:
                print(f"\nspecial_offer: {special_offer}")
                related = special_offer.get("related")
                cnt = special_offer["cnt"]
                price = special_offer["price"]
                discount_cnt = num // cnt

                if related:
                    related_price = PRODUCTS[related]["regular"]
                    item_price = -(discount_cnt * related_price) + ((num % cnt) * regular)
                else:
                    item_price = (discount_cnt * price) + ((num % cnt) * regular)

                total += item_price
        else:
            total += (num * regular)
    return total

