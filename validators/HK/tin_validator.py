import re
from utils.logger import get_logger
from validators.tin_validator import TINValidator

log = get_logger(__name__)

class HKTINValidator(TINValidator):

    # Regular expression for HKID number
    _HKID_PATTERN = r"^[A-Z]{1,2}\d{6}[0-9A]?$"
    
    # Regular expression for BR number
    _BR_PATTERN = r"^\d{8}$"
    
    def __init__(self):
        pass
    
    def validate_business_tin(self, tin):
        """
        Validates the BR number.
        Format: It comprises 8 numerals (e.g., 99999999)
        """
        if re.match(self._BR_PATTERN, tin):
            log.info(f"Valid BR number: {tin}")
            return True, {"message": "BRID validation successful", "code": 0}
        else:
            log.warning(f"Invalid BR number: {tin}")
            return False, {"message": "Invalid BR number format.", "code": 102}
            
    def validate_individual_tin(self, tin):
        """
        Validates the HKID number.
        Format: @ 123456(#)
        - @ represents any one or two capital letters of the alphabet.
        - # is the check digit which has 11 possible values from 0 to 9 and A.
        """
        if re.match(self._HKID_PATTERN, tin):
            log.info(f"Valid HKID: {tin}")
            return True, {"message": "HKID validation successful", "code": 0}
        else:
            log.warning(f"Invalid HKID: {tin}")
            return False, {"message": "Invalid HKID format.", "code": 101}

    def validate_business_tin(self, tin):
        """
        Validates the BR number.
        Format: It comprises 8 numerals (e.g., 99999999)
        """
        if re.match(self._BR_PATTERN, tin):
            log.info(f"Valid BR number: {tin}")
            return True, {"message": "BRID validation successful", "code": 0}
        else:
            log.warning(f"Invalid BR number: {tin}")
            return False, {"message": "Invalid BR number format.", "code": 102}
