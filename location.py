class Location:
    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name}, position={self.position})"

    def __str__(self):
        return self.name
