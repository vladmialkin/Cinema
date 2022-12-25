import flet


class ModelSession:
    def __init__(self, database):
        self.database = database

    def get_sessions(self):
        """функция получает данные всех сеансов"""
        return self.database.get_sessions()




