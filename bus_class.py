class Bus:
    def __init__(self, car_number, driver, route_number):
        self.car_number, self.driver, self.route_number = car_number, driver, route_number

    def get_data(self):
        return self.car_number, self.driver, self.route_number