from database import Database
from presenters import Manager
from presenters import Customer
from presenters import Sessions


class Core:
    def __init__(self, page):
        self.page = page
        self.database = Database()
        self.sessions_presenter = Sessions(database=self.database, page=page)
        self.page.scroll = True
        #self.page.on_route_change = self.on_route_change
        self.page.views.append(self.sessions_presenter.view)
        self.page.update()

    def insert_views(self, views: list):
        self.page.views.clear()
        for view in views:
            self.page.views.append(view)

    """
    def on_route_change(self, route):
        """"""функция изменяет view""""""
        for view in self.page.views:
            if view.route == route.route:
                view = self.page.views[-1]
                self.page.views.pop()
                self.page.views.insert(0, view)
                break
    """

