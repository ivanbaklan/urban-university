class Shop:

    def __init__(self):
        self.__file_name = "products.txt"

    def add(self, *products):
        for product in products:
            if product.name not in self.get_products():
                file = open(self.__file_name, "a")
                file.write(f"{product}\n")
                file.close()
            else:
                print(f"Продукт {product.name} уже есть в магазине")

    def get_products(self):
        file = open(self.__file_name, "r")
        data = file.read()
        file.close()
        return data


class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


s1 = Shop()
p1 = Product("Potato", 50.5, "Vegetables")
p2 = Product("Spaghetti", 3.4, "Groceries")
p3 = Product("Potato", 5.5, "Vegetables")

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

# Первый запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Продукт Spaghetti уже есть в магазине
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
