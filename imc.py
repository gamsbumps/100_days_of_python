height = float(input('What is your height? '))
weight = float(input('What is your weight? '))

imc = weight/(height*height)

if imc < 18.5:
    print('You are a healthy weight')
elif 18.5 < imc < 25:
    print('You are on average')
elif 25 < imc < 30:
    print('You are overweight')
elif 30 < imc < 35:
    print('You are obese')
else:
    print('You are severely obese')

print(f'Your imc is {imc}kg/m^2')                