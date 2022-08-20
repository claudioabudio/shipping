import iso6346


class ShippingContainer:
    next_serial = 1337

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6))

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, items, **kwargs):
        return cls(owner_code, contents=list(items), **kwargs)

    def __init__(self, owner_code, contents, **kwargs):
        self.contents = contents
        self.owner_code = owner_code
        self.bic = self._make_bic_code(
            owner_code,
            ShippingContainer._generate_serial())


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, celsius):
        if celsius > self.MAX_CELSIUS:
            raise ValueError("Temperature too hot !")
        super().__init__(owner_code, contents)
        self.celsius = celsius

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category='R')
