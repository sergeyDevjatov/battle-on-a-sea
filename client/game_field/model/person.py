

class Person(object):
    __slots__ = ['shots']

    def __init__(self) -> None:
        self.shots = set()
