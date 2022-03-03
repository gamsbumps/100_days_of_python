height = input('What is the students height? ').split(',')
for n in range(0,len(height)):
    height[n] = int(height[n])
count = 0   
sum = 0 
average = 0

for i in height:
    count += 1
    sum += i
    average = round(sum/count)

print(f'The total of stundents is: {count} and their avarage height is {average}m')   
def rev_number(n):
  s = 0
  while True:
    k = str(n)
    if k == k[::-1]:
      break
    else:
      m = int(k[::-1])
      n += m
      s += 1
  return s, n, m 

print(rev_number(195))
print(rev_number(1473))