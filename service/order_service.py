from domain.order import Order
from domain.order_viewmodel import OrderViewModel


class OrderService:

    """
    Manages location logic.
    """

    def __init__(self, order_repository, car_repository, location_repository):
        """
        Creates a location service.
        """
        self.__order_repository = order_repository
        self.__car_repository = car_repository
        self.__location_repository = location_repository

    def add_order(self, id_order, id_car, id_location, final_time, km_cost, distance, status):

        if self.__car_repository.read(id_car) is None:
            raise ValueError('Nu exista nicio masina cu id-ul: ' + id_car)
        if self.__location_repository.read(id_location) is None:
            raise ValueError('Nu exista nicio locatie cu id-ul: ' + id_location)

        order = Order(id_order, id_car, id_location, final_time, km_cost, distance, status)
        #self.__validator.validate(location)
        self.__order_repository.create(order)

    def get_all(self):
        """
        :return: a list of all the orders, containing Car and Location objects.
        """
        orders = self.__order_repository.read()
        viewmodels = []
        for order in orders:
            order_viewmodel = OrderViewModel(
                order,
                self.__car_repository.read(order.id_car),
                self.__location_repository.read(order.id_location)
            )
            viewmodels.append(order_viewmodel)
        return viewmodels

    def get_streets_ordered_desc_by_max_distances(self):
        """
        ...
        :return:
        """
        street_max_dist = {}
        for order in self.__order_repository.read():
            location = self.__location_repository.read(order.id_location)
            street = location.street_name
            if street in street_max_dist:
                street_max_dist[street] = max(
                    street_max_dist[street],
                    order.distance
                )
            else:
                street_max_dist[street] = order.distance

        # TODO: also return the max distance, using a view model
        return sorted(street_max_dist.keys(),
                      key=lambda street: street_max_dist[street],
                      reverse=True)
