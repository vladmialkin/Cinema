import mysql.connector
from models import ModelFilm
from models import ModelHall
from models import ModelSale


class Database:
    def __init__(self):
        self.database = None
        self.cursor = None
        self.connect_to_db()
        self.create_tables()
        #self.insert_hall(name_hall="Зал 2", size_hall=40, rows=6)
        #self.insert_genre(genre_name="Драма")

    def connect_to_db(self):
        try:
            self.database = mysql.connector.connect(
                user='admi',
                password='admin',
                host='172.17.0.3',
                database='intership',
                port='3306'
            )
            self.cursor = self.database.cursor()

        except Exception as e:
            print(e)

    def create_tables(self):
        """функции создания таблиц БД"""
        self.cursor.execute("CREATE TABLE IF NOT EXISTS hall("
                            "id INT NOT NULL AUTO_INCREMENT,"
                            "name TEXT,"
                            "size_hall INT,"
                            "count_row INT,"
                            "PRIMARY KEY (id))")
        self.database.commit()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS places("
                            "id INT NOT NULL AUTO_INCREMENT,"
                            "id_hall INT,"
                            "employment INT,"
                            "PRIMARY KEY (id))")
        self.database.commit()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS genre("
                            "id INT NOT NULL AUTO_INCREMENT,"
                            "name TEXT,"
                            "PRIMARY KEY (id))")
        self.database.commit()

    def get_halls(self):
        """функция получения списка залов"""
        self.cursor.execute("SELECT * FROM hall")
        values = self.cursor.fetchall()
        return values

    def get_hall(self, hall_id):
        """функция получает данные зала"""
        self.cursor.execute(f"SELECT * FROM hall WHERE id={hall_id}")
        values = self.cursor.fetchall()
        return values

    def insert_hall(self, name_hall: str, size_hall: int, rows: int):
        """функция добавляет новый зал в БД"""
        if isinstance(size_hall, int):
            self.cursor.execute(f"INSERT INTO hall(name, size_hall, count_row) "
                                f"VALUES('{name_hall}',{size_hall},{rows})")
            self.database.commit()
            self.cursor.execute("SELECT id FROM hall")
            values = self.cursor.fetchall()
            id_last_hall = values[-1][0]
            for index in range(size_hall):
                self.cursor.execute(f"INSERT INTO places(id_hall, employment) "
                                    f"VALUES({id_last_hall},{0})")
                self.database.commit()

    def insert_genre(self, genre_name):
        """функция добавляет новый жанр в БД"""
        self.cursor.execute(f"INSERT INTO genre(name) "
                            f"VALUES('{genre_name}')")
        self.database.commit()

    def get_genres(self):
        """функция получает данные жанров"""
        self.cursor.execute(f"SELECT * FROM genre")
        values = self.cursor.fetchall()
        return values

    def get_places(self, id_hall):
        """функция получает данные мест зала"""
        self.cursor.execute(f"SELECT * FROM places WHERE id_hall={id_hall}")
        values = self.cursor.fetchall()
        return values
