from models import ModelSession
from views import ViewSessions
from presenters import Manager
from presenters import Customer


class Sessions:
    def __init__(self, database, page):
        self.database = database
        self.page = page
        self.model = ModelSession(self.database)
        self.view = ViewSessions()
        self.create_sessions()
        self.manager_presenter = None
        self.customer_presenter = None

    def create_sessions(self):
        """функция создания отображения сеансов"""
        data_sessions = self.model.get_sessions()
        self.view.create_sessions(data_sessions=data_sessions, session_on_click=self.session_on_click)

    def session_on_click(self, event):
        """функция нажатия на сеанс"""
        data = event.control.data
        session_id = data.get("session_id")
        self.manager_presenter = Manager(database=self.database, page=self.page)
        self.customer_presenter = Customer(database=self.database, page=self.page, session_id=session_id)
        self.page.views.append(self.customer_presenter.view)
        self.page.update()
