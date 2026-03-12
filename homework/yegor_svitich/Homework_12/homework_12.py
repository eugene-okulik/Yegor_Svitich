class Flower:
    def __init__(self, name, price, lifespan, freshness, color, stem_length):
        self.name = name
        self.price = price
        self.lifespan = lifespan  # среднее время до увядания (в днях)
        self.freshness = freshness  # свежесть по десятибалльной шкале, где 10 - наиболее свежий
        self.color = color
        self.stem_length = stem_length

    def __repr__(self):
        return (f"{self.name} | Цвет: {self.color} | "
                f"Свежесть: {self.freshness}/10 | Длина стебля: {self.stem_length}см | "
                f"Среднее время до увядания: {self.lifespan} дней | Цена: {self.price} BYN.")

class Rose(Flower):
    def __init__(self, price, freshness, color, stem_length):
        super().__init__("Роза", price, 7, freshness, color, stem_length)

class Tulip(Flower):
    def __init__(self, price, freshness, color, stem_length):
        super().__init__("Тюльпан", price, 5, freshness, color, stem_length)

class Lily(Flower):
    def __init__(self, price, freshness, color, stem_length):
        super().__init__("Лилия", price, 8, freshness, color, stem_length)

class Bouquet:
    def __init__(self):
        self.flowers = []
        self.params_map = {
            "стоимость": "price",
            "свежесть": "freshness",
            "цвет": "color",
            "длина стебля": "stem_length"
        }

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_total_price(self):
        return sum(f.price for f in self.flowers)

    def get_average_lifespan(self):
        if not self.flowers: return 0
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    # Метод поиска цветов со временем увядания больше либо равным среднему
    def find_by_average_lifespan(self):
        avg = self.get_average_lifespan()
        results = [flower for flower in self.flowers if flower.lifespan >= avg]
        print(f"\nЦветы со временем увядания >= среднему ({avg:.1f} дн.):")
        for flower in results:
            print(flower)
        return results

    def sort_by(self, parameter, reverse=False):
        attr = self.params_map.get(parameter.lower())
        if attr:
            self.flowers.sort(key=lambda flower: getattr(flower, attr), reverse=reverse)
            print(f"\nСортировка по параметру '{parameter}':")
            self.show()
        else:
            print(f"\nОшибка: параметр '{parameter}' не поддерживается.")

    def show(self):
        for flower in self.flowers:
            print(flower)


my_bouquet = Bouquet()
my_bouquet.add_flower(Rose(price=7, freshness=7, color="красный", stem_length=70))
my_bouquet.add_flower(Tulip(price=3, freshness=10, color="жёлтый", stem_length=35))
my_bouquet.add_flower(Lily(price=15, freshness=9, color="белый", stem_length=115))

# 1. Информация о букете
print(f"\nОбщая стоимость: {my_bouquet.get_total_price()} BYN.")
print(f"\nСреднее время до увядания: {my_bouquet.get_average_lifespan():.1f} дн.")

# 2. Пример сортировки
my_bouquet.sort_by("стоимость", reverse=True)

# 3. Поиск цветов со временем увядания больше либо равным среднему
my_bouquet.find_by_average_lifespan()
