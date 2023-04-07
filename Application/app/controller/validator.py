import datetime


def validate_header(header: str) -> str:
    if header.rfind('\n') != -1:
        header = 'Header'
    return header


def validate_body(body: str) -> str:
    return body


def validate_datetime(date_value: datetime) -> str:
    return date_value.strftime("%d.%m.%Y-%H:%M:%S")

