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

    def __init__(self, owner_code, contents):
        self.contents = contents
        self.owner_code = owner_code
        self.bic = ShippingContainer._make_bic_code(
            owner_code,
            ShippingContainer._generate_serial())
    