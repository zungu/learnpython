#usr/bin/python

#Minimum Monthly Payment = Minimum monthly payment rate x Balance
#(Minimum monthly payment gets split into interest paid and pricipal paid)

#Interest Paid = Annual interest rate / 12 months x Balance

#Principle paid = Minimum monthly payment - Interest paid

#Remaining balance = Balance - Principal paid

#Program calculates credit card balance after one year if person only pays the minimum monthly payment required

balance = float(raw_input('Enter the outstanding balance on your credit card:  '))
annualInterestRate = float(raw_input('Enter the annual credit card interest rate as a decimal:  '))
minMonthlyPaymentRate = float(raw_input('Enter the minimum monthly payment as a decimal:  '))

#monthly interest rate
monthlyInterestRate = annualInterestRate/12

#initialize state variable
numMonths = 1
totalAmtPaid = 0

while numMonths <= 12:
	#Minimum monthly payment of balance at the start of the mont
	minPayment = round(minMonthlyPaymentRate * balance, 2)
	totalAmtPaid += minPayment

	#Amt of monthly payment that goes to interest
	interestPaid = round(monthlyInterestRate * balance, 2)

	#Amt of principal paid off
	principalPaid = minPayment - interestPaid

	# Subtract monthly payment from outstanding balance
	balance -= principalPaid

	print "Month: ", numMonths
	print "Minimum monthly payment: ", minPayment
	print "Remaining balance: ", balance

	#Count this as a new month
	numMonths += 1

print "RESULT"
print "Total amount paid:", totalAmtPaid
print "Remaining balance:", balance 
		

