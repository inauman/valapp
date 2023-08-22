from lib.data_loader import load_data
from utils.logger import get_logger

log = get_logger(__name__)

class IDValidator:
    DEFAULT_CSV_PATH = "data/IDTIN.csv"

    def __init__(self, csv_path: str = DEFAULT_CSV_PATH):
        self.data = load_data(csv_path)

    def verify(self, country_code: str, id_subtype: str, id_value: str, detailed: bool = False):
        raise NotImplementedError("This method should be overridden in child classes.")
