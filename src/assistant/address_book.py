from collections import UserDict
from datetime import date, datetime, timedelta


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


class Birthday(Field):
    """Class for storing birthday in DD.MM.YYYY format."""

    def __init__(self, value: str):
        try:
            parsed_date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError as exc:
            raise ValueError("Invalid date format. Use DD.MM.YYYY") from exc
        super().__init__(parsed_date)

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


class Record:
    """Class for storing contact information."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

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

    def add_birthday(self, birthday: str):
        """Add or replace birthday for record."""
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        birthday_str = str(self.birthday) if self.birthday else "not set"
        return (
            f"Contact name: {self.name.value}, "
            f"phones: {phones_str}, birthday: {birthday_str}"
        )


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

    @staticmethod
    def _birthday_for_year(source_date, year):
        """Return birthday date in the target year with leap day fallback."""
        try:
            return date(year, source_date.month, source_date.day)
        except ValueError:
            return date(year, 3, 1)

    def get_upcoming_birthdays(self):
        """Return birthdays within 7 days shifted from weekend to Monday."""
        today = date.today()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            birthday_this_year = self._birthday_for_year(
                record.birthday.value, today.year
            )
            if birthday_this_year < today:
                birthday_this_year = self._birthday_for_year(
                    record.birthday.value, today.year + 1
                )

            if 0 <= (birthday_this_year - today).days <= 7:
                congratulation_date = birthday_this_year
                if congratulation_date.weekday() == 5:
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append(
                    {
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime(
                            "%d.%m.%Y"
                        ),
                    }
                )

        return upcoming_birthdays
