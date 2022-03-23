from domain.car_validator import CarValidator
from repository.GenericFileRepository import GenericFileRepository
from repository.car_repository import CarInMemoryRepository
from repository.location_repository import LocationInMemoryRepository
from repository.order_repository import OrderInMemoryRepository
from service.car_service import CarService
from service.location_service import LocationService
from service.order_service import OrderService
from UI.console import Console

# car_repository = CarInMemoryRepository()
# location_repository = LocationInMemoryRepository()
# order_repository = OrderInMemoryRepository()
car_repository = GenericFileRepository('cars.pkl')
location_repository = GenericFileRepository('locations.pkl')
order_repository = GenericFileRepository('orders.pkl')

car_validator = CarValidator()
# order_validator = OrderValidator(car_repository, location_repository)

car_service = CarService(car_repository, order_repository, car_validator)
location_service = LocationService(location_repository)
order_service = OrderService(order_repository, car_repository, location_repository)
#
# car_service.add_car(1, '1', 'high', 'da', '1234')
# location_service.add_location(1, 'kogalniceanu', 1, 1, 1, 'nimic')
# location_service.add_location(2, 'rebreanu', 2, 2, 2, 'nimic 2')
# order_service.add_order(1, 1, 1, 20, 3, 10, 'done')
# order_service.add_order(2, 1, 1, 20, 3, 7, 'done')
# order_service.add_order(3, 1, 1, 20, 3, 12, 'done')
# order_service.add_order(4, 1, 2, 20, 3, 20, 'done')
# order_service.add_order(50, 1, 2, 20, 3, 14, 'done')

console = Console(car_service, location_service, order_service)
console.run_console()
