import inspect

def auto_repr(cls):
    members = vars(cls)
    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} already defines __repr__")
    if "__init__" not in members:
        raise TypeError(f"{cls.__name__} does not override __init__")

    sig = inspect.signature(cls.__init__)
    parameter_names = list(sig.parameters)[1:]
    if not all(
            isinstance(members.get(name, None), property) for name in parameter_names
        ):
        raise TypeError(f"can not apply auto_repr to {cls.__name__} because not all "
                        "__init__ parameters have a corresponding property")

    def synthesized_repr(self):
        return "{typename}({args})".format(
            typename=type(self).__name__,
            args=", ".join(
               "{name}={value!r}".format(
                   name=name2,
                   value=getattr(self, name2)
               ) for name2 in parameter_names
            )
        )

    setattr(cls, "__repr__", synthesized_repr)
    return cls



@auto_repr
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

    # def __repr__(self):
    #     return f"{type(self).__name__}(name={self.name}, position={self.position})"

    def __str__(self):
        return self.name
