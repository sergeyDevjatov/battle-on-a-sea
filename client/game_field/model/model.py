from person import Person


class Model(object):
    __slots__ = ['player', 'enemy']

    def __init__(self):
        self.player = Person()
        self.enemy = Person()
