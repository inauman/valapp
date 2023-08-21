from app.file_readers.validation_dict_reader import ValidationDictReader
from app.file_readers.xlsx_reader import XLSXReader
from app.utils.logger import get_app_logger

log = get_app_logger(__name__)

class BaseDAO:
    def __init__(self, xlsx_data):
        self.validation_dict_reader = ValidationDictReader()
        self.validation_rules = self.validation_dict_reader.fetch_validation_rules()
        self.xlsx_data = xlsx_data

    def get_available_forms(self):
        """
        Return the names of available forms (worksheets).
        """
        return list(self.validation_rules.keys())

    def get_fields_for_form(self, form_name):
        """
        Return the names of fields available in a given form.
        """
        fields = []
        form_data = self.validation_rules.get(form_name, [])
        for field_data in form_data:
            fields.append(field_data.get("field_name"))
        return fields

    def get_form_data(self, form_name):
        """
        Retrieve all field data for a given form.
        """
        return self.xlsx_data.get(form_name, {})

    def get_field_data(self, form_name, field_name):
        """
        Retrieve specific field data for a given form.
        """
        form_data = self.get_form_data(form_name)
        return form_data.get(field_name)
