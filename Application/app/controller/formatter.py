import re
from model.note import Note


def json_parse(text: str) -> list:
    text_items = re.split("ID: |\nDate: |\nHeader: |\nBody: ", text)
    text_items.remove('')
    data = []
    if len(text_items) <= 1:
        return data
    for i in range(0, len(text_items), 4):
        note = Note((int(text_items[i]), text_items[i + 1], text_items[i + 2], text_items[i + 3][0:-1]))
        data.append(note)
    return data


def json_format(data: list) -> str:
    text = str()
    for item in data:
        note = item.get()
        text += "ID: " + str(note[0])
        text += "\nDate: " + str(note[1])
        text += "\nHeader: " + note[2]
        text += "\nBody: " + note[3] + "\n"
    return text


def csv_parse(text: str) -> list:
    text_items = re.split(";\n", text)
    text_items.remove('')
    data = []
    if len(text_items) == 0:
        return data
    for item in text_items:
        data_items = re.split(";", item)
        note = Note((int(data_items[0]), data_items[1], data_items[2], data_items[3]))
        data.append(note)
    return data


def csv_format(data: list) -> str:
    text = str()
    for item in data:
        note = item.get()
        for data_item in note:
            text += str(data_item) + ';'
        text += '\n'
    return text

