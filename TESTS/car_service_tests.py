from domain.car import Car
from service.car_service import CarService


def test_car_service():

    car_service = CarService()
    car = Car(1, 12, 'premium', True, 'e46')
    car_service.add_car(car.id_entity,
                        car.indicator,
                        car.comfort_level,
                        car.card_payment,
                        car.model)
    assert car_service.get_all() == [car]

    try:
        car_service.add_car(car.id_entity,
                            car.indicator,
                            car.comfort_level,
                            car.card_payment,
                            car.model)
        assert False
    except KeyError:
        assert True


test_car_service()

