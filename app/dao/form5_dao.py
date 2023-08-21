
from .base_dao import BaseDAO
from app.utils.logger import get_app_logger

log = get_app_logger(__name__)

class Form5DAO(BaseDAO):
    def __init__(self, xlsx_data):
        super().__init__(xlsx_data=xlsx_data)

    def get_GIIN(self):
        return self.get_field_data('Part 5', 'GIIN')

    def get_GIIN_template(self):
        return self.get_field_data('Part 5', 'GIIN')

    def get_FIName(self):
        return self.get_field_data('Part 5', 'FIName')