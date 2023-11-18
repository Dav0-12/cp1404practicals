"""Band class definition"""


class Band:
    def __init__(self, name=""):
        """Construct a Band with a name and an empty list of Musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        band_string = f"{self.name} "
        musician_strings = []
        for musician in self.musicians:
            musician_strings.append(f"{musician.name} ({musician.instruments})")
        band_string += f'({", ".join(musician_strings)})'
        return band_string

    def add(self, musician):
        """Add a musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Returns the instrument each band member is playing."""
        band_string = ""
        for musician in self.musicians:
            if not musician.instruments:
                band_string += f"{musician.name} needs an instrument!\n"
            else:
                band_string += f"{musician.name} is playing: {musician.instruments[0]}\n"
        return band_string
