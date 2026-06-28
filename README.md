# Expense Tracker

A command-line expense tracking application built with Python.

## Features
- Add expenses with name, category and automatic date stamping
- View expenses sorted by name, amount, category or date
- Summary of total spending broken down by category
- Data persists between sessions using JSON file storage

## Concepts used
- Object Oriented Programming (2 classes: ExpenseTracker, Expense)
- File I/O with JSON serialization
- datetime for automatic expense dating
- Sorting with lambda functions
- Dictionary grouping for category summaries
- List comprehensions and generator expressions

## How to run
python expense_tracker.py

## Menu options
| Option | Description |
|--------|-------------|
| 1 | Add a new expense |
| 2 | View and sort all expenses |
| 3 | View spending summary by category |
| 4 | Save and quit |

## Example summary output
```
Total spent: $250.00
By category:
Food: $120.00
Transport: $80.00
Entertainment: $50.00
```
