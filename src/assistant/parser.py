def parse_input(user_input: str):
    """Parse user input into command and list of arguments."""
    parts = user_input.strip().split()

    if not parts:
        raise ValueError("Empty input")

    command = parts[0].lower()
    args = parts[1:]
    return command, args
