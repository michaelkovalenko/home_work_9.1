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

```
from src.processing import filter_by_state

# Quick integration example
data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

executed_jobs = filter_by_state(data, "EXECUTED")
```

## Project Structure

- `masks.py` - Handles secure masking of credit card and account numbers.
- `widget.py` - Identifies and masks payment identifiers, and formats transaction dates.
- `processing.py` - Manages filtering datasets by state and sorting by date.


## Testing and Code Quality

The project features automated testing and strict code style verification using modern tools from the Python ecosystem.

### Automated Testing (Pytest)

To run the entire test suite, execute the following command:
```bash
pytest
```

### Code Coverage Analysis (Coverage)

The project achieves **100% test coverage** for its core functionality.

* To view the summary coverage report directly in the terminal, run:
  ```bash
  pytest --cov=src --cov-report=term-missing
  ```
* To generate a detailed interactive HTML report, run:
  ```bash
  pytest --cov=src --cov-report=html
  ```
  The interactive report will be available at `htmlcov/index.html`.

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
