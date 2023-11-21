from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        # super().__init__(value)
        self.name = name
        # self.value = value
    def set_name(self, name):
        self.name = name
        print(self.name)
    # реалізація класу

class ValueError(Exception):
    def __init__(self, message="Invalid phone number"):
        self.message = message
        super().__init__(self.message)

class Phone(Field):
    def validate(self, value):
        if len(value) != 10:
            raise ValueError('Phone should be 10 symbols')
        return self.phones.append(value)
    
    def set_phone(self, phone_numder):
        self.phone_numder = phone_numder
        self.data['phone'] = self.phone_numder
    # реалізація класу

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)

    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone_number

    def edit_phone(self, old_phone, new_phone):
        # put your logic here
        pass

    def remove_phone(self, phone):
        # put your logic here
        pass

    # реалізація класу

class AddressBook(UserDict):
    def add_record(self):
        # додає запис до self.data.  Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується значення Record.name.value.
    def find(self, name):
        
        # знаходить запис за ім'ям.
    def delet(sels):
        # видаляє запис за ім'ям.


book = AddressBook()

############################    
        



             
    # реалізація класу
    
    
# Після реалізації ваш код має виконуватися наступним чином:

#     # Створення нової адресної книги
#     book = AddressBook()
    

#     # Створення запису для John
#     john_record = Record("John")
#     john_record.add_phone("1234567890")
#     john_record.add_phone("5555555555")

#     # Додавання запису John до адресної книги
#     book.add_record(john_record)

#     # Створення та додавання нового запису для Jane
#     jane_record = Record("Jane")
#     jane_record.add_phone("9876543210")
#     book.add_record(jane_record)

#     # Виведення всіх записів у книзі
#     for name, record in book.data.items():
#         print(record)

#     # Знаходження та редагування телефону для John
#     john = book.find("John")
#     john.edit_phone("1234567890", "1112223333")

#     print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

#     # Пошук конкретного телефону у записі John
#     found_phone = john.find_phone("5555555555")
#     print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

#     # Видалення запису Jane
#     book.delete("Jane")