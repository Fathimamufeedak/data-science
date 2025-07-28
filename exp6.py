from datetime import datetime

# Function to parse and compare dates
def find_earlier_date(date_str1, date_str2):
    # Convert strings to datetime objects
    date1 = datetime.strptime(date_str1, "%d-%m-%Y")
    date2 = datetime.strptime(date_str2, "%d-%m-%Y")

    # Compare the dates
    if date1 < date2:
        print(f"The earlier date is: {date1.strftime('%d-%m-%Y')}")
    elif date2 < date1:
        print(f"The earlier date is: {date2.strftime('%d-%m-%Y')}")
    else:
        print("Both dates are the same.")

# Input two dates from the user
d1 = input("Enter first date (dd-mm-yyyy): ")
d2 = input("Enter second date (dd-mm-yyyy): ")

# Find and print the earlier date
find_earlier_date(d1, d2)


