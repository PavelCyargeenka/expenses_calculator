Expenses Calculator

This is a simple Python script that helps you count and store your 
daily/monthly expenses in a .txt file. 
The script creates a .json file where the expenses 
are stored and updates the total amount of money spent for each day in that month.

Usage
To use this script, simply run exp_calculator.py. You will be prompted to enter the following information:

Month number (1-12)
Date (1-31)
Amount paid

After entering this information, the script will update the total amount spent 
for that day and write the details to a .txt file in the format 
Month Date. Paid amount. Total amount spent in Month: Total amount spent.

For example, if you entered 1 for the month, 15 for the date, and 10.50 for the amount paid, 
the script would write the following to a .txt file:

January 15. Paid 10.5 eur. Total paid in January: 10.5 eur 

File Structure
The script consists of a single Python file exp_calculator.py. 
The expenses for each month are stored in a separate .json file, 
and the details for each day are written to a .txt file.

Dependencies
This script does not have any external dependencies.

Contributing
If you find any issues or would like to suggest improvements, 
feel free to submit a pull request or open an issue.

License
This script is released under the MIT license.
