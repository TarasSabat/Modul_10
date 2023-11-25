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
    
    
    def edit_phone(self, old_phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i].value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
            raise ValueError('Phone not found')

   
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:  
                return Phone(phone_number)

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