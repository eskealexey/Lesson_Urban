class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.weight, self.category)


class Shop:
    __file_name = 'product.txt'
    lst_product = []

    def get_products(self):
        with open(file=self.__file_name, mode='r', encoding='utf-8') as f:
            strig_ = f.read()
            return strig_

    def add(self, *products):
        with open(file=self.__file_name, mode='r', encoding='utf-8') as fr:
            vv = fr.readlines()
            print(vv)


        for v in range(len(products)):
            prod = str(products[v]).split(', ')
            if not prod[0] in self.lst_product:
                self.lst_product.append(prod[0])
                with open(file=self.__file_name, mode='a', encoding='utf-8') as f:
                    f.writelines(str(products[v]) + '\n')




s1 = Shop()
p1 = Product('Potati', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potati', 5.5, 'Vegetables')


s1.add(p1, p2, p3)
print(s1.lst_product)
