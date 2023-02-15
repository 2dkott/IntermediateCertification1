class NoRecord(Exception):

    def __init__(self, note_id: str):
        super().__init__(f'Заметка (Id: {note_id}) не найдена!')
