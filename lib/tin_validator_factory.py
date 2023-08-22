from lib.tin_validator import TINValidator
from lib.hk_tin_validator import HKTINValidator
from utils.logger import get_logger

log = get_logger(__name__)

class TINValidatorFactory:
    @staticmethod
    def create_validator(country_code: str) -> TINValidator:
        if country_code == "HK":
            return HKTINValidator()
        # ... other country mappings can be added here ...
        else:
            return TINValidator()
