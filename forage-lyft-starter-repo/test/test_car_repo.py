import unittest
from datetime import datetime
from parameterized import parameterized

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

class TestCarModels(unittest.TestCase):
    @parameterized.expand([
        (Calliope, datetime.today().date().replace(year=datetime.today().year - 3), 0, 0, True),
        (Calliope, datetime.today().date().replace(year=datetime.today().year - 1), 0, 0, False),
        (Calliope, datetime.today().date(), 30001, 0, True),
        (Calliope, datetime.today().date(), 30000, 0, False),
        (Glissade, datetime.today().date().replace(year=datetime.today().year - 3), 0, 0, True),
        (Glissade, datetime.today().date().replace(year=datetime.today().year - 1), 0, 0, False),
        (Glissade, datetime.today().date(), 60001, 0, True),
        (Glissade, datetime.today().date(), 60000, 0, False),
        (Palindrome, datetime.today().date().replace(year=datetime.today().year - 5), False, True),
        (Palindrome, datetime.today().date().replace(year=datetime.today().year - 3), False, False),
        (Palindrome, datetime.today().date(), True, True),
        (Palindrome, datetime.today().date(), False, False),
        (Rorschach, datetime.today().date().replace(year=datetime.today().year - 5), 0, 0, True),
        (Rorschach, datetime.today().date().replace(year=datetime.today().year - 3), 0, 0, False),
        (Rorschach, datetime.today().date(), 60001, 0, True),
        (Rorschach, datetime.today().date(), 60000, 0, False),
        (Thovex, datetime.today().date().replace(year=datetime.today().year - 5), 0, 0, True),
        (Thovex, datetime.today().date().replace(year=datetime.today().year - 3), 0, 0, False),
        (Thovex, datetime.today().date(), 30001, 0, True),
        (Thovex, datetime.today().date(), 30000, 0, False),
    ])
    def test_car_needs_service(self, car_model, last_service_date, current_mileage, last_service_mileage, expected_result):
        car = car_model(last_service_date, current_mileage, last_service_mileage)
        self.assertEqual(car.needs_service(), expected_result)

if __name__ == '__main__':
    unittest.main()