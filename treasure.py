l1 = ['🫂','🫂','🫂']
l2 = ['🫂','🫂','🫂']
l3 = ['🫂','🫂','🫂']
map = [l1, l2, l3]
print(f'{l1}\n{l2}\n{l3}')

swap_line = int(input('Which line do you want to mark? '))
column = int(input('Which column do you want to mark? '))

map[swap_line - 1][column - 1] = 'x'
print(f'{l1}\n{l2}\n{l3}')