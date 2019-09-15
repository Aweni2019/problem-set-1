annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
portion_down_payment = 0.25
rate_of_return = 0.04
monthly_rate_of_return = rate_of_return / 12
monthly_salary = annual_salary / 12
down_payment = total_cost * portion_down_payment
monthly_deposit = monthly_salary * portion_saved
current_savings = 0.0
months = 0
while current_savings < down_payment:  
    months += 1
    current_savings *= 1 + monthly_rate_of_return
    current_savings += monthly_deposit
    
print('Congratulations!!! It will take you,', months, ' months to buy your dream house.')