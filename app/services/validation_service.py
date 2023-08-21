# import app logger
from app.utils.logger import get_app_logger
import glob, os
from app.dao.form4_dao import Form4DAO
from app.dao.form5_dao import Form5DAO
from validators.commons.giin_validator import GIINValidator
from app.file_readers.xlsx_reader import XLSXReader
from validators.HK.tin_validator import HKTINValidator

log = get_app_logger(__name__)

class ValidationService:
    def __init__(self):
        pass


    def validate_all_files(self, directory_path):
        log.debug("Validating all files in directory: " + directory_path)
        files = self._get_files_from_directory(directory_path)
        log.debug("Found " + str(len(files)) + " files to validate.")
        results = {}
        for file in files:
            if not file.startswith("~$") and file.endswith(".xlsx"):
                results[file] = self._validate_single_file(file)
        return results

    def _get_files_from_directory(self, directory_path):
        log.debug("Getting files from directory: " + os.path.join(directory_path, "*.xlsx"))
        return glob.glob(os.path.join(directory_path, "*.xlsx"))


    def _validate_single_file(self, file_path):
        log.debug("Validating file: " + file_path)
        
        # Reading the file just once
        xlsx_reader = XLSXReader()
        xlsx_data = xlsx_reader.fetch_data_from_xlsx(file_path)
        form5_dao = Form5DAO(xlsx_data)

        # Get the GIIN and FI Name from the DAO
        giin = form5_dao.get_GIIN()
        expected_fi_name = form5_dao.get_FIName()
        log.info(f'GIIN: {giin}')

        # Validate the GIIN
        giin_validator = GIINValidator()
        response_giin_validator = giin_validator.validate(giin=giin, template='XXXXXX.XXXXX.XX.XXX', expected_fi_name=expected_fi_name)
        log.info(response_giin_validator)

        # Validate the TIN
        form4_dao = Form4DAO(xlsx_data)
        BRID = form4_dao.get_BRID()
        hk_validator = HKTINValidator()
        response_hk_validator = hk_validator.validate_business_tin(tin=BRID)
        log.info(response_hk_validator)

