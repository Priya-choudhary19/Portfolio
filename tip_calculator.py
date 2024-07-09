print("Welcome to the tip Calculator")
bill= float(input("What was the total bill?"))
tip= int(input("How much tip would you like to give? 10,12,15:"))
people=int(input("How many people to split the bill?"))
Total_amount= (tip/100*bill)+bill
print("Total amount to be paid:",Total_amount)
ind_amount= Total_amount/people
print("Each one get:",ind_amount)