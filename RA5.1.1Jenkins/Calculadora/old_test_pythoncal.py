import unittest
from calculadora import suma, resta, multiplicacion, division

class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)

    def test_division_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            division(5, 0)

if __name__ == '__main__':
    unittest.main()
