''' Створення класів, конструкторів, методів '''
# class Animal:
#     def __init__(self, nickname='', age=5):
#         self.nickname = nickname                # ініціалізація змінних (обов'язково)
#         self.age = age                          # ініціалізація змінних (обов'язково)

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"


# animal = Animal()
# print(animal.nickname)
# print(animal.age)
# print(animal.get_info())
# animal.age = 5
# print(animal.get_info())

"""
Базові принципи ООП - Спадкування
Спадкування є властивістю об'єктів породжувати своїх нащадків.
Об'єкт-нащадок автоматично успадковує від батька все:
поля та методи, може доповнювати об'єкти новими полями та змінювати (перекривати) методи батька або доповнювати їх.
"""
# class Animal:
#     def __init__(self, nickname, age):
#         self.nickname = nickname
#         self.age = age

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"

# class Cat(Animal):
#     name = ['Cat']     # mutable

#     def __init__(self, nickname, age, owner):
#         super().__init__(nickname, age)
#         self.owner = owner

#     def sound(self):
#         return f'{self.nickname} says Meow!!!!'

#     def get_info(self):
#         return 5 * 5


# cat = Cat('Borys', 3, 'Valerii')
# print(cat.nickname)
# print(cat.age)
# cat.age = 6
# print(cat.get_info())
# print(cat.sound())

# cat_2 = Cat('Jack', 2, 'Ivan')
# print(f'cat.name: {cat.name}')

# cat.name[0] = 'Test'

# print(f'cat.name: {cat.name}')
# print(f'cat_2.name: {cat_2.name}')
# print(f'Cat.name: {Cat.name}')


# class Car:
#     brand = 'TOYOTA'

# p1 = Car()
# p2 = Car()
# print(p1.brand)
# print(p2.brand)

# # Car.brand = 'Daewoo'
# # print(p1.brand)
# # print(p2.brand)
# p1.brand = 'Mazda'
# print(p1.brand)
# print(p2.brand)

# print(dir(cat))

"""
Базові принципи ООП - Поліморфізм
Поліморфізм - це властивість споріднених об'єктів (тобто об'єктів, що мають одного спільного батька)
вирішувати схожі за змістом проблеми різними способами.
"""
# class Animal:
#     def __init__(self, nickname, age):
#         self.nickname = nickname
#         self.age = age

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"


# class Cat(Animal):
#     def __init__(self, nickname, age, owner):
#         super().__init__(nickname, age)
#         self.owner = owner

#     def sound(self):
#         return f'{self.nickname} says Meow!!!!'

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"


# class Dog(Animal):
#     def __init__(self, nickname, age, owner):
#         super().__init__(nickname, age)
#         self.owner = owner

#     def sound(self):
#         return f'{self.nickname} says Woof !!!!'

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"

# cat = Cat('Borys', 4, 'Ivan')
# dog = Dog('Bella', 3, 'Petro')

# print(isinstance(dog, Animal))
# print(isinstance(dog, Cat))
# print(isinstance(dog, Dog))
# print('============')
# print(type(dog) is Animal)
# print(type(dog) is Dog)

# for element in (cat, dog):
#     print(element.sound())

"""
Асоціація
Це коли один клас включає інший клас як один з полів. Асоціація описується словом "має".
Тварина має господаря.
Виділяють два окремі випадки асоціації: композицію та агрегацію.
Композиція
Це коли господар не існує окремо від вихованця. Він створюється при створенні вихованця і повністю управляється вихованцем.
КОМПОЗИЦІЯ - це якщо цикл життя одного об'єкта нерозривно зв'язаний з циклом життя іншого об'єкта.
Агрегація
АГРЕГАЦІЯ - це якщо цикл життя одного об'єкта не пов'язаний з циклом життя іншого об'єкта але взаємодіє з ним. 
"""

# class Animal:
#     def __init__(self, nickname, age):
#         self.nickname = nickname
#         self.age = age

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"

# class Owner:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone

#     def info(self):
#         return f'{self.name}- {self.phone}'

# class Cat(Animal):
#     def __init__(self, nickname, age, name, phone):
#         super().__init__(nickname, age)
#         self.owner = Owner(name, phone)  # композиція

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"

#     def sound(self):
#         return f'{self.nickname} says Meow!!!!'

# cat = Cat('Alex', 3, 'Petro', '0951234567')
# print(cat.owner.info())

"""
Агрегація
Це коли екземпляр господаря створюється десь в іншому місці коду, і передається в конструктор вихованця як параметр
Так є правильно. Так завди і робити.
"""

# class Animal:
#     def __init__(self, nickname, age):
#         self.nickname = nickname
#         self.age = age

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"


# class Owner:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone

#     def info(self):
#         return f'{self.name}- {self.phone}'


# class Cat(Animal):
#     def __init__(self, nickname, age, owner: Owner):
#         super().__init__(nickname, age)
#         self.owner = owner  # агрегація

#     def get_info(self):
#         return f"It's class Animal. Name is {self.nickname} and his age is: {self.age}"

#     def sound(self):
#         return f'{self.nickname} says Meow!!!!'


# owner = Owner('Petro', '0951233455')
# cat = Cat('Alex', 3, owner)
# print(cat.owner.info())

"""
Method Resolution Order (MRO).
MRO в Python працює наступним чином:
1. Шукає атрибут серед атрибутів самого класу. Саме завдяки цьому ви можете "перевизначати"
батьківські атрибути.
2. Шукає атрибут у першого з батьків (той, що зазначено першим у списку батьків).
3. Шукає атрибут у наступного батька у списку батьків, доки такі є.
4. Шукає атрибут у батьках першого з батьків.
5. Повторює п.4 всім батьків.
6. Викликає виняток, що атрибут не знайдено.
"""

# class A:
#     def hi(self):
#         print('A')

# class B(A):
#     def hi(self):
#         print('B')

# class C(A):
#     def hi(self):
#         print('C')

# class D(B, C):
#     def hi_(self):
#         print(55)

# d = D()
# d.hi()
# print(D.__mro__)   # магічний метод який показує де буде відбуватись пошук атрибутів

# #####

# class Human:
#     pass


# class Developer(Human):
#     field_description = "My Programming language"
#     language = ""
#     value = ''
#     def make_some_code(self):
#         return f"{self.field_description} is {self.value}"

#     def test(self):
#         return 25


# class PythonDeveloper(Developer):
#     value = "Python"

#     def make_some_code(self):
#         res = self.test()
#         return f"{self.field_description} is {self.value}. Result is: {res}"


# class JSDeveloper(Developer):
#     value = "JavaScript"


# a = PythonDeveloper()
# print(a.make_some_code())

# dev = Developer()
# dev.value = 'Python'
# print(dev.make_some_code())

''' Контейнери UserList '''

# from collections import UserList
# from random import randint

# class MyList(UserList):
#     info = 'This is my list class'

#     def get_positive(self):
#         return list(filter(lambda x: x > 0, self.data))

#     def get_negative(self):
#         return list(filter(lambda x: x < 0, self.data))

#     def get_info(self):
#         return self.info

# r = []
# for _ in range(0, 35):
#     r.append(randint(-10, 10))

# result = MyList(r)
# print(result)

# result.append(5555)
# print(result)
# print(result.get_positive())
# print(result.get_negative())
# print(result.get_info())

'''Словник UserDict'''
# from collections import UserDict

# contacts = [
#    {
#        "name": "Allen Raymond",
#        "email": "nulla.ante@vestibul.co.uk",
#        "phone": "(992) 914-3792",
#        "favorite": False,
#    },
#    {
#        "name": "Chaim Lewis",
#        "email": "dui.in@egetlacus.ca",
#        "phone": "(294) 840-6685",
#        "favorite": False,
#    },
#    {
#        "name": "Kennedy Lane",
#        "email": "mattis.Cras@nonenimMauris.net",
#        "phone": "(542) 451-7038",
#        "favorite": True,
#    },
#    {
#        "name": "Wylie Pope",
#        "email": "est@utquamvel.net",
#        "phone": "(692) 802-2949",
#        "favorite": False,
#    },
#    {
#        "name": "Cyrus Jackson",
#        "email": "nibh@semsempererat.com",
#        "phone": "(501) 472-5218",
#        "favorite": True,
#    },
# ]

# class Customer(UserDict):
#     def get_phone(self):
#         return f"{self.get('name')}: {self.get('phone')}"

#     def get_email(self):
#         return f"{self.get('name')}: {self.get('email')}"

# customers = [Customer(contact) for contact in contacts]
# print(customers)

# for customer in customers:
#     print(customer.get_email())
#     print(customer.get_phone())

'''Строки UserString'''
# from collections import UserString

# template = [
#     "Ви можете досягти всього. Варто лише трохи постаратися і запастися книгами.",
#     "Цей смартфон - справжня знахідка. Великий і яскравий екран, потужний процесор - все це в невеликому гаджеті.",
#     "Зібрати камені нескінченності легко, якщо ви природжений герой.",
#     "Освоїти верстку нескладно. Візьміть книгу нову книгу і закріпіть усі вправи на практиці.",
#     "Боротися з прокрастинацією нескладно. Просто дійте. Маленькими кроками.",
#     "Програмувати не настільки складно, як про це говорять.",
#     "Прості щоденні вправи допоможуть досягти успіху."
# ]


# # for item, text in enumerate(template):
# #     print("|{:^5}|{:<15}".format(item, text))

# class Text(UserString):
#     def set_limit_text(self, limit=15):
#         return (f'{self.data[:limit]}...')


# text = [Text(text) for text in template]
# for item, text in enumerate(text):
#     print("|{:^5}|{:<15}".format(item, text.set_limit_text(35)))