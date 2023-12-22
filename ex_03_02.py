#Input Hours
hrs_input = input("Enter hours: ")

#Input Rate
rate_input = input("Enter rate: ")

#Catching typing errors
try:
    hours = float(hrs_input)
    rate = float(rate_input)
except:
    print("Error, please enter numeric input")
    quit()
    
#Gross pay variable
gross_pay = 0

#If statement to calculate groos pay depending on the hours worked
if hours <= 40:
    gross_pay = hours * rate
elif hours > 40:
    gross_pay = rate * 40 + (rate * 1.5 * (hours - 40))

#Printing the gross pay    
print(gross_pay)