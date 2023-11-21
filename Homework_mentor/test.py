from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError('Phone should be 10 symbols')
        super().__init__(value)
    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone_number: str):     
        phone = Phone(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)
           
    def remove_phone(self, phone_number):              
        self.phones = [phone for phone in self.phones if phone.value != phone_number]
       
    # def edit_phone(self, old_phone, new_phone):    # варіант чат-бота
    #     self.remove_phone(old_phone)
    #     self.add_phone(new_phone)
    
    def edit_phone(self, old_phone, new_phone):
        for i in self.phones:
            a = i # print(self.phones[i])
            b = int(old_phone) # print(old_phone)
            if a==b: #self.phones[i] == old_phone:
            
                print(0)
        
        # for i in range(len(self.phones)):
        #     a=self.phones[i] # print(self.phones[i])
        #     b=int(old_phone) # print(old_phone)
        #     if a==b: #self.phones[i] == old_phone:
        #         print('ok')
        #         self.phones[i] = new_phone
        #         print(self.phones)
            
        
        # for p in self.phones:
        #     if p == int(old_phone):
                
        #             i = new_phone
                
            # if old_phone in self.phones:
            #     for i in range(len(self.phones)):
            #         if i == old_phone:
            #             i = new_phone
            # if old_phone == self.phones:
            #     self.phones = new_phone
        
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:  
                return phone_number

    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name}, phones: {phones_str}" 
 

class AddressBook(UserDict):
             
    def add_record(self, record):
        self.data[record.name.value] = record
            
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Контакт {name} видалено")
        else:
            print(f"Контакт {name} не знайдено")
    
    def find(self, name):
        if name in self.data:
            return self.data[name]
    
    
       
          
   

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

john = book.find("John")
print(john)

# Додавання запису John до адресної книги
# book.add_record(john_record)

# Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# jane = book.find("Jane")
# print(jane)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

john = book.find("John")
print(john)

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
# found_phone = jane.find_phone("9876543210")
# print(f"{jane.name}: {found_phone}")  # Виведення: 5555555555

# # Видалення запису Jane
# book.delete("Jane")
        
    





