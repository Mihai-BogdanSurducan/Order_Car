from domain.entity import Entity


class Location(Entity):

    def __init__(self, id_location, street_name, number, block, building, notes):
        super().__init__(id_location)
        self.__street_name = street_name
        self.__number = number
        self.__block = block
        self.__building = building
        self.__notes = notes

    @property
    def street_name(self):
        return self.__street_name

    @property
    def number(self):
        return self.__number

    @property
    def block(self):
        return self.__block

    @property
    def building(self):
        return self.__building

    @property
    def notes(self):
        return self.__notes

    def __str__(self):
        return '{}. {}, {}'.format(self.id_entity, self.street_name, self.number)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_location
