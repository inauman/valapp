import csv
from utils.logger import get_logger

log = get_logger(__name__)

class GIINValidator:
    def __init__(self):
        self.irs_data_path = "data/irs/FFIListFull.csv"  # Assuming this is the path, adjust if needed.

    def _validate_giin_format(self, giin, template):
        """
        Validate the giin format based on the template
        :param giin: The giin string to validate
        :param template: The expected format/template
        :return: True if valid, False otherwise
        """
        if not giin:
            return False

        if len(giin) != len(template):
            return False

        for g, t in zip(giin, template):
            if t == 'X' and not g.isalnum():
                return False
            elif t == '.' and g != '.':
                return False

        return True

    def _get_fi_name_from_giin(self, giin):
        """
        Look up the FI Name based on the giin in FFIListFull.csv
        :param giin: The giin string to lookup
        :return: FI Name if found, None otherwise
        """
        with open(self.irs_data_path, "r", encoding="utf-8") as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip header
            for row in csvreader:
                if row[0] == giin:  # Assuming GIIN is the first column
                    return row[1]  # Assuming FI Name is the second column

        return None

    def validate(self, giin, template, expected_fi_name=None):
        """
        Validate giin and (optionally) check it against an expected FI Name
        :param giin: The giin string to validate
        :param template: The expected format/template
        :param expected_fi_name: Expected FI Name (optional)
        :return: Validation result and details
        """
        if not self._validate_giin_format(giin, template):
            log.error(f"Invalid GIIN format: {giin}")
            return False, {"message": f"Invalid GIIN format for: {giin}", "code": 400}

        fi_name = self._get_fi_name_from_giin(giin)
        if not fi_name:
            log.error(f"GIIN not found in IRS list: {giin}")
            return False, {"message": f"GIIN not found in IRS list: {giin}", "code": 401}

        if expected_fi_name and fi_name != expected_fi_name:
            log.error(f"Mismatched FI Name. Expected: {expected_fi_name}, Found: {fi_name}")
            return False, {
                "message": f"Mismatched FI Name. Expected: {expected_fi_name}, Found: {fi_name}",
                "code": 402
            }

        return True, {"message": "GIIN validation successful", "code": 0}

