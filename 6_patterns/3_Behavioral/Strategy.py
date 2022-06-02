class Price:

    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
        return self.price - discount

    def __repr__(self):
        result = f'Price: {self.price}, price after discount: {self.price_after_discount()}!'
        return result


def on_sale_discount(order):
    return order.price * 0.5


def twenty_persent_discount(order):
    return order.price * 0.2


if __name__ == "__main__":
    print(Price(20000))
    print(Price(20000, discount_strategy=on_sale_discount))
    print(Price(20000, discount_strategy=twenty_persent_discount))
