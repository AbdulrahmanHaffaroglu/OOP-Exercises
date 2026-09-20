# Library Management System

A small object-oriented Python project that models a library with books, members, loans, and borrowing rules.

## Features

- Add books to the library
- Register members
- Borrow and return books
- Track loan history and return dates
- Search books by title and author
- Enforce library business rules
- Demonstrate object interaction, composition, and state management

## Project structure

```text
exercise_6/
├── pyproject.toml
├── README.md
├── src/
│   └── library_management_system/
│       ├── __init__.py
│       ├── main.py
│       └── models/
│           ├── __init__.py
│           ├── book.py
│           ├── member.py
│           ├── loan.py
│           └── library.py
├── tests/
│   ├── book_test.py
│   ├── member_test.py
│   ├── loan_test.py
│   └── library_test.py
└── .venv/   # optional local virtual environment
```

## Requirements

- Python 3.10 or newer
- pytest (for running tests)

## Setup

From the project root, create and activate a virtual environment:

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[test]"
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
```

## Run the app

```bash
python src/library_management_system/main.py
```

## Run the tests

```bash
python -m pytest -q
```

## Example behavior

The library demonstrates:

- borrowing a book
- returning a book
- searching by title and author
- rejecting duplicate borrows
- preventing over-borrowing beyond 3 books
- rejecting invalid publication years
- rejecting returns by the wrong member

## Notes

This project follows the same src-based package pattern used in the earlier exercises, so the package is imported as:

```python
from library_management_system.models import Book, Member, Library, Loan
```
