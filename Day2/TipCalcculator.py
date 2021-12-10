#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip Calculator!")

#Get the bill amount and type cast it to float because as we have used input function we the value in string format for that only we are type casting it to float
BillAmt=float(input("What was the total bill?$"))

#Get the tip from the user ,typecasting it to int type and storing it in variable tipPercent
tipPercent = int(input("How much tip would you like to give? 10, 12, or 15? "))

#Calculating the tip and adding it to the total bill amount
tip=BillAmt*(tipPercent/100)
TotBill = BillAmt+tip

People=int(input("How many people to split the bill? "))
#Splitting the bill amount among the n number of people(as per the information shared by the user) and rounding it to 2 values
Per_People_Pay = round(TotBill/People,2)

#Printing the final value to the console
print(f"Each person should pay: ${Per_People_Pay}")
