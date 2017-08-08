from presenter import Presenter


class IView(object):
    pass


class View(IView):
    __slots__ = ['_presenter']

    def __init__(self):
        self._presenter = Presenter(self)
