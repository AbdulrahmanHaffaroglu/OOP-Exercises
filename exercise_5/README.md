# E-Commerce Order System

An object-oriented Python exercise demonstrating products, customers, orders,
order items, properties, composition, association, and order state changes.

## Requirements

- Python 3.10 or newer

## Setup

Create and activate a virtual environment from the repository root:

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[test]"
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
```

In VS Code, select the Python interpreter from `.venv` when prompted, or use
**Python: Select Interpreter**.

## Run the tests

```bash
python -m pytest -q
```

## Run the demonstration

```bash
python -m e_commerce_order_system.main
```