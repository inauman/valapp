import csv

def load_data(csv_path: str) -> dict:
    """
    Load data from the given CSV file into a dictionary.

    :param csv_path: Path to the CSV file.
    :return: Dictionary with country codes as keys and ID details as values.
    """
    data = {}
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            country_code = row["ISOCode"]
            id_subtype = row["IDSubType"]
            if country_code not in data:
                data[country_code] = {}
            data[country_code][id_subtype] = row

    return data
