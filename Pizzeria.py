#Создаю класс для проверки title на заполненость и для наследования в следующих классах
class Base():
    def __init__(self, title):
        if Base.check_title(title):
            self.__title = title
        else:
            raise ValueError

    @staticmethod
    def check_title(title):
        return title != ''

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if Base.check_title(title):
            self.__title = title
        else:
            raise ValueError


# Наследую в созданынй класс Product класс Base.В классе Product проверяю на отрицательные значения
# атрибуты caloric,cost 
class Product(Base):
    def __init__(self, title, caloric, cost):
        if Product.check_object(caloric) and Product.check_object(cost):
            self.__caloric = caloric
            self.__cost = cost
            super().__init__(title)
        else:
            raise ValueError

    def __str__(self):
        return f'Продукт {self.title} колорийность на 100 гр. {self.__caloric} kkal стоимость за 100 гр. {self.__cost} руб.'

    @staticmethod
    def check_object(object):
        return object > 0
    
    
   
    @property
    def caloric(self):
        return self.__caloric

    @property
    def cost(self):
        return self.__cost

    @caloric.setter
    def caloric(self, caloric):
        if Product.check_object(caloric):
            self.__caloric = caloric
        else:
            raise ValueError

    @cost.setter
    def cost(self, cost):
        if Product.check_object(cost):
            self.__cost = cost
        else:
            raise ValueError


# В классе Ingredient реализую метды для расчета калрийности и себестоимость
class Ingredient():
    def __init__(self, product, weight):
        if Ingredient.check_weight(weight):
            self.product = product
            self.__weight = weight
        else:
            raise ValueError

    def __str__(self):
        return f'{self.product} весом {self.__weight} гр.'

    @staticmethod
    def check_weight(weight):
        return weight > 0

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if Ingredient.check_weight(weight):
            self.__weight = weight
        else:
            raise ValueError


    def get_cost_price(self):
        product_cost = self.product.cost
        return product_cost * (self.__weight / 100)
    
    def get_kkal(self):
        kkal_value = self.product.caloric
        return kkal_value * (self.__weight / 100)



# Класс Pizza наследует title из класса Base, переопределяю два метода по расчету себестоимости и калорийности
# По принципу полиморфизма (но он тут реализован не совсем, как должен)
class Pizza(Base):
    
    def __init__(self, title, ingredients):
        super().__init__(title)
        self.ingredients = ingredients
        
    def __str__(self):
         return f'Пицца {self.title} ({self.get_kkal()} kkal) - {self.get_cost_price()} руб.'
    
    def get_cost_price(self):
        total_cost = 0
        for ingredient in self.ingredients:
            product_cost = ingredient.get_cost_price()
            total_cost += product_cost
        return  total_cost

    def get_kkal(self):
        total_kkal = 0
        for ingredient in self.ingredients:
            product_kkal = ingredient.get_kkal()
            total_kkal += product_kkal 
        return  total_kkal    

   

dough_product = Product('Тесто',-10, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)
dough_ingredient = Ingredient(dough_product, 100)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 100)
pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])
print(pizza_margarita)

    