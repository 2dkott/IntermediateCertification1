from note_repository import NoteRepository
from note import Note
from note_exceptions import NoRecord


class NoteController:

    def __init__(self, repository: NoteRepository):
        self.__note_repository = repository

    def add_note(self, title):
        new_note = Note(title)
        self.__note_repository.record_note(new_note)
        return new_note

    def delete_note(self, note_id):
        self.__note_repository.delete_note(note_id)

    def find_note(self, note_id):
        note = self.__note_repository.find_note(note_id)
        if note is not None:
            return note
        raise NoRecord(note_id)

    def update_note(self, note_id, title):
        self.find_note(note_id)
        self.__note_repository.delete_note(note_id)
        self.__note_repository.record_note(Note.of(note_id, title))

    def get_all_notes(self):
        return self.__note_repository.get_notes()
