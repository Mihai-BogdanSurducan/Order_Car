class OrderViewModel:

    def __init__(self, order, car, location):

        self.order = order
        self.car = car
        self.location = location

    def __str__(self):
        return '{}. car: {} -- location: {}'.format(
            self.order.id_entity,
            self.car,
            self.location
        )

