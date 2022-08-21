import iso6346


class ShippingContainer:
    next_serial = 1337

    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

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
    def create_empty(cls, owner_code, length_ft):
        return cls(owner_code, length_ft, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), **kwargs)

    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.contents = contents
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.bic = self._make_bic_code(
            owner_code,
            ShippingContainer._generate_serial())

    @property
    def volume_ft3(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > self.MAX_CELSIUS:
            raise ValueError("Temperature too hot !")
        self._celsius = value

    @property
    def volume_ft3(self):
        return super().volume_ft3 - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category='R')


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):
    MIN_CELSIUS = -20

