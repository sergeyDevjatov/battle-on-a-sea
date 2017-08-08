

class Shot(object):
    __slots__ = ['column', 'row', 'hit']

    def __init__(self, column: int, row: int, hit: bool) -> None:
        self.column = column
        self.row = row
        self.hit = hit
