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
        self.session_id = None
        #self.insert_hall(name_hall="Зал 2", size_hall=40, rows=6)
        #self.insert_genre(genre_name="Драма")

    def connect_to_db(self):
        try:
            self.database = mysql.connector.connect(
                user='admi',
                password='admin',
                host='172.17.0.2',
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
                            "session_id INT,"
                            "number INT,"
                            "PRIMARY KEY (id))")
        self.database.commit()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS genre("
                            "id INT NOT NULL AUTO_INCREMENT,"
                            "name TEXT,"
                            "PRIMARY KEY (id))")
        self.database.commit()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS film("
                            "id INT NOT NULL AUTO_INCREMENT,"
                            "name TEXT,"
                            "genre_id int,"
                            "PRIMARY KEY (id))")
        self.database.commit()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS session("
                            "id INT NOT NULL AUTO_INCREMENT,"
                            "TIME TEXT,"
                            "PRIMARY KEY (id))")
        self.database.commit()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS session_information("
                            "id INT NOT NULL AUTO_INCREMENT,"
                            "session_id INT,"
                            "hall_id INT,"
                            "film_id INT,"
                            "PRIMARY KEY (id))")
        self.database.commit()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS sale("
                            "id INT NOT NULL AUTO_INCREMENT,"
                            "hall_id INT,"
                            "place INT,"
                            "session_id INT,"
                            "film_id INT,"
                            "PRIMARY KEY (id))")
        self.database.commit()

    def get_halls(self, session_id):
        """функция получения списка залов"""
        self.cursor.execute(f"SELECT DISTINCT hall.id, hall.name, hall.size_hall, count_row FROM hall "
                            f"LEFT JOIN session_information "
                            f"ON hall.id = session_information.hall_id "
                            f"WHERE session_information.session_id = {session_id}")
        values = self.cursor.fetchall()
        return values

    def get_hall(self, hall_id: int):
        """функция получает данные зала"""
        self.cursor.execute(f"SELECT * FROM hall WHERE id={hall_id}")
        values = self.cursor.fetchall()
        return values

    def insert_hall(self, name_hall: str, size_hall: int, rows: int, session_id: int):
        """функция добавляет новый зал в БД"""
        if isinstance(size_hall, int):
            self.cursor.execute(f"INSERT INTO hall(name, size_hall, count_row) "
                                f"VALUES('{name_hall}',{size_hall},{rows})")
            self.database.commit()
            self.cursor.execute("SELECT id FROM hall")
            values = self.cursor.fetchall()
            id_last_hall = values[-1][0]
            for index in range(size_hall):
                self.cursor.execute(f"INSERT INTO places(id_hall, employment, session_id) "
                                    f"VALUES({id_last_hall},{0}, {session_id})")
                self.database.commit()

    def insert_genre(self, genre_name: str):
        """функция добавляет новый жанр в БД"""
        self.cursor.execute(f"INSERT INTO genre(name) "
                            f"VALUES('{genre_name}')")
        self.database.commit()

    def get_genres(self):
        """функция получает данные жанров"""
        self.cursor.execute(f"SELECT * FROM genre")
        values = self.cursor.fetchall()
        return values

    def get_places(self, id_hall: int, session_id):
        """функция получает данные мест зала"""
        self.cursor.execute(f"SELECT * FROM places WHERE id_hall={id_hall} and session_id={session_id}")
        values = self.cursor.fetchall()
        return values

    def insert_film(self, name_film: str, genre_id: int):
        """функция добавляет новый фильс в БД"""
        self.cursor.execute(f"INSERT INTO film(name, genre_id) "
                            f"VALUES('{name_film}',{genre_id})")
        self.database.commit()

    def get_film_for_name(self, name: str):
        """функция получает данные фильма по его значениям"""
        self.cursor.execute(f"SELECT * FROM film WHERE name='{name}'")
        values = self.cursor.fetchone()
        return values

    def get_films(self, session_id, hall_id):
        """функция получает данные всех фильмов"""
        self.cursor.execute(f"SELECT DISTINCT film.id, film.name, film.genre_id FROM film "
                            f"LEFT JOIN session_information "
                            f"ON film.id = session_information.film_id "
                            f"WHERE session_information.session_id = {session_id} and "
                            f"session_information.hall_id = {hall_id}")
        values = self.cursor.fetchall()
        return values

    def insert_session(self, time: str):
        """функция добавляет новую сессию в БД"""
        self.cursor.execute(f"INSERT INTO session(time) "
                            f"VALUES('{time}')")
        self.database.commit()

    def get_session(self, session_id: int):
        """функция получает данные сеанса по id"""
        self.cursor.execute(f"SELECT * FROM session " 
                            f"WHERE id = {session_id}")
        values = self.cursor.fetchone()
        return values

    def get_sessions(self):
        """функция получает данные всех фильмов"""
        self.cursor.execute(f"SELECT * FROM session")
        values = self.cursor.fetchall()
        return values

    def insert_session_information(self, session_id: int, hall_id: int, film_id: int):
        """функция добавляет новые данные сессий в БД"""
        self.cursor.execute(f"INSERT INTO session_information(session_id, hall_id, film_id) "
                            f"VALUES({session_id},{hall_id},{film_id})")
        self.database.commit()

    def get_sessions_information(self):
        """функция получает данные всей информации о сессиях"""
        self.cursor.execute(f"SELECT * FROM session_information")
        values = self.cursor.fetchall()
        return values

    def create_sale(self, hall_id: int, place: int, session_id: int, film_id: int):
        """функция создает продажу билета"""
        self.cursor.execute(f"INSERT INTO sale(hall_id, place, session_id, film_id) "
                            f"VALUES({hall_id},{place},{session_id}, {film_id})")
        self.database.commit()

    def update_employment_place(self, session_id: int, hall_id: int, number: int):
        """функция изменяет место на занятое"""
        self.cursor.execute(f"UPDATE places SET "
                            f"employment = 1 WHERE "
                            f"id_hall = {hall_id} and session_id = {session_id} and number = {number}")
        self.database.commit()
