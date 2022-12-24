import flet
from database import Database
from presenters import Manager
from presenters import Customer


class Core:
    def __init__(self, page):
        self.page = page
        self.database = Database()
        self.manager_presenter = Manager(database=self.database, page=page)
        self.customer_presenter = Customer(database=self.database, page=page)
        self.page.scroll = True

        self.page.views.append(self.customer_presenter.view)
        self.page.update()




