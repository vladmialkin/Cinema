class ModelHall:
    def __init__(self, database):
        self.connect = database
        self.cursor = self.connect.cursor()

    def insert_data(self, size_hall: int):
        """функция добавления данных в БД"""
        if isinstance(size_hall, int):
            self.cursor.execute(f"INSERT INTO hall (size_hall) VALUES({size_hall})")
            self.connect.commit()

    def get_data(self):
        """функция получения данных из БД"""
        self.cursor.execute("SELECT * FROM hall")
        data = self.cursor.fetchall()
        return data
