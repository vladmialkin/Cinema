from models import ModelSession
from views import ViewSessions


class Sessions:
    def __init__(self, database, page):
        self.database = database
        self.page = page
        self.model = ModelSession(self.database)
        self.view = ViewSessions()
        self.create_sessions()

    def create_sessions(self):
        """функция создания отображения сеансов"""
        data_sessions = self.model.get_sessions()
        self.view.create_sessions(data_sessions=data_sessions, session_on_click=self.session_on_click)

    def session_on_click(self, event):
        """функция нажатия на сеанс"""
        print(event.control.data)
