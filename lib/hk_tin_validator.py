from lib.tin_validator import TINValidator
import re
from utils.logger import get_logger
from typing import Union, Tuple

log = get_logger(__name__)

class HKTINValidator(TINValidator):
    def verify1(self, country_code: str, id_subtype: str, id_value: str, detailed: bool = False):
        # Assuming 'country_code' is 'HK' for this subclass.
        regex = self.data['HK'][id_subtype]['RegEx']
        if not re.match(regex, id_value):
            log.error(f"TIN {id_value} does not match the expected format for Hong Kong.")
            return (False, "3", "Invalid TIN format.") if detailed else False

        # Hong Kong checksum validation goes here.
        if not self._validate_hk_checksum(id_value):
            log.error(f"TIN {id_value} failed the checksum validation for Hong Kong.")
            return (False, "4", "Invalid TIN checksum.") if detailed else False

        return (True, "0", "Valid TIN") if detailed else True

    def verify(self, country_code: str, id_subtype: str, tin: str, detailed: bool = False) -> Union[bool, Tuple[bool, str, str]]:
        # If the ID subtype is 'I' (Individual), then validate the checksum.
        

        # For all TIN types, validate against the regex.
        regex = self.data['HK'][id_subtype]['RegEx']
        if not regex or not re.match(regex, tin):
            if detailed:
                return False, "FORMAT_ERR", f"TIN {tin} does not match the expected format for Hong Kong."
            else:
                return False

        if id_subtype == "P":
                    if not self._validate_hk_checksum(tin):
                        if detailed:
                            return False, "CHKSUM_ERR", f"TIN {tin} does not match the expected checksum for Hong Kong."
                        else:
                            return False
        if detailed:
            return True, "SUCCESS", f"TIN {tin} is valid for Hong Kong."
        else:
            return True

    def _validate_hk_checksum(self, tin: str) -> bool:
        # Extract parts of TIN
        prefix = tin[0]
        body = tin[1:7]
        check_digit_str = tin[8:-1]

        # Handle check digit 'A' scenario
        if check_digit_str == 'A':
            check_digit = 10
        else:
            check_digit = int(check_digit_str)

        # Weighted calculation
        weights = [9, 8, 7, 6, 5, 4, 3]

        # Handle 1 or 2 character prefixes
        if tin[1].isalpha():
            prefix_weighted_sum = (ord(prefix[0]) - 64) * weights[0] + (ord(prefix[1]) - 64) * weights[1]
            body_weighted_sum = sum(int(body[i]) * weights[i+2] for i in range(6))
        else:
            prefix_weighted_sum = (ord(prefix) - 64) * weights[1]
            body_weighted_sum = sum(int(body[i]) * weights[i+1] for i in range(6))

        weighted_sum = prefix_weighted_sum + body_weighted_sum
        modulo_result = weighted_sum % 11
        #print(f"Weighted sum: {weighted_sum}, Modulo result: {modulo_result}, Check digit: {check_digit}")
        # Verify against check digit
        if modulo_result == 0 and check_digit == 0:
            return True
        elif modulo_result != 0 and check_digit == 11 - modulo_result:
            return True
        else:
            return False

