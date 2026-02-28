# Assistant Bot

A simple console assistant for storing contacts and phone numbers.

## Run

Requirements:
- Python 3.9+

Run from the project root:

```bash
python3 src/main.py
```

## Supported commands

- `hello` - greeting from the bot.
- `add <name> <phone>` - add a new contact or append one more phone to an existing contact.
- `change <name> <old_phone> <new_phone>` - replace one phone number with another.
- `phone <name>` - show all phone numbers for a contact.
- `all` - show all contacts.
- `add-birthday <name> <DD.MM.YYYY>` - add or replace birthday for a contact.
- `show-birthday <name>` - show a contact's birthday.
- `birthdays` - show upcoming birthdays in the next 7 days (weekend birthdays shift to Monday).
- `close` or `exit` - quit the application.

## Examples

```text
Enter a command: hello
How can I help you?

Enter a command: add Anna 0931234567
Contact added.

Enter a command: phone Anna
0931234567

Enter a command: add Anna 0501112233
Contact updated.

Enter a command: phone Anna
0931234567; 0501112233

Enter a command: change Anna 0931234567 0672223344
Contact updated.

Enter a command: add-birthday Anna 01.03.1995
Birthday added.

Enter a command: show-birthday Anna
01.03.1995

Enter a command: birthdays
No birthdays in the next 7 days.

Enter a command: all
Contact name: Anna, phones: 0501112233; 0672223344, birthday: 01.03.1995

Enter a command: exit
Good bye!
```

## Phone number format constraints

- A phone number must contain exactly `10` digits.
- Only digits are allowed, without spaces or symbols (`+`, `-`, `(`, `)`, etc.).
- Valid format examples: `0931234567`, `0501112233`.
