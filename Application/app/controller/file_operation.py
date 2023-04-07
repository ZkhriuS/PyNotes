def default_filename() -> str:
    return 'notes.txt'


def write(data: str, filename: str = default_filename()):
    with open(filename, 'w') as f:
        f.write(data)


def all_read(filename: str = default_filename()) -> str:
    try:
        with open(filename, 'r') as f:
            return f.read()
    except Exception as e:
        with open(filename, 'w'):
            return ''
