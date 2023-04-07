import view.console_view as v
from model.repository import Repository
from model.note import Note


def run():
    frmt = v.prompt("Введите формат файла для записок: ")
    rep = Repository(frmt)
    while True:
        v.menu()
        command = v.prompt("Введите команду: ")
        match command:
            case 'add': add(rep)
            case 'read': read(rep)
            case 'edit': edit(rep)
            case 'delete': delete(rep)
            case 'list': list_notes(rep)
            case 'save': save(rep)
            case 'exit': return
            case _: "Неизвестная команда!"


def add(rep: Repository):
    note = Note(v.input_data())
    rep.add(note)
    print("Записка успешно добавлена!")


def read(rep: Repository) -> int:
    _id = int(v.prompt("Введите ID записки: "))
    for note in rep.get_repository():
        if note.id == _id:
            v.print_note(note)
            return _id
    print("Записка не найдена!")
    return -1


def edit(rep: Repository):
    _id = read(rep)
    if _id < 0:
        return
    note = Note(v.input_data())
    note.id = _id
    rep.edit(note)
    print("Записка успешно отредактирована!")


def delete(rep: Repository):
    _id = read(rep)
    if _id < 0:
        return
    rep.delete(_id)
    print("Записка успешно удалена!")


def list_notes(rep: Repository):
    if len(rep.get_repository()) > 0:
        for item in rep.get_repository():
            v.print_note(item)
        return
    print("Список записок пуст.")


def save(rep: Repository):
    rep.save()
    print("Сохранение записок")




