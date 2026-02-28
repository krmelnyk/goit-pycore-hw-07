"""Public interface for the assistant package."""

from .address_book import AddressBook, Record
from .handlers import (
    add_birthday,
    add_contact,
    birthdays,
    change_contact,
    show_all,
    show_birthday,
    show_phone,
)
from .parser import parse_input

__all__ = [
    "AddressBook",
    "Record",
    "parse_input",
    "add_contact",
    "change_contact",
    "show_phone",
    "show_all",
    "add_birthday",
    "show_birthday",
    "birthdays",
]
