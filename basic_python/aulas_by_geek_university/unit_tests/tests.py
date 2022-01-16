'''
Unittest -> Testes unitários


Unittest - Antes e após Hooks


----
hooks -> são os testem em si
----


setup() -> é executado antes de cada teste

tearDown() -> é executado após cada teste
'''


import unittest
from utils_default import *


class tests_utils_default(unittest.TestCase):
    def setUp(self):
        # Executado antes de cada teste
        print('SetUp')
    
    def test_float_w_str(self):
        self.assertEqual(convert_float_from_str('1.2'), 1.2)
    
    def test_float_w_number(self):
        self.assertEqual(convert_float_from_str('1,2'), 1.2)
    
    def test_float_w_zero(self):
        self.assertEqual(convert_float_from_str('0,0'), 0.0)
    
    def test_int_w_str(self):
        self.assertEqual(convert_int_from_str('1'), 1)
    
    def test_int_w_number_dot(self):
        self.assertEqual(convert_int_from_str('10.0'), 10)
        
    def test_int_w_number(self):
        self.assertEqual(convert_int_from_str('-10'), -10)
    
    def test_int_w_out_number(self):
        self.assertEqual(convert_int_from_str('-'), 0)
    
    def test_int_w_zero(self):
        self.assertEqual(convert_int_from_str(''), 0)
        
    def tearDown(self) -> None:
        # Executado depois de cada teste
        print('TearDown')
    
    

if __name__ == '__main__':
    unittest.main()