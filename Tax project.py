def is_valid_ssn(ssn):
    # Check if the Social Security Number is exactly 9 digits.
    return ssn.isdigit() and len(ssn) == 9


def read_tax_brackets(tax_bracket):
    #Read tax brackets from a file and return as a list of tuples.
    brackets = []  # Initialize an empty list to store brackets
    with open(tax_bracket, 'r') as file:
        lines = file.readlines()  # Read all lines at once

    # Iterate through the lines two at a time
    for i in range(0, len(lines), 2):
        rate = float(lines[i].strip())  # Read and convert the tax rate
        threshold_line = lines[i + 1].strip()  # Read the threshold

        # Convert threshold to float or use infinity
        threshold = float('inf') if threshold_line == 'inf' else int(threshold_line)

        # Append the (rate, threshold) tuple to the brackets list
        brackets.append((rate, threshold))

    return brackets

    #I had some help from teh internet since i did not know how to go about this: reading the file


def calculate_federal_tax(income):
    # Calculate the federal tax based on the stepped tax brackets for 2023.
    tax_due = 0

    if income > 578125:
        tax_due += (income - 578125) * 0.37
        income = 578125
    if income > 231250:
        tax_due += (income - 231250) * 0.35 + 52832
        income = 231250
    if income > 182100:
        tax_due += (income - 182100) * 0.32 + 37104
        income = 182100
    if income > 95375:
        tax_due += (income - 95375) * 0.24 + 16290
        income = 95375
    if income > 44725:
        tax_due += (income - 44725) * 0.22 + 5147
        income = 44725
    if income > 11000:
        tax_due += (income - 11000) * 0.12 + 1100
        income = 11000
    tax_due += income * 0.10  # First bracket 10%

    return round(tax_due, 2)


def format_receipt(name, ssn, salary, tax_due, effective_rate):
    # Prints the tax details in a formatted receipt.
    receipt = f"""
+{'-' * 56}+
| {"Federal Income Tax Statement":<54} |
+{'-' * 56}+
| {"Name":<30} .................... {name:>22} |
| {"SSN":<30} .................... {ssn:>22} |
| {"Income":<30} .................... ${salary:>21,.2f} |
| {"Federal Tax Due":<30} .................... ${tax_due:>21,.2f} |
| {"Effective Tax Rate":<30} .................... {effective_rate:>21.1f}% |
+{'-' * 56}+ 
"""
# the effective tax rate is printed into one decimal place using string formatting
    print(receipt)


def main():
    while True:
        # Get the name, SSN, and salary from the user
        name = input("Enter your name: ")

        ssn = input("Enter your Social Security Number (9 digits): ")
        while not is_valid_ssn(ssn):
            print("Invalid SSN. Please enter a 9-digit SSN.")
            ssn = input("Enter your Social Security Number (9 digits): ")

        salary = float(input("Enter your salary: "))

        # Calculate the federal tax and effective tax rate
        tax_due = calculate_federal_tax(salary)
        effective_tax_rate = (tax_due / salary) * 100

        # Print the receipt with formatted output
        format_receipt(name, ssn, salary, tax_due, effective_tax_rate)

        # Ask if the user wants to calculate for another filer
        another = input("Do you want to calculate for another filer? (yes/no): ").lower()
        if another != 'yes':
            break


main()