import random

names = input('Write your names separated by comma: \n')
separated_names = names.split(',')
qtd = len(separated_names)
randoms = random.randint(0, qtd-1)
drawn = separated_names[randoms]
print(randoms)