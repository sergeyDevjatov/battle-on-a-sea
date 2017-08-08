from model import Model


class IPresenter(object):
    pass


class Presenter(IPresenter):
    __slots__ = ['_view', '_model']

    def __init__(self, view):
        self._view = view
        self._model = Model()
