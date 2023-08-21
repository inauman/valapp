import importlib
from core.base_validator import BaseValidator
from utils.logger import get_logger

log = get_logger(__name__)
class TINValidator(BaseValidator):
    def __init__(self):
        pass

    def validate_individual_tin(self, tin, country_code):
        # Use dynamic import to call country-specific TIN validation
        try:
            module = importlib.import_module(f"validators.{country_code}.tin_validator")
            validator_class = getattr(module, f"{country_code.upper()}TINValidator")
            validator = validator_class()
            log.info(f"Validating individual TIN for country: {country_code}")
            return validator.validate_individual(tin)
        except (ModuleNotFoundError, AttributeError) as e:
            log.error(f"Error validating individual TIN for country {country_code}: {e}")
            return False, {"message": f"No TIN validator found for country: {country_code}", "code": 401}

    def validate_business_tin(self, tin, country_code):
        # Similarly, call the business TIN validation for the given country
        try:
            module = importlib.import_module(f"validators.{country_code}.tin_validator")
            validator_class = getattr(module, f"{country_code.upper()}TINValidator")
            validator = validator_class()
            log.info(f"Validating business TIN for country: {country_code}")
            return validator.validate_business(tin)
        except (ModuleNotFoundError, AttributeError) as e:
            log.error(f"Error validating business TIN for country {country_code}: {e}")
            return False, {"message": f"No business TIN validator found for country: {country_code}", "code": 402}

    def validate_individual_tin(self, tin, country_code):
        # Use dynamic import to call country-specific TIN validation
        try:
            module = importlib.import_module(f"validators.{country_code}.tin_validator")
            validator_class = getattr(module, f"{country_code.upper()}TINValidator")
            validator = validator_class()
            log.info(f"Validating individual TIN for country: {country_code}")
            return validator.validate_individual(tin)
        except (ModuleNotFoundError, AttributeError) as e:
            log.error(f"Error validating individual TIN for country {country_code}: {e}")
            return False, {"message": f"No TIN validator found for country: {country_code}", "code": 401}

    def validate_business_tin(self, tin, country_code):
        # Similarly, call the business TIN validation for the given country
        try:
            module = importlib.import_module(f"validators.{country_code}.tin_validator")
            validator_class = getattr(module, f"{country_code.upper()}TINValidator")
            validator = validator_class()
            log.info(f"Validating business TIN for country: {country_code}")
            return validator.validate_business(tin)
        except (ModuleNotFoundError, AttributeError) as e:
            log.error(f"Error validating business TIN for country {country_code}: {e}")
            return False, {"message": f"No business TIN validator found for country: {country_code}", "code": 402}

