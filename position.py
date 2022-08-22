class Position:
    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= 90):
            raise ValueError(f"Latitude {latitude} out of range !")
        if not (-180 <= longitude <= 180):
            raise ValueError(f"Longitude {longitude} out of range !")
        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    def __repr__(self):
        return f"{type(self).__name__}(latitude={self.latitude}, longitude={self.longitude})"

    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude > 0 else "S"

    @property
    def longitude_hemisphere(self):
        return "E" if self.longitude > 0 else "W"

    def __str__(self):
        return f"{abs(self.latitude)}º {self.latitude_hemisphere}, {abs(self.longitude)}º {self.longitude_hemisphere}"

    def __format__(self, format_spec):
        component_format_spec = ".2f"
        prefix, dot, suffix = format_spec.partition(".")
        if dot:
            num_decimals = int(suffix)
            component_format_spec = f".{num_decimals}f"
        return (f"{format(abs(self.latitude), component_format_spec)}º {self.latitude_hemisphere} "
                f"{format(abs(self.longitude), component_format_spec)}º {self.longitude_hemisphere}")
