#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

print('Welcome to tip calculator!')
total_bill = input('How much was your total bill? $')
tip_percentage = input('How much percentage of tip you want to give? Enter 10, 12 or 15: ')
total_payment = round(float(total_bill) * (1 + int(tip_percentage)/100),2)

count_of_folks = input('Enter the Number of people among them the bill has to be shared: ')

share_of_each = round(total_payment / int(count_of_folks), 2)

print('The total payment is ${}, so each one has to pay ${}'.format(total_payment, share_of_each))


                       

