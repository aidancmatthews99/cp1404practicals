from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness=1):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return "{}, {}km on current fare, ${:.2f}/km plus flagfall of ${:0.2f}".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km, self.flagfall)

    def get_fare(self):
        if super().get_fare() != 0:
            return super().get_fare() + self.flagfall
        else:
            return 0.00
