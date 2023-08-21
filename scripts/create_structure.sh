#!/bin/bash

# Define the base directory (taxguards)
BASE_DIR="."

# Create base files and utils
touch $BASE_DIR/__init__.py
touch $BASE_DIR/base_validator.py
mkdir $BASE_DIR/utils
touch $BASE_DIR/utils/__init__.py
touch $BASE_DIR/utils/common_utils.py

# Create validators directory and its sub-directories
mkdir $BASE_DIR/validators
touch $BASE_DIR/validators/__init__.py

# Global validators
mkdir $BASE_DIR/validators/global
touch $BASE_DIR/validators/global/__init__.py
touch $BASE_DIR/validators/global/giin_validator.py

# Country-specific validators
mkdir $BASE_DIR/validators/HK
touch $BASE_DIR/validators/HK/__init__.py
touch $BASE_DIR/validators/HK/tin_validator.py

mkdir $BASE_DIR/validators/US
touch $BASE_DIR/validators/US/__init__.py
touch $BASE_DIR/validators/US/tin_validator.py

# Create tests directory
mkdir $BASE_DIR/tests
touch $BASE_DIR/tests/__init__.py
touch $BASE_DIR/tests/test_giin_validator.py
touch $BASE_DIR/tests/test_hk_tin_validator.py

echo "Project structure created successfully!"
