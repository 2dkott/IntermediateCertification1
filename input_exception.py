class UnknownRecord(Exception):

    def __init__(self):
        super().__init__(f'Введена неопознаная комманда!')
