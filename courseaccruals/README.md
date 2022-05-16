# Course Accruals

## Motivation

An SPLC teaching term usually crosses 3 months, with course fees paid for before the start of term, and facilitator costs paid out either monthly or at the end of term.

In each month of term, we need to as accurately as possible estimate the income earned from course fees for that month only, per course category. Ditto the facilitator fees. For example, if an 8 week course was paid $160 in advance, with 4 weeks in April and 4 weeks in May, we need to report $80 of income in April, and another $80 of income in May. Ditto the facilitator fees.

To construct the spreadsheet to achieve this, we must first obtain a list of all courses, sorted by category, containing the course and facilitator fees for the term, for each course. This script does exactly that. It takes the exported 'Fees Generated' table from a ClassManager term report (`course_income.csv`) and outputs the aforementioned list as `hurrah.csv`, which is a starting point.

This `hurrah.csv` is then to be put in a spreadsheet to calculate the accrued facilitator fees/course income by pro rata-ing the number of weeks in the month. 
A sample of such a spreadsheet for Term 1 2022 can be found [here](https://docs.google.com/spreadsheets/d/1xhA5-VlcYlu5uovARmEN74ugkUaD-adyTGs5Cd84QvE/edit?usp=sharing)

## Instructions
1. in ClassManager go to ```Reports``` -> ```Financial Reports``` and select the Term in question. It will default to ```Financial Reports```, click ```Generate Report```.

2. scroll down to ```Fees generated from classes running in this period``` table, and click the ```Export table``` button at the bottom of this table. The file ```course_income.csv``` will be generated.

3. `course_income.csv` in this folder, then run the notebook. To begin a new term, run the 'New Term' notebook, then for subsequent months, run the 'Monthly' notebook, to show updated values (then manually update the values in the spreadsheet for that month). The output of the notebook is ```hurrah.csv```.

## Next Steps
The next steps have nothing to do with the script, but is here for completeness

1. Add columns for each month of the term

2. Populate these columns with the number of weeks a course (row) runs for those months (hint: sort by start date first, populate, then re-sort by category/course.

3. For each month, add a column to calculate the accrued income earnt for the month, and the accrued facilitator fee for the month.

4. Fill the columns in step 3. with a formula that does the relevant apportioning, using the total number of weeks and number of weeks for the month to calculate the portions acccured

5. Add the figures in set 4. each month, and report them in a General Journal.
