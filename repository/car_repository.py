from domain.car import Car


class CarInMemoryRepository:
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

    def create(self, car):
        '''
        Adds a new car.
        :param car: the given car
        :return: -
        :raises: KeyError if the id already exists
        '''
        car_id = car.id_car
        if car_id in self.__storage:
            raise KeyError('The car id already exists!')
        self.__storage[car_id] = car

    def read(self, car_id=None):
        '''
        Gets a car by id or all the cars
        :param car_id: optional, the car id
        :return: the list of cars or the car with the given id
        '''
        if car_id is None:
            return self.__storage.values()

        if car_id in self.__storage:
            return self.__storage[car_id]
        return None

    def update(self, car):
        '''
        Updates car.
        :param car: the car to update
        :return: -
        :raises: KeyError if the id does not exist
        '''
        car_id = car.id_car
        if car_id not in self.__storage:
            raise KeyError('There is no car with that id!')
        self.__storage[car_id] = car

    def delete(self, car_id):
        '''
        Deletes a car.
        :param car_id: the car id to delete.
        :return: -
        :raises KeyError: if no car with car_id
        '''
        if car_id not in self.__storage:
            raise KeyError('There is no car with that id!')
        del self.__storage[car_id]

    def clear(self):
        self.__storage.clear()


# def test_CarInMemoryRepository():
#     r = CarInMemoryRepository()
#     v1 = Car(1, '234', 'high', True, 'fdsa')
#     v2 = Car(2, '234', 'high', True, 'fdsa')
#     r.create(v1)
#     r.create(v2)
#
#     assert len(r.read()) == 2
#     r.update(Car(2, '1111', 'high', True, 'fdsa'))
#     updated_v = r.read(2)
#     assert updated_v.indicator == '1111'
#
#     r.delete(1)
#     assert len(r.read()) == 1
#     assert r.read(1) == None
#
#
# test_CarInMemoryRepository()
