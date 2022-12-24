from views import ViewManager


class Manager:
    def __init__(self, database, page):
        self.database = database
        self.page = page
        self.view = ViewManager()
