class Musician:
    instruments = ["guitar", "bass", "drums"]
    solos = ["face melting guitar solo", "bom bom buh bom", "rattle boom crash"]

    def __init__(self, name):
        self.name = name

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def get_instrument(self):
        pass

    def play_solo(self):
        pass


class Guitarist(Musician):
    instrument = Musician.instruments[0]
    solos = Musician.solos[0]

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solos


class Bassist(Musician):
    instrument = Musician.instruments[1]
    solos = Musician.solos[1]

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solos


class Drummer(Musician):
    instrument = Musician.instruments[2]
    solos = Musician.solos[2]

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solos


class Band(Musician):
    membersList = []
    instances = []

    def __init__(self, name, members):
        super().__init__(name)
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        for member in self.members:
            Band.membersList.append(member.play_solo())
        return Band.membersList

    @classmethod
    def to_list(cls):
        return cls.instances

    def __str__(self):
        pass

    def __repr__(self):
        pass