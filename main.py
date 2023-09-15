from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be a 10-digit number")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        raise ValueError(f"Phone number '{old_phone}' not found")

    def find_phone(self, phone):
        phones_found = [p for p in self.phones if p.value == phone]
        return phones_found[0] if phones_found else None

        # found_phones = list(map(lambda p: p.value, filter(lambda p: p.value == phone, self.phones)))
        # return found_phones if found_phones else None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]


if __name__ == "__main__":
    address_book = AddressBook()
    record1 = Record("John")
    record1.add_phone("1234567890")
    record1.add_phone("0987654321")
    address_book.add_record(record1)

    record2 = Record("Alice")
    record2.add_phone("9876543210")
    address_book.add_record(record2)

    print(record1.find_phone("1234567890"))
    print(record1.find_phone("0987654321"))

    print(address_book.find("John"))
