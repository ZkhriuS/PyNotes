from model.note import Note
import controller.formatter as frmt
import controller.file_operation as file


class Repository:
    def __init__(self, strfmt):
        self.format = strfmt
        match strfmt:
            case 'json': self.repository = frmt.json_parse(file.all_read())
            case 'csv': self.repository = frmt.csv_parse(file.all_read('csv_notes.txt'))

    def add(self, n: Note) -> list:
        n.id = self.index_incr()
        self.repository.append(n)
        return self.repository

    def get_repository(self) -> list:
        return self.repository

    def delete(self, _id: int) -> list:
        note = Note((_id, "", "", ""))
        for i in self.repository:
            if note.equals(i):
                self.repository.remove(i)
        return self.repository

    def edit(self, n: Note) -> list:
        for i in self.repository:
            if n.equals(i):
                i.edit(n)
        return self.repository

    def save(self):
        match self.format:
            case 'json': file.write(frmt.json_format(self.repository))
            case 'csv': file.write(frmt.csv_format(self.repository), 'csv_notes.txt')

    def index_incr(self):
        _max = 0
        for item in self.repository:
            if _max < item.id:
                _max = item.id
        return _max + 1
