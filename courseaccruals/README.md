# Course Accruals

An SPLC teaching term usually crosses 3 months, with course fees paid for before the start of term, and facilitator costs paid out either monthly or at the end of term.

In each month of term, we need to as accurately as possible estimate the income earned from course fees for that month, per course category. Ditto the facilitator fees.

To construct the spreadsheet to achieve this, we must first obtain a list of all courses, sorted by category, containing the course and facilitator fees for each course. This script is the first step to achieving this. It takes the exported 'Fees Generated' table from a ClassManager term report (`course_income.csv`) and outputs the aforementioned list as `hurrah.csv`, which is a starting point.

This `hurrah.csv` is then to be put in a spreadsheet to calculate the accrued facilitator fees/course income by pro rata-ing the number of weeks in the month. For example, if an 8 week course was paid $160 in advance, with 4 weeks in April and 4 weeks in May, we need to report $80 of income in April, and another $80 of income in May. Ditto the facilitator fees.

A sample of such a spreadsheet for Term 1 2022 can be found [here](https://docs.google.com/spreadsheets/d/1xhA5-VlcYlu5uovARmEN74ugkUaD-adyTGs5Cd84QvE/edit?usp=sharing)

## Instructions

Put `course_income.csv` in this folder, then run the notebook. To begin a new term, run the 'New Term' notebook, then for subsequent months, run the 'Monthly' notebook, to show updated values (then manually update the values in the spreadsheet for that month).
