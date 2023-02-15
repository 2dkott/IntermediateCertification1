from note import Note
from datetime import datetime

DATE_FORMAT = "%d-%m-%Y:%H:%M:%S"
DATE_INPUT = "%d-%m-%Y"


def map_from_list(values: []):
    return Note.of(values[0], values[1], datetime.strptime(values[2], DATE_FORMAT))


def map_to_list(note: Note):
    return [note.id, note.title, note.date.strftime(DATE_FORMAT)]


def map_date_to_string(date: datetime):
    return date.strftime(DATE_INPUT)
