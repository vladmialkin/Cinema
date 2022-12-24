import flet


class ViewCustomer(flet.View):
    def __init__(self):
        super().__init__()
        self.row_dropdowns = flet.Row()
        self.horizontal_alignment = "center"
        self.blue_color = flet.colors.BLUE
        self.red_color = flet.colors.RED
        self.yellow_color = flet.colors.YELLOW

        self.hall_dropdown = flet.Dropdown()
        self.genre_dropdown = flet.Dropdown()
        self.film_dropdown = flet.Dropdown()

        self.append_widgets(widget=self.row_dropdowns,
                            append_widgets=[self.hall_dropdown, self.genre_dropdown, self.film_dropdown])

        self.hall_place_table = flet.Column()

        self.sales_column = flet.Column(height=400)
        self.sales_column.scroll = True
        self.sales_column.horizontal_alignment = "center"

        self.sales_table = flet.DataTable(width=700)

        self.buttons_row = flet.Row()
        self.buttons_row.alignment = "center"
        self.save_button = flet.ElevatedButton(content=flet.Text(value="Подтвердить",
                                                             size=20,
                                                             weight="bold"))
        self.cansel_button = flet.ElevatedButton(content=flet.Text(value="Отмена",
                                                               size=20,
                                                               weight="bold"))

        self.append_widgets(self.buttons_row, [self.save_button, self.cansel_button])

        self.sales_column.controls.append(self.sales_table)
        self.append_widgets(widget=self, append_widgets=[self.row_dropdowns,
                                                         self.hall_place_table,
                                                         self.sales_column,
                                                         self.buttons_row])

    @staticmethod
    def insert_dropdowns(dropdown: flet.Dropdown, values: list, data):
        """функция заполняет выпадающий список значениями"""
        for index, value in enumerate(values):
            option = flet.dropdown.Option(value)
            option.data = data[index]
            dropdown.options.append(option)
        dropdown.value = dropdown.options[0].key

    def create_hall_place_table(self, data: list, place_on_click, hall_id: int):
        """функция создания таблицы"""
        self.hall_place_table.controls.clear()
        place_count = 1
        for index, value in enumerate(data):
            employments = data[index].get("employments")
            places = data[index].get("place count")
            place_count, row = self.create_row_hall_place_table(places=places,
                                                                employments=employments,
                                                                place_on_click=place_on_click,
                                                                place_count=place_count,
                                                                hall_id=hall_id)
            self.hall_place_table.controls.append(row)

    @staticmethod
    def create_row_hall_place_table(places: int, employments: list, place_on_click, place_count: int, hall_id: int):
        """функция создает ряд таблицы"""
        row = flet.Row()
        for index in range(places):
            container = flet.Container(width=75, height=75, content=flet.Text(value=str(place_count),
                                                                              weight="bold",
                                                                              size=20,
                                                                              text_align="center"))
            container.alignment = flet.alignment.center
            if employments[index] == 1:
                container.bgcolor = flet.colors.RED
            else:
                container.bgcolor = flet.colors.BLUE
            container.data = {
                "place": place_count,
                "hall": hall_id
            }
            container.on_click = place_on_click
            row.controls.append(container)
            place_count += 1
        return place_count, row

    def create_sale_table(self):
        """функция создания таблицы продаж"""
        self.sales_table.columns = [
            flet.DataColumn(flet.Text("Зал", size=20)),
            flet.DataColumn(flet.Text("Фильм", size=20)),
            flet.DataColumn(flet.Text("Место", size=20)),
            flet.DataColumn(flet.Text("Начало фильма", size=20))
        ]

    def create_row_sale_table(self, data):
        """функция создания строки таблицы с данными по продаже"""
        row = flet.DataRow(selected=False)
        cells = []
        for value in data:
            cell = flet.DataCell(flet.Text(value, size=18))
            cells.append(cell)
        row.cells = cells
        row.data = data
        self.sales_table.rows.append(row)

    @staticmethod
    def append_widgets(widget, append_widgets: list):
        if isinstance(append_widgets, list):
            for value in append_widgets:
                widget.controls.append(value)
