# Banking transactions widget
## Description:
A collection of Python utility modules for processing banking transactions, including automated data masking, sorting, and state-based filtering.
## Installation:

1. Clone repository:
    ```bash
    git clone git@github.com:michaelkovalenko/home_work_9.1.git
    ```
2. Installing dependencies:
    ```bash
    poetry install
    ```
## Usage:

Import the required functions into your script to process your financial datasets.

### Data Filtering and Sorting
```python
from src.processing import filter_by_state, sort_by_date

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

executed_jobs = filter_by_state(data, "EXECUTED")
sorted_jobs = sort_by_date(data, reverse=True)
```

### Payment Data Masking
```python
from src.widget import mask_account_card, get_date

# Masking cards and accounts
print(mask_account_card("Visa Platinum 7000792289606361")) 
# Output: Visa Platinum 7000 79** **** 6361

# Formatting ISO dates
print(get_date("2024-03-11T02:08:58.425572")) 
# Output: 11.03.2024
```

### Card Number Generation
```python
from src.generators import card_number_generator

# Generate card numbers in a given range
for card_number in card_number_generator(1, 3):
    print(card_number)

# Output:
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003
```
## Project Structure

- `masks.py` - Handles secure masking of credit card and account numbers.
- `widget.py` - Identifies and masks payment identifiers, and formats transaction dates.
- `processing.py` - Manages filtering datasets by state and sorting by date.
- `generators.py` - Generates standardized bank card numbers in specified ranges.

## Testing and Code Quality

The project features automated testing and strict code style verification using modern tools from the Python ecosystem.

### Automated Testing and Coverage (Pytest)

All testing and coverage configurations are automated via `pyproject.toml`. To run the entire test suite, execute:
```bash
pytest
```

* Running `pytest` automatically displays the summary coverage report with missing lines directly in the terminal.
* It also updates the interactive HTML report, which is available locally at `htmlcov/index.html`.

### Linters and Code Formatting

The codebase is fully standardized and verified for potential type errors:
* **Black** — the uncompromising code formatter for consistent code style.
* **Isort** — automatically sorts and groups imports according to PEP 8.
* **Flake8** — checks compliance with PEP 8 standards and docstring presence.
* **Mypy** — performs strict static type checking (configured with safe overrides for the tests directory).

To run the complete code quality pipeline, execute these commands sequentially:
```bash
isort .
black .
flake8 src/ tests/
mypy src tests
```
