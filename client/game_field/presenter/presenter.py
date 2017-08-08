from model import Model
from view import IView


class IPresenter(object):
    def button_clicked(self) -> None:
        raise NotImplementedError

    def mouse_moved(self) -> None:
        raise NotImplementedError

    def mouse_downed(self) -> None:
        raise NotImplementedError

    def mouse_upped(self) -> None:
        raise NotImplementedError


class Presenter(IPresenter):
    __slots__ = ['_view', '_model']

    def __init__(self, view: IView) -> None:
        self._view = view
        self._model = Model()
