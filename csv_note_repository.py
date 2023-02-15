import csv
from pathlib import Path
import os

from note import Note
from note_repository import NoteRepository
from note_mappers import map_from_list, map_to_list


class CsvNoteRepository(NoteRepository):

    def __init__(self, csv_file_name):
        path = os.path.join(csv_file_name)
        self.__csv_file = Path(path)
        if not self.__csv_file.exists():
            with open(csv_file_name, 'w'): pass

    def record_note(self, note: Note):
        note_list = self.__read_notes(self.__csv_file)
        note_list.append(note)
        self.__write_lines(self.__csv_file, note_list)

    def find_note(self, note_id: int):
        note_list = self.__read_notes(self.__csv_file)
        return next((x for x in note_list if x.id == note_id), None)

    def delete_note(self, note_id: int):
        note_list = self.__read_notes(self.__csv_file)
        updated_list = [note for note in note_list if note.id != note_id]
        self.__write_lines(self.__csv_file, updated_list)

    def get_notes(self):
        return self.__read_notes(self.__csv_file)

    @staticmethod
    def __read_notes(file_name):
        note_list = []
        with open(file_name, newline='', encoding="utf-8") as csvfile:
            csv_reader = csv.reader(csvfile, quotechar='|')
            note_list = [map_from_list(record) for record in csv_reader]
        return note_list

    @staticmethod
    def __write_lines(file_name, note_list):
        updated_list = [map_to_list(note) for note in note_list]
        with open(file_name, 'w', newline='', encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(updated_list)


