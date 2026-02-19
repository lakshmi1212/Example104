# Example104 Math Operations

This repository provides simple math operations (addition and subtraction) with automated tests and CI integration.

## Usage

```
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 2))   # Output: 3
```

## Running Tests

Install dependencies:

```
pip install -r default/requirements.txt
```

Run all tests:

```
pytest tests/
```

## CI Workflow

The CI pipeline runs on GitHub Actions using `.github/workflows/ci.yml`. It executes all tests and generates HTML/JUnit reports.

## Project Structure

- src/                  - Source code
- tests/                - Test files (pytest)
- default/requirements.txt - Python dependencies
- default/math.json     - CI workflow metadata
- default/README.md     - This documentation
