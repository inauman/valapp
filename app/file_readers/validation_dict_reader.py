import csv
import json
from app.utils.logger import get_app_logger

log = get_app_logger(__name__)

class ValidationDictReader:
    def __init__(self, file_path="app/data/rules/validation-dict.csv"):
        self.file_path = file_path

    @staticmethod
    def _process_cells(cell_data):
        """Converts cell data into a list of cells."""
        cells = []

        cell_entries = [entry.strip() for entry in cell_data.split(",")]

        for entry in cell_entries:
            if ':' in entry:  # This is a range
                start, end = entry.split(":")
                start_col = ord(start) - ord('A') + 1  # Convert char to number
                end_col = ord(end) - ord('A') + 1

                cells.extend([chr(i + ord('A') - 1) for i in range(start_col, end_col + 1)])
            else:  # This is an individual cell
                cells.append(entry)

        return cells

    def fetch_validation_rules(self):
        """
        Reads the validation-dict.csv and returns a structured dictionary with rules for each worksheet.
        """
        rules = {}
        repetitive_fields = {}
        with open(self.file_path, "r", encoding="iso-8859-1") as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip the header row

            for row in csvreader:
                worksheet_name, form_name, field_name, target_row, cell_data, template, pad_to, pad_with = row

                if not worksheet_name:  # If worksheet name is not provided, continue to next row
                    continue

                if worksheet_name not in rules:
                    rules[worksheet_name] = []

                field_rule = {
                    "form_name": form_name,
                    "field_name": field_name,
                    "row": int(target_row),
                    "cells": self._process_cells(cell_data) if cell_data else []
                }

                if template:
                    field_rule["template"] = template
                    field_rule["pad_to"] = pad_to if pad_to else None
                    field_rule["pad_with"] = pad_with

                rules[worksheet_name].append(field_rule)
                if worksheet_name not in repetitive_fields:
                    repetitive_fields[worksheet_name] = {}
                
                if field_name in repetitive_fields[worksheet_name]:
                    repetitive_fields[worksheet_name][field_name] += 1
                else:
                    repetitive_fields[worksheet_name][field_name] = 1

            for worksheet, fields in repetitive_fields.items():
                repetitive_fields[worksheet] = {k: v for k, v in fields.items() if v > 1}

            log.debug(f"Validation rules extracted from {self.file_path}: {rules}: {repetitive_fields}")
            return rules, repetitive_fields
        

if __name__ == "__main__":
    dict_reader = ValidationDictReader()
    rules = dict_reader.fetch_validation_rules()
    pretty_json = json.dumps(rules, indent=4)
    log.info(pretty_json)
