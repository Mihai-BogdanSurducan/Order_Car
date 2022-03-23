from domain.location import Location


class LocationService:

    """
    Manages location logic.
    """

    def __init__(self, repository):
        """
        Creates a location service.
        """
        self.__repository = repository

    def add_location(self, id_location, street_name, number, block, building, notes):
        location = Location(id_location, street_name, number, block, building, notes)
        #self.__validator.validate(location)
        self.__repository.create(location)

    def get_all(self):
        """
        :return: a list of all the cars.
        """
        return self.__repository.read()

    def get_sorted_desc_by_notes_length(self):
        return sorted(self.get_all(),
                      key=lambda location: len(location.notes),
                      reverse=True)