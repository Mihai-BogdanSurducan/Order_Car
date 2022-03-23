from domain.entity import Entity


class Car(Entity):
    """
    Car business object.
    """

    def __init__(self, id_car, indicator, comfort_level, card_payment, model):
        """
        Creates a car
        :param id_car: int, the card id.
        :param indicator: int, the indicator.
        :param comfort_level: str, one of 'standard', 'high', 'premium'
        :param card_payment: bool
        :param model: str, the model
        """
        super(Car, self).__init__(id_car)
        self.__indicator = indicator
        self.__comfort_level = comfort_level
        self.__card_payment = card_payment
        self.__model = model

    @property
    def indicator(self):
        return self.__indicator

    @property
    def comfort_level(self):
        return self.__comfort_level

    @property
    def card_payment(self):
        return self.__card_payment

    @property
    def model(self):
        return self.__model

    def __str__(self):
        return 'Car {}. {} - {}'.format(self.id_entity,
                                        self.indicator,
                                        self.model)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_entity

#
# c = Car(1, 24, 'fdsf', '234', '234')
# print(c == 8)
