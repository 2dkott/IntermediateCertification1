import abc
from note import Note


class NoteRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def record_note(self, note: Note):
        raise NotImplementedError

    @abc.abstractmethod
    def find_note(self, note_id: int):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_note(self, note_id: int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_notes(self):
        raise NotImplementedError
