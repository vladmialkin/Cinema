class ModelCustomer:
    def __init__(self, database):
        self.database = database

    def get_genres_to_dropdown(self):
        """функция получает данные всех жанров"""
        genres = self.database.get_genres()
        id_genre = []
        names = []
        for value in genres:
            id_genre.append(value[0])
            names.append(value[1])
        return names, id_genre

    def get_halls_to_dropdown(self):
        """функция получает данные всех залов"""
        halls = self.database.get_halls()
        id_halls = []
        names = []
        for value in halls:
            id_halls.append(value[0])
            names.append(value[1])
        return names, id_halls

    def get_places_to_hall_table(self, id_hall):
        """функция получает данные мест зала"""
        places = self.database.get_places(id_hall=id_hall)
        data = []

        hall = self.database.get_hall(id_hall)[0]
        size = hall[2]
        count_row = hall[3]
        if size % count_row == 0:
            count = 0
            for row in range(count_row):
                row_data = {}
                employments = []
                for index in range(int(size / count_row)):
                    employments.append(places[count][2])
                    count += 1
                dict = {"employments": employments, "place count": int(size / count_row)}
                row_data.update(dict)
                data.append(row_data)
        else:
            count = 0
            for row in range(count_row - 1):
                row_data = {}
                employments = []
                for index in range(int(size / count_row) + 1):
                    employments.append(places[count][2])
                    count += 1
                dict = {"employments": employments, "place count": int(size / count_row)}
                row_data.update(dict)
                data.append(row_data)
            employments = []
            row_data = {}
            for index in range(int(size % count_row)):
                employments.append(places[count][2])
                count += 1
            dict = {"employments": employments, "place count": int(size % count_row)}
            row_data.update(dict)
            data.append(row_data)
        return data