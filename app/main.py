from app.services.validation_service import ValidationService

def main():
    service = ValidationService()
    validation_results = service.validate_all_files("app/data/forms")

if __name__ == '__main__':
    main()
