import flet


class ViewSessions(flet.View):
    def __init__(self):
        super().__init__()
        self.vertical_alignment = 'center'
        self.column = flet.Column()
        self.column.horizontal_alignment = 'center'
        self.column.alignment = 'center'
        self.information_text = flet.Text("Выбор сеанса", size=40, weight='bold')
        self.sessions_row = flet.Row(spacing=50)
        self.sessions_row.alignment = 'center'
        self.append_widgets(self.column, [self.information_text, self.sessions_row])
        self.controls.append(self.column)

    def create_sessions(self, data_sessions, session_on_click):
        """функция создает отображение сеансов"""
        for session in data_sessions:
            container = flet.Container(content=flet.Text(session[1], size=24, weight='bold'),
                                       bgcolor=flet.colors.BLUE_100,
                                       border=flet.border.all(2.0, flet.colors.BLACK),
                                       border_radius=flet.border_radius.all(30.0),
                                       padding=flet.padding.all(20.0),
                                       on_click=session_on_click)
            container.data = {'session_id': session[0]}
            self.sessions_row.controls.append(container)

    @staticmethod
    def append_widgets(widget, append_widgets: list):
        if isinstance(append_widgets, list):
            for value in append_widgets:
                widget.controls.append(value)
