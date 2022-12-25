from views import ViewCustomer
from models import ModelCustomer


class Customer:
    def __init__(self, database, page, session_id):
        self.database = database
        self.page = page
        self.session_id = session_id
        self.model = ModelCustomer(self.database)
        self.view = ViewCustomer()

        self.view.save_button.on_click = self.save_button_on_click
        self.view.cansel_button.on_click = self.cansel_button_on_click

        self.view.hall_dropdown.on_change = self.hall_on_change

        self.insert_dropdowns()
        self.create_tables(place_on_click=self.place_on_click, hall_id=self.view.hall_dropdown.value[-1])

    def create_tables(self, place_on_click, hall_id):
        """функция созадния таблицы"""
        id_hall = self.view.hall_dropdown.value[-1]
        data = self.model.get_places_to_hall_table(id_hall=id_hall, session_id=self.session_id)
        self.view.create_hall_place_table(data=data, place_on_click=place_on_click, hall_id=hall_id)
        self.view.create_sale_table()
        self.page.update()

    def insert_dropdowns(self):
        """функция заполняет данными выпадающие списки"""
        names_halls, id_halls = self.model.get_halls_to_dropdown(session_id=self.session_id)
        self.view.insert_dropdowns(dropdown=self.view.hall_dropdown, values=names_halls, data=id_halls)
        names_genres, id_genres = self.model.get_genres_to_dropdown()
        self.view.insert_dropdowns(dropdown=self.view.genre_dropdown, values=names_genres, data=id_genres)
        hall_id = self.view.hall_dropdown.value[-1]
        names_films, id_films = self.model.get_films_to_dropdown(session_id=self.session_id, hall_id=hall_id)
        self.view.insert_dropdowns(dropdown=self.view.film_dropdown, values=names_films, data=id_films)

    def place_on_click(self, event):
        """функция нажатия на выбранное место в зале"""
        data = event.control.data
        place = data.get("place")
        if event.control.bgcolor is self.view.blue_color:
            event.control.bgcolor = self.view.yellow_color
            session_start, session_time = self.model.get_session_to_hall_table(self.session_id)
            new_data = [self.view.hall_dropdown.value, self.view.film_dropdown.value, place, session_start]
            self.view.create_row_sale_table(new_data)
        elif event.control.bgcolor is self.view.yellow_color:
            for index, table_row in enumerate(self.view.sales_table.rows):
                if table_row.cells[2].content.value == place:
                    self.view.sales_table.rows.pop(index)
                    event.control.bgcolor = self.view.blue_color
        self.page.update()

    def save_button_on_click(self, event):
        """функция подтверждения покупки"""
        place = []
        for row in self.view.sales_table.rows:
            place.append(row.data[2])
            film_id = self.model.get_film_for_name(name=row.data[1])

            self.model.create_sale(hall_id=row.data[0][-1], place=row.data[2], session_id=self.session_id,
                                   film_id=film_id)
            self.model.update_place(session_id=self.session_id, hall_id=row.data[0][-1], number=row.data[2])
        self.view.sales_table.rows.clear()
        place.sort()
        for row in self.view.hall_place_table.controls:
            for container in row.controls:
                if container.data.get("place") in place:
                    container.bgcolor = self.view.red_color
        self.page.update()

    def cansel_button_on_click(self, event):
        """функция отмены покупки билетов"""
        place = []
        for row in self.view.sales_table.rows:
            place.append(row.data[2])
        self.view.sales_table.rows.clear()
        place.sort()
        for row in self.view.hall_place_table.controls:
            for container in row.controls:
                if container.data.get("place") in place:
                    container.bgcolor = self.view.blue_color
        self.page.update()

    def hall_on_change(self, event):
        """функция изменяет зал на выбранный"""
        self.view.hall_dropdown.value = event.data
        self.view.film_dropdown.options.clear()
        hall_id = self.view.hall_dropdown.value[-1]
        names_films, id_films = self.model.get_films_to_dropdown(session_id=self.session_id, hall_id=hall_id)
        self.view.insert_dropdowns(dropdown=self.view.film_dropdown, values=names_films, data=id_films)
        self.create_tables(place_on_click=self.place_on_click, hall_id=self.view.hall_dropdown.value[-1])
