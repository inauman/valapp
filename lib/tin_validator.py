from lib.id_validator import IDValidator
from utils.logger import get_logger

log = get_logger(__name__)

class TINValidator(IDValidator):
    def verify(self, country_code: str, id_subtype: str, id_value: str, detailed: bool = False):
        # Placeholder, should be overridden by specific country subclasses
        raise NotImplementedError("This method should be overridden in child classes.")
    
    def verifyTIN(self, country_code: str, id_subtype: str, tin: str, detailed: bool = False):
        return self.verify(country_code, id_subtype, tin, detailed)
