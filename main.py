import input_commands
from note_controller import NoteController
from csv_note_repository import CsvNoteRepository
from note_exceptions import NoRecord
from input_exception import UnknownRecord
from note_mappers import map_date_to_string

START_TITLE = 'Добро пожаловать в Заметки!'
SELECT_DESCRIPTION = f'Для создания заметки ввердите "{input_commands.CREATE}" ' \
                     f'\nДля удаления заметки введите "{input_commands.DELETE}"<Id заметки>' \
                     f'\nДля просмотра заметки введите "{input_commands.SHOW}"<Id заметки>' \
                     f'\nДля поиска заметок по дате "{input_commands.FIND_BY_DATE}"<Дата заметки>' \
                     f'\nДля вывода заметок по дате(возрастание) "{input_commands.FIND_BY_DATE_ASC}"' \
                     f'\nДля вывода заметок по дате(убывание) "{input_commands.FIND_BY_DATE_ASC}"' \
                     f'\nДля вывода всех заметок"{input_commands.ALL}"' \
                     f'\nДля редактирования заметки введите "{input_commands.EDIT}"<Id заметки>' \
                     f'\nДля выхода введите "{input_commands.EXIT}"'

note_controller = NoteController(CsvNoteRepository("file.csv"))


def start_input():

    print(START_TITLE)

    while True:
        input_value = input(SELECT_DESCRIPTION + '\n')
        try:
            if input_value == input_commands.CREATE:
                title_value = input('Добавьте тайтл: ')
                note_controller.add_note(title_value)
            if input_value == input_commands.SHOW:
                id_value = input('Введите Id заметки: ')
                print(note_controller.find_note(id_value))
            if input_value == input_commands.DELETE:
                id_value = input('Введите Id заметки: ')
                note_controller.delete_note(id_value)
            if input_value == input_commands.EDIT:
                id_value = input('Введите Id заметки: ')
                title_value = input('Добавьте тайтл: ')
                note_controller.update_note(id_value, title_value)
            if input_value == input_commands.ALL:
                [print(note) for note in note_controller.get_all_notes()]
            if input_value == input_commands.FIND_BY_DATE:
                date_value = input('Введите дату(DD-MM-YYYY): ')
                [print(note) for note in note_controller.get_all_notes() if map_date_to_string(note.date) == date_value]
            if input_value == input_commands.FIND_BY_DATE_ASC:
                note_list = note_controller.get_all_notes().sort(key=lambda x: x.date, reverse=True)
                note_list.sort(key=lambda x: x.date, reverse=True)
                [print(note) for note in note_list]
            if input_value == input_commands.FIND_BY_DATE_DESC:
                note_list = note_controller.get_all_notes().sort(key=lambda x: x.date, reverse=False)
                note_list.sort(key=lambda x: x.date, reverse=False)
                [print(note) for note in note_list]
            if input_value == input_commands.EXIT:
                return
            raise UnknownRecord()

        except NoRecord as e:
            print(f"{e}\n")
        except UnknownRecord as e:
            print(f"{e}\n")


if __name__ == '__main__':
    start_input()
