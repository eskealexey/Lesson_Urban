class Product:
    def __init__(self, name: str, weigth: float, category: str):
        self.name = name
        self.weight = weigth
        self.category = category

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.weight, self.category)


class Shop:
    __file_name = 'product.txt'
    def get_products(self):
        with open(file=self.__file_name, mode='r', encoding='utf-8') as f:
            list_products = f.read()
        return list_products

    def add(self, *products: Product):
        text = self.get_products()

        for product in products:
            if product.name in text:
                print("{} уже есть в магазине".format(product))
            else:
                with open(file=self.__file_name, mode='a', encoding='utf-8') as f:
                    f.write("{}\n".format(product))


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spagetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())




