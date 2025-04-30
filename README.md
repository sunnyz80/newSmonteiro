Install the required libraries using pip:
pip install pandas scikit-learn matplotlib

Ensure the 1000SalesRecords.csv file is in the correct location:

By default, the script looks for the file in the newSmonteiro/ directory relative to the script.
If the file is elsewhere, update the file_path variable in the script with the correct path
file_path = '/path/to/1000SalesRecords.csv'

Open a terminal and navigate to the directory containing the script
cd /path/to/your/script

Run the script:
python IntroToDS.py

If you're using Python 3, use:
python3 IntroToDS.py

Troubleshooting
FileNotFoundError:

Ensure the file_path variable points to the correct location of 1000SalesRecords.csv.
ModuleNotFoundError:

Install missing libraries using pip install.
Incorrect Column Names:

Verify the column names in your dataset and update the script accordingly.

License
This project is for educational purposes and is provided "as-is" without warranty.
