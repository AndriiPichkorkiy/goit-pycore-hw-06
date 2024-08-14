from collections import UserDict


class PhoneValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)


# Base class for record fields
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


# A class for storing a contact name. Mandatory field.
class Name(Field):
    def __init__(self, value):
        super().__init__(value)


# A class for storing a phone number. Has format validation (10 digits).
class Phone(Field):
    def __init__(self, value):
        if len(value) == 10:
            super().__init__(value)
        else:
            raise PhoneValidationError("Valid phone length is 10")


# A class for storing information about a contact, including name and phone list.
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def find_phone(self, phone_to_find):
        for phone in self.phones:
            if phone.value == phone_to_find:
                return phone

    # privat method
    def __find_phone_index__(self, phone_to_find):
        for i, phone in enumerate(self.phones):
            if phone.value == phone_to_find:
                return i

    def remove_phone(self, phone):
        phone_to_delete = self.find_phone(phone)
        self.phones.remove(phone_to_delete)

    def edit_phone(self, phone, new_phone):
        index = self.__find_phone_index__(phone)
        self.phones[index] = Phone(new_phone)


# A class for storing and managing records.
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name]

    def delete(self, name):
        del self.data[name]


# testing:
def main():
    # Creating a new address book
    book = AddressBook()

    # Create record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Adding John to the address book
    book.add_record(john_record)

    # Create and add a new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Output of all entries in the book
    for name, record in book.data.items():
        print(record)

    # Find and edit phone for John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Output: Contact name: John, phones: 1112223333; 5555555555

    # Search for a specific phone in the John record
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Deleting Jane's record
    book.delete("Jane")


if __name__ == "__main__":
    main()
