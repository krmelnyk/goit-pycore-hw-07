from collections import UserDict


class Field:
    """Base class for record fields."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Class for storing contact name (required field)."""

    def __init__(self, value: str):
        if not value:
            raise ValueError("Name cannot be empty.")
        super().__init__(value)


class Phone(Field):
    """Class for storing phone number with validation (10 digits)."""

    def __init__(self, value: str):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


class Record:
    """Class for storing contact information."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        """Add new phone to record."""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """Remove phone from record."""
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
        else:
            raise ValueError("Phone not found.")

    def edit_phone(self, old_phone: str, new_phone: str):
        """Edit existing phone."""
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            self.phones.remove(phone_obj)
            self.phones.append(Phone(new_phone))
        else:
            raise ValueError("Phone not found.")

    def find_phone(self, phone: str):
        """Find phone in record."""
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class AddressBook(UserDict):
    """Class for storing and managing records."""

    def add_record(self, record: Record):
        """Add record to address book."""
        self.data[record.name.value] = record

    def find(self, name: str):
        """Find record by name."""
        return self.data.get(name)

    def delete(self, name: str):
        """Delete record by name."""
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Record not found.")