from presenter import Presenter


class IView(object):
    def active_mouse_button(self) -> tuple:
        raise NotImplementedError


class View(IView):
    __slots__ = ['_presenter']

    def __init__(self) -> None:
        self._presenter = Presenter(self)

