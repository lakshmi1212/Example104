# Example104 Math Operations

## Overview
This repository contains Python functions for basic math operations (addition and subtraction) and their corresponding pytest-based unit tests.

## Structure
- `src/math_operations.py`: Business logic for add and subtract functions.
- `tests/test_add.py`: Tests for addition.
- `tests/test_subtract.py`: Tests for subtraction.

## Usage
```
from src.math_operations import add, subtract
print(add(2, 3))       # Output: 5
print(subtract(5, 2))  # Output: 3
```

## Running Tests
Install dependencies:
```
pip install -r default/requirements.txt
```
Run tests:
```
pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI Workflow
The CI pipeline runs on pushes to the `Feature1` branch and pull requests to `main`. Test results are reported in both JUnit XML and HTML formats.
