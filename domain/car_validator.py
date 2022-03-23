class CarValidationError(Exception):
    pass

class CarValidator:

    def validate(self, car):

        errors = []
        if car.comfort_level not in ['standard', 'high', 'premium']:
            errors.append('Comfortul trebuie sa fie unul dintre: standard, high, premium!')
        if car.card_payment not in [True, False]:
            errors.append('Plata cu cardul trebuie sa fie una dintre: da, nu')

        if errors != []:
            raise CarValidationError(errors)
