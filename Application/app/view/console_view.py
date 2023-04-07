import datetime as dt
from model.note import Note
import controller.validator as valid


def prompt(message: str) -> str:
    return input(message)


def menu():
    print("Список команд:")
    print("\t\tadd - добавление заметки;")
    print("\t\tread - чтение заметки;")
    print("\t\tedit - редактирование заметки;")
    print("\t\tdelete - удаление заметки;")
    print("\t\tlist - список заметок;")
    print("\t\tsave - сохранить заметки;")
    print("\t\texit - выйти\n")


def input_data() -> tuple:
    header = valid.validate_header(prompt("Введите заголовок: "))
    body = valid.validate_body(prompt("Введите тело записки: "))
    date = valid.validate_datetime(dt.datetime.now())
    return 0, date, header, body


def print_note(note: Note):
    data = note.get()
    print(str(data[0]) + ". [" + data[1] + "]")
    print("\t\t\t\t"+data[2])
    print("\t" + data[3])

