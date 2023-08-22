
from .base_dao import BaseDAO
from app.utils.logger import get_app_logger

log = get_app_logger(__name__)

class Form4DAO(BaseDAO):
    def __init__(self, xlsx_data):
        super().__init__(xlsx_data=xlsx_data)

    def get_BRID(self):
        return self.get_field_data('Part 4', 'BRID')