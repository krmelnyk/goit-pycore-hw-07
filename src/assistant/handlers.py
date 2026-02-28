from .address_book import AddressBook, Record


def input_error(func):
    """Decorator for handling common user input errors."""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as error:
            if error.args:
                message = str(error.args[0])
            else:
                message = str(error)
            return message if message else "Invalid input."

    return inner


@input_error
def add_contact(args, book: AddressBook):
    """Add new contact or add one more phone to existing contact."""
    if len(args) < 2:
        raise ValueError("Give me name and phone please.")

    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    """Update an existing contact phone number."""
    if len(args) < 3:
        raise ValueError("Give me name, old phone and new phone please.")

    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")

    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def show_phone(args, book: AddressBook):
    """Return all phone numbers for a given contact name."""
    if not args:
        raise ValueError("Enter the contact name.")

    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    if not record.phones:
        return "No phones for this contact."
    return "; ".join(phone.value for phone in record.phones)


@input_error
def show_all(book: AddressBook):
    """Return all saved contacts as a formatted multi-line string."""
    if not book.data:
        return "No contacts saved."
    return "\n".join(str(record) for record in book.data.values())


@input_error
def add_birthday(args, book: AddressBook):
    """Add birthday for an existing contact."""
    if len(args) < 2:
        raise ValueError("Give me name and birthday please.")

    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def show_birthday(args, book: AddressBook):
    """Show birthday for an existing contact."""
    if not args:
        raise ValueError("Enter the contact name.")

    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    if record.birthday is None:
        raise ValueError("Birthday is not set for this contact.")
    return str(record.birthday)


@input_error
def birthdays(args, book: AddressBook):
    """Show upcoming birthdays in the next 7 days."""
    if args:
        raise ValueError("The birthdays command does not require arguments.")

    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays in the next 7 days."

    return "\n".join(
        f"{item['name']}: {item['congratulation_date']}" for item in upcoming
    )
