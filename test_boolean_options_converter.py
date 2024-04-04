import unittest
from boolean_options_converter import BooleanOptionsCode, get_calculated_options_from_code, get_calculated_code_from_boolean_options

class TestBooleanOptionsCode(unittest.TestCase):
    def test_no_values(self) -> None:
        with self.assertRaises(TypeError):
            code = BooleanOptionsCode()

    def test_negative_number(self) -> None:
        with self.assertRaises(ValueError):
            code = BooleanOptionsCode(number=-1, length=0)

    def test_negative_length(self) -> None:
        with self.assertRaises(ValueError):
            code = BooleanOptionsCode(number=0, length=-1)


class TestBooleanOptionsCodeCalculationFromOptions(unittest.TestCase):

    def test_calculate_asymmetrical_code(self) -> None:
        # Asymmetrical options with False
        options = [True, False, True, True, True, False]

        code = get_calculated_code_from_boolean_options(options)

        self.assertEqual(
            code,
            BooleanOptionsCode(number=29, length=6)
        )


class TestOptionsCalculationFromBooleanOptionsCode(unittest.TestCase):

    def test_calculate_asymmetrical_options_no_trailing_false_options(self) -> None:
        code = BooleanOptionsCode(number=23, length=5)

        options = get_calculated_options_from_code(code)

        self.assertEqual(
            options,
            [True, True, True, False, True]
        )

    def test_calculate_trailing_false_options(self) -> None:
        code = BooleanOptionsCode(number=23, length=10)

        options = get_calculated_options_from_code(code)

        self.assertEqual(
            options,
            [True, True, True, False, True, False, False, False, False, False]
        )


if __name__ == "__main__":
    unittest.main()
