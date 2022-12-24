class ModelFilm:
    def __init__(self, database):
        self.connect = database
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS film"
                            "("
                            "id_film INTEGER PRIMARY KEY,"
                            "name_film TEXT,"
                            "genre_film TEXT)")
        self.connect.commit()

    def insert_data(self, name_film: str, genre_film: str):
        """функция добавления данных в БД"""
        if isinstance(name_film, str) and isinstance(genre_film, str):
            self.cursor.execute(f"INSERT INTO film (name_film, genre_film) "
                                f"VALUES('{name_film}','{genre_film}')")
            self.connect.commit()

    def get_data(self):
        """функция получения данных из БД"""
        self.cursor.execute("SELECT * FROM film")
        data = self.cursor.fetchall()
        return data

