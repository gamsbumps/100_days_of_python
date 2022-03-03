import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer = [rock, paper, scissors]
comp = len(computer)
randoming = random.randint(0, comp - 1)
comp_choice = computer[randoming]

player = input('Rock, Paper ou Scissors? ').lower()

if player == 'rock':
    if comp_choice  == 0:
        print('Tie')
    elif comp_choice  == 1:
        print('Computer wins')
        print(paper)   
    else:
        print('You win')
        print(rock)  
        print(comp_choice )   

if player == 'paper':
    if comp_choice  == 0:
        print('You win')
        print(paper)
        print(comp_choice )
    elif comp_choice  == 1:
        print('Tie')
    else:
        print('Computer wins')
        print(scissors)     
if player == 'scissors':
    if comp_choice  == 0:
        print('Computer wins')
        print(rock)
    elif comp_choice  == 1:
        print('You win')
        print(scissors)   
        print(comp_choice )
    else:
        print('Tie')



