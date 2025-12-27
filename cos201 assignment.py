
# Oyebanji isaac ibukunoluwa
# Matric No: BU24CSC1048
# Department: Computer Science
# this program calculate the federal income tax based on filling status and tax based on filling status and taxable income
# Using the 2009 tax brackets
# Ask user for filling status

print("US Federal Income Tax Calculator(2009)")
print("Enter your filling status:")
print("0 - Single")
print("1 - Married Filing jointly or Qualifying Widow(er) ")
print("2 - Married Filling separately ")
print("3 - Head of Household ")
status = int(input("Enter number (0-3):"))
#Get taxable income
income = float(input("Enter your taxable income:"))
# Define the tax brackets and rates for each filing status

if status == 0: #Single 1
    brackets = [8350,33950,82250,171550,372950]
    rates = [0, 10, 0.15, 0.25, 0.28, 0.33, 0.35]

elif status == 1: # Married Jointly 1
    brackets = [16700, 67900, 137050, 208850, 372950]
    rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

elif status == 2: #Married Separately 1
    brackets = [8350, 33950, 68525, 104425, 186475]
    rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

elif status == 3: #Head of Household 1
    brackets = [11950, 45500, 117450, 190200, 372950]
    rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

else:
    print("Invalid filling status! Please enter 0, 1, 2, 3.")

    exit()
#Calculate the tax
tax = 0.0
previous_brackets = 0
for i in range(len(brackets)):
    if income > brackets[i]:
        tax += (brackets[i] - previous_brackets) * rates[i]
        previous_brackets = brackets[i]
    else:
        tax += (income - previous_brackets)* rates[i]
        break

#Print the result
print("\nYour federal income tax is: ${:.2f}".format(tax))
print("\nThank you for using the tax calculator by ISAAC")