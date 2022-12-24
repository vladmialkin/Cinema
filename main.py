from core import Core
import flet


def main(page: flet.Page):
    Core(page=page)


flet.app(target=main, view=flet.FLET_APP, port=5211)
