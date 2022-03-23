from repository.repository_error import RepositoryError


class LocationInMemoryRepository:
    '''
    Repository for storing data in memory
    '''

    def __init__(self):
        '''
        Creates an in memory repository.
        '''
        self.__storage = {}

    # metode CRUD
    # CRUD = Create
    #        Read
    #        Update
    #        Delete

    def create(self, location):
        '''
        Adds a new location.
        :param location: the given location
        :return: -
        :raises: KeyError if the id already exists
        '''
        location_id = location.id_location
        if location_id in self.__storage:
            raise RepositoryError('The location id already exists!')
        self.__storage[location_id] = location

    def read(self, location_id=None):
        '''
        Gets a location by id or all the locations
        :param location_id: optional, the location id
        :return: the list of locations or the location with the given id
        '''
        if location_id is None:
            return self.__storage.values()

        if location_id in self.__storage:
            return self.__storage[location_id]
        return None

    def update(self, location):
        '''
        Updates location.
        :param location: the location to update
        :return: -
        :raises: KeyError if the id does not exist
        '''
        location_id = location.id_location
        if location_id not in self.__storage:
            raise RepositoryError('There is no location with that id!')
        self.__storage[location_id] = location

    def delete(self, location_id):
        '''
        Deletes a location.
        :param location_id: the location id to delete.
        :return: -
        :raises KeyError: if no location with location_id
        '''
        if location_id not in self.__storage:
            raise RepositoryError('There is no location with that id!')
        del self.__storage[location_id]

    def clear(self):
        self.__storage.clear()
