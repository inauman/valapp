import pytest
from app.file_readers.validation_dict_reader import ValidationDictReader
from app.utils.logger import get_app_logger

# Assuming you have the actual `validation-dict.xlsx` at this location
FILE_PATH = "app/data/rules/validation-dict.xlsx"

log = get_app_logger(__name__)

class TestValidationDictReader:

    def setup_method(self, method):
        pass
    
    def test_fetch_validation_rules(self):
        dict_reader = ValidationDictReader(FILE_PATH)
        rules = dict_reader.fetch_validation_rules()
        log.info(rules)
        
        # Asserting that the rules are not empty, you can expand this as needed
        assert rules
