""""********* Sample Data Used For Testing *********
check city: Arroyo Grande
|  MLS   |    Location   |   Price    | Bedrooms | Bathrooms | Size | Price/SQ.Ft |    Status   |
+--------+---------------+------------+----------+-----------+------+-------------+-------------+
| 132842 | Arroyo Grande | 795000.00  |    3     |     3     | 2371 |    335.30   |  Short Sale
--------------------------------------------------------
Most expensive property $ 5499000.0
Least expensive property $ 54500.0
Average property price $ 680103.75
Average property price per sq/ft $ 299.40225
--------------------------------------------------------"""

import unittest
from read_write_csv_json import read_and_write, check_location


class TestBasicFunctions(unittest.TestCase):

    def setUp(self):
        self.my_result_list=check_location(file_name='RealEstate.csv', city_name='Arroyo Grande')
        self.result_func=read_and_write(self.my_result_list)

    def test_mls_my_result_list(self):
        self.assertEqual(self.my_result_list[1][0],'132842')

    def test_location_name(self):
        self.assertEqual(self.my_result_list[1][1],'Arroyo Grande')

    def test_price(self):
        self.assertEqual(self.my_result_list[1][2], '795000.00')

    def test_mls_match_price(self):
        self.assertEqual(self.my_result_list[1],['132842', 'Arroyo Grande', '795000.00', '3', '3', '2371', '335.30', 'Short Sale'])

    def test_max_price(self):
        self.assertEqual(self.result_func['max_price'],5499000.0)

    def test_min_price(self):
        self.assertEqual(self.result_func['min_price'], 54500.0)

    def test_avg_property_price(self):
        # Average price is in float, for testing, we use a generator to split from decimal and used a round value
        average_str = str(self.result_func["avg_price"])
        round_val, decimal_val = (int(x) for x in average_str.split("."))

        self.assertEqual(round_val,680103)

    def test_avg_price_per_sqft(self):
        # Average price/sqft is in float, for testing, we use a generator to split from decimal and used a round value
        average_per_sqft_str = str(self.result_func["avg_price_per_sqft"])
        round_val, decimal_val = (int(x) for x in average_per_sqft_str.split("."))

        self.assertEqual(round_val,299)

if __name__=='__main__':
    unittest.main()
