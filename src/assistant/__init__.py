"""Public interface for the assistant package."""

from .handlers import add_contact, change_contact, show_all, show_phone
from .parser import parse_input

__all__ = [
    "parse_input",
    "add_contact",
    "change_contact",
    "show_phone",
    "show_all",
]
