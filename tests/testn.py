from lib.tin_validator_factory import TINValidatorFactory
from utils.logger import get_logger

log = get_logger(__name__)

def main():
    # Create a validator for Hong Kong TINs
    validator = TINValidatorFactory.create_validator("HK")
    
    # Sample HKIDs (Personal TIN for Hong Kong)
    sample_hkids = ["A123456(4)", "Z999999(0)", "InvalidHKID"]
    for hkid in sample_hkids:
        is_valid = validator.verifyTIN("HK", "P", hkid, detailed=False)
        print(f"HKID: {hkid} -> IsValid: {is_valid}")
        #is_valid, code, message = validator.verifyTIN("HK", "P", hkid, detailed=True)
        #print(f"HKID: {hkid} -> IsValid: {is_valid}, Code: {code}, Message: {message}")

    # Sample Business Registration Numbers (BRN) for Hong Kong
    sample_brns = ["12345678", "87654321", "InvalidBRN"]
    for brn in sample_brns:
        is_valid = validator.verifyTIN("HK", "B", brn, detailed=False)
        print(f"BRN: {brn} -> IsValid: {is_valid}")
        #is_valid, code, message = validator.verifyTIN("HK", "B", brn, detailed=True)
        #print(f"BRN: {brn} -> IsValid: {is_valid}, Code: {code}, Message: {message}")

if __name__ == "__main__":
    main()
