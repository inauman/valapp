import openpyxl
from app.file_readers.validation_dict_reader import ValidationDictReader
from app.utils.logger import get_app_logger

from app.utils.logger import get_app_logger

log = get_app_logger(__name__)

class XLSXReader:

    def __init__(self, rules, repetitive_fields=None):
        self.validation_dict_reader = ValidationDictReader()
        self.rules = rules
        self.repetitive_fields = repetitive_fields if repetitive_fields else {}
        # self.rules = self.validation_dict_reader.fetch_validation_rules()
        # self.repetitive_fields = repetitive_fields if repetitive_fields else {}

    def _get_values_from_range(self, worksheet, cell_range):
        start_col, end_col = openpyxl.utils.cell.coordinate_from_string(cell_range)
        row, _ = openpyxl.utils.cell.rowcol_from_string(cell_range)
        values = []
        for col in range(start_col, end_col + 1):
            values.append(worksheet.cell(row=row, column=col).value)
        return ''.join(str(value) for value in values)

    def fetch_data_from_xlsx(self, filename):
        wb = openpyxl.load_workbook(filename)
        data = {}

        for worksheet_name, fields in self.rules.items():
            worksheet = wb[worksheet_name]
            data[worksheet_name] = {}

            for field in fields:
                # Check if this field is a repetitive field
                is_repetitive = worksheet_name in self.repetitive_fields and field["field_name"] in self.repetitive_fields[worksheet_name]

                if is_repetitive and "template" not in field:
                    # For repetitive fields, store the values in a list
                    if field["field_name"] not in data[worksheet_name]:
                        data[worksheet_name][field["field_name"]] = []

                values = []
                for cell in field["cells"]:
                    value = worksheet[f"{cell}{field['row']}"].value

                    if value is not None:  # Check if the value is not None
                        if isinstance(value, str):
                            value = value.strip()  # Only strip strings
                        values.append(str(value))  # Convert value to string explicitly
                    else:
                        values.append("")  # Add empty string for None values
                # If a template is provided for the field
                if "template" in field:
                    concatenated_value = self._pad_value("".join(values), field["template"], field["pad_to"], field["pad_with"])
                    if is_repetitive:
                        data[worksheet_name][field["field_name"]].append(concatenated_value)
                    else:
                        data[worksheet_name][field["field_name"]] = concatenated_value
                else:
                    # If there's no template, simply join the values
                    concatenated_value = "".join(values)
                    if is_repetitive:
                        if concatenated_value and concatenated_value != "":
                            data[worksheet_name][field["field_name"]].append(concatenated_value)
                        # After extraction, if the list remains empty, remove the field from the data dictionary
                        if not data[worksheet_name][field["field_name"]]:
                            del data[worksheet_name][field["field_name"]]
                    else:
                        data[worksheet_name][field["field_name"]] = concatenated_value
        log.debug(f"Data extracted from {filename}: {data}")
        return data



    def _pad_value(self, value, template, pad_to, pad_with):
        # Split the value and the template on "."
        value_parts = value.split(".")
        template_parts = template.split(".")
        log.debug(f"Value parts: {value_parts}")
        # Pad each part of the value based on its corresponding template part
        padded_parts = []
        for val_part, tmpl_part in zip(value_parts, template_parts):
            if pad_to == "start" and val_part == "0":
                padded_parts.append(val_part.rjust(len(tmpl_part), str(pad_with)))
            elif pad_to == "end" and val_part == "0":  # Assuming 'end' is the only other option
                padded_parts.append(val_part.ljust(len(tmpl_part), str(pad_with)))
            else: #no padding
                padded_parts.append(val_part)

        return ".".join(padded_parts)

if __name__ == "__main__":
    xlsx_reader = XLSXReader()
    xlsx_reader.fetch_data_from_xlsx("Tax Form - ABC.xlsx")
