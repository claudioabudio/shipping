class ShippingContainer:
    next_serial = 1337

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    def __init__(self, owner_code, contents):
        self.contents = contents
        self.owner_code = owner_code
        self.serial = ShippingContainer._generate_serial()
    