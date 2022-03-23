from domain.entity import Entity


class Order(Entity): # Order mosteneste pe Entity

    def __init__(self, id_order, id_car, id_location, final_time, km_cost, distance, status):
        super().__init__(id_order)
        self.__id_car = id_car
        self.__id_location = id_location
        self.__final_time = final_time
        self.__km_cost = km_cost
        self.__distance = distance
        self.__status = status

    @property
    def id_car(self):
        return self.__id_car

    @property
    def id_location(self):
        return self.__id_location

    @property
    def final_time(self):
        return self.__final_time

    @property
    def km_cost(self):
        return self.__km_cost

    @property
    def distance(self):
        return self.__distance

    @property
    def status(self):
        return self.__status

    def __str__(self):
        return '{}. location: {} - car: {}'.format(self.id_entity, self.id_location, self.id_car)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_entity
