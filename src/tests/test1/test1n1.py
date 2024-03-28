from __future__ import annotations

from typing import List


class Product:
    def __init__(self, name: str, cost: float, rating: float, quantity: int) -> None:
        self.name = name
        self.cost = cost
        self.rating = rating
        self.quantity = quantity

    def __add__(self, other: Product) -> Product:
        if other.name != self.name or other.cost != self.cost or other.rating != self.rating:
            raise TypeError("Product names, costs or ratings do not match.")
        return Product(self.name, self.cost, self.rating, self.quantity + other.quantity)

    def __sub__(self, other: Product) -> Product:
        if other.name != self.name or other.cost != self.cost or other.rating != self.rating:
            raise TypeError("Product names, costs or ratings do not match.")
        return Product(self.name, self.cost, self.rating, self.quantity - other.quantity)


class Cart:
    def __init__(self) -> None:
        self.cost = 0.0
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        product_names = [product.name for product in self.products]
        if product.name not in product_names:
            self.products.append(product)
        else:
            self.products[product_names.index(product.name)] += product
        self.cost = sum([p.cost * p.quantity for p in self.products])

    def delete_product(self, product: Product) -> None:
        product_names = [product.name for product in self.products]
        if product.name not in product_names:
            pass
        else:
            self.products[product_names.index(product.name)] -= product
        self.cost = sum([p.cost * p.quantity for p in self.products])


class Shop:
    def __init__(self, assortment: Cart) -> None:
        self.assortment = assortment

    def get_expensive(self) -> Product:
        return max(self.assortment.products, key=lambda x: x.cost)

    def get_cheap(self) -> Product:
        return min(self.assortment.products, key=lambda x: x.cost)

    def get_best(self) -> Product:
        return max(self.assortment.products, key=lambda x: x.rating)

    def get_worst(self) -> Product:
        return min(self.assortment.products, key=lambda x: x.rating)

    def buy(self, cart: Cart) -> None:
        for product in cart.products:
            self.assortment.delete_product(product)


def main() -> None:
    shop_storage = Cart()
    for x in [
        Product("Snackers", 70, 4.7, 100),
        Product("Kirieshki", 45, 4.5, 150),
        Product("Twux", 65, 4.6, 35),
        Product("Cola", 90, 4.3, 20),
        Product("Banana", 30, 1.7, 27),
    ]:
        shop_storage.add_product(x)
    best_shop = Shop(shop_storage)
    print("Before:")
    for p in best_shop.assortment.products:
        print(p.name, p.quantity)
    print(f"Cost of all in Goshan: {best_shop.assortment.cost}\n\n")

    dima_cart = Cart()
    sasha_cart = Cart()
    dima_cart.add_product(Product("Snackers", 70, 4.7, 5))
    sasha_cart.add_product(Product("Twux", 65, 4.6, 2))
    sasha_cart.add_product(Product("Cola", 90, 4.3, 1))
    print(f"Dima must pay: {dima_cart.cost}\nSasha must pay: {sasha_cart.cost}\n\n")
    best_shop.buy(dima_cart)
    best_shop.buy(sasha_cart)

    print("After:")
    for p in best_shop.assortment.products:
        print(p.name, p.quantity)
    print(f"Cost of all in Goshan: {best_shop.assortment.cost}")


if __name__ == "__main__":
    main()
