class ModelSale:
    def __init__(self, database, film, hall):
        self.connect = database
        self.cursor = self.connect.cursor()
        self.film = film
        self.hall = hall
        self.size_hall = 0
        self.max_popular = []
        self.cursor.execute("CREATE TABLE IF NOT EXISTS sale("
                            "id_sale INTEGER PRIMARY KEY,"
                            "id_film INT,"
                            "id_hall INT,"
                            "data TEXT,"
                            "place INT"
                            ")")
        self.connect.commit()

    def insert_data(self, id_film: int, id_hall: int, data: str, place: int):
        """функция добавления данных в БД"""
        self.cursor.execute(f"INSERT INTO sale(id_film, id_hall, data, place)"
                            f"VALUES({id_film}, {id_hall}, '{data}', {place})")
        self.connect.commit()

    def get_data(self):
        """функция получения данных из БД"""
        self.cursor.execute("SELECT * FROM sale")
        data = self.cursor.fetchall()
        return data

    def get_persent(self, id_hall):
        """функция находит процент заполненности выбранного зала"""
        self.cursor.execute(f"SELECT * FROM sale WHERE id_hall={id_hall}")
        halls = self.hall.get_data()
        self.size_hall = 0
        for hall in halls:
            if id_hall == hall[0]:
                self.size_hall = hall[1]
        data = self.cursor.fetchall()
        films = self.film.get_data()
        for film in films:
            count = 0
            for value in data:
                if value[1] == film[0]:
                    count += 1
            return(film[1], count / self.size_hall * 100, '%')

    def get_popular_genre(self):
        """функция выводит самый популярный фильм"""
        sales = self.get_data()
        self.cursor.execute("SELECT * FROM film")
        films = self.cursor.fetchall()
        list_popular = []
        for film in films:
            count = 0
            for value in sales:
                if value[1] == film[0]:
                    count += 1
            list_popular.append([film[2], count])
        self.cursor.execute("SELECT * FROM film GROUP BY genre_film")
        genre = self.cursor.fetchall()
        for film in genre:
            count = 0
            for value in list_popular:
                if value[0] == film[2]:
                    count += value[1]
            self.max_popular.append([film[2], count])

    def get_max_popular(self):
        self.get_popular_genre()
        max = 0
        for value in self.max_popular:
            if max < value[1]:
                max = value[1]
        for value in self.max_popular:
            if max == value[1]:
                return (value[0])