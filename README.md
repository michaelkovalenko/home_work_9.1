# Banking transactions widget
## Description:
A collection of Python utility modules for processing banking transactions, including automated data masking, sorting, and state-based filtering.
## Installation:

1. Clone repository:
    ```commandline
    git clone git@github.com:michaelkovalenko/home_work_9.1.git
    ```
2. Installing dependencies:
    ```
    poetry install
    ```
## Usage:

Import the required functions into your script to process your financial datasets.

```commandline
from src.processing import filter_by_state

# Quick integration example (Пример быстрой интеграции)
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