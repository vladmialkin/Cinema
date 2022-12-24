from views import ViewCustomer
from models import ModelCustomer


class Customer:
    def __init__(self, database, page):
        self.database = database
        self.page = page
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
        data = self.model.get_places_to_hall_table(id_hall)
        self.view.create_hall_place_table(data=data, place_on_click=place_on_click, hall_id=hall_id)
        self.view.create_sale_table()
        self.page.update()

    def insert_dropdowns(self):
        """функция заполняет данными выпадающие списки"""
        names_halls, id_halls = self.model.get_halls_to_dropdown()
        self.view.insert_dropdowns(dropdown=self.view.hall_dropdown, values=names_halls, data=id_halls)
        names_genres, id_genres = self.model.get_genres_to_dropdown()
        self.view.insert_dropdowns(dropdown=self.view.genre_dropdown, values=names_genres, data=id_genres)


    def place_on_click(self, event):
        """функция нажатия на выбранное место в зале"""
        data = event.control.data
        place = data.get("place")
        if event.control.bgcolor is self.view.blue_color:
            event.control.bgcolor = self.view.yellow_color
            new_data = [1, "Гарри Потный", place, "20:12"]
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
        self.create_tables(place_on_click=self.place_on_click, hall_id=self.view.hall_dropdown.value[-1])
