total_years = 100


your_age = int(input('How old are you? '))

years_left = total_years - your_age
months_left = years_left*12
weeks_left = years_left*52
days_left = years_left*365 


print(f'You have {days_left} days, {weeks_left} weeks and {months_left} months left')