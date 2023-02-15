import uuid
from datetime import datetime


class Note:

    def __init__(self, title):
        self.__id = uuid.uuid4()
        self.__title = title
        self.__date = datetime.now()

    @classmethod
    def of(cls, id: str, title: str, date: datetime):
        note = cls(title)
        note.__id = id
        note.__date = date
        return note

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def date(self):
        return self.__date

    def __str__(self):
        return 'Заметка:\n' \
               f'Id: {self.__id}\n' \
               f'Title: {self.__title}\n' \
               f'Date: {self.__date.strftime("%m-%d-%Y:%H:%M:%S")}\n'
