import unittest
from io import StringIO
from unittest.mock import patch

from .calculadora import calculadora

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        user_input = ['1', '5', '3', '5']
        expected_output = "Resultado: 5.0 + 3.0 = 8.0\n"
        with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            self.assertIn(expected_output, mock_stdout.getvalue())

    def test_resta(self):
        user_input = ['2', '10', '4', '5']
        expected_output = "Resultado: 10.0 - 4.0 = 6.0\n"
        with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            self.assertIn(expected_output, mock_stdout.getvalue())

    def test_multiplicacion(self):
        user_input = ['3', '6', '7', '5']
        expected_output = "Resultado: 6.0 * 7.0 = 42.0\n"
        with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            self.assertIn(expected_output, mock_stdout.getvalue())

    def test_division(self):
        user_input = ['4', '20', '4', '5']
        expected_output = "Resultado: 20.0 / 4.0 = 5.0\n"
        with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            self.assertIn(expected_output, mock_stdout.getvalue())

    def test_division_por_cero(self):
        user_input = ['4', '10', '0', '5']
        expected_output = "Error: No se puede dividir entre cero.\n"
        with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculadora()
            self.assertIn(expected_output, mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
