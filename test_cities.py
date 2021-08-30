from city_functions import city_country as cc
import unittest


class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        """Does data like 'Bucharest, Romania' work?"""
        formatted_city_country = cc('bucharest', 'romania')
        self.assertEqual(formatted_city_country, 'Bucharest, Romania')

    def test_city_country_population(self):
        """Does data like 'Santiago, Chile, 5000000' work?"""
        formatted_city_country_population = cc('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city_country_population, 'Santiago, Chile - Population: 5000000')


if __name__ == '__main__':
    unittest.main()
