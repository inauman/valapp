import unittest
from validators.tin_validator import TINValidator
import logging


class TestHKTINValidator(unittest.TestCase):

    def setUp(self):
        self.validator = TINValidator()

    def test_validate_individual_valid(self):
        valid_tin = "A123456A"
        result, _ = self.validator.validate_individual_tin(valid_tin, "HK")
        #self.assertTrue(result)
        assert result

    def test_validate_individual_invalid(self):
        invalid_tin = "12345678"
        result, _ = self.validator.validate_individual_tin(invalid_tin, "HK")
        assert not result


    def test_validate_business_valid(self):
        valid_br = "12345678"
        result, _ = self.validator.validate_business_tin(valid_br, "HK")
        assert result

    def test_validate_business_invalid(self):
        invalid_br = "A1234567A"
        result, _ = self.validator.validate_business_tin(invalid_br, "HK")
        assert not result

if __name__ == '__main__':
    unittest.main()