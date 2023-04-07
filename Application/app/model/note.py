import datetime


class Note:
    def __init__(self, data: tuple):
        self.id = data[0]
        self.date = data[1]
        self.header = data[2]
        self.body = data[3]

    def __eq__(self, other):
        if not self.equals(other):
            return False
        if self.date != other.date:
            return False
        if self.header != other.header:
            return False
        if self.body != other.body:
            return False
        return True

    def equals(self, other):
        if self.id != other.id:
            return False
        return True

    def set_header(self, header: str):
        self.header = header

    def set_body(self, body: str):
        self.body = body

    def set_date(self, date: datetime):
        self.date = date

    def edit(self, other):
        self.header = other.header
        self.body = other.body
        self.date = other.date

    def get(self) -> tuple:
        data = (self.id, self.date, self.header, self.body)
        return data
