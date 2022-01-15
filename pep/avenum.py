total = 0
count = 0

while True:
  inp = input('Enter a number: ')
  if inp.lower() == 'done':break
  try:value =float(inp)    
  except ValueError:
    print('Invalid value given, try again')
    continue
 
  total += value
  count += 1
  print(count)
try:
	average = total/count
	print('Average', average)
except ZeroDivisionError:print('Take a break')

#rewrite to work with list

numlist = []

while True:
  inp = input('Enter a value: ')
  if inp.lower() == 'done':
    break
  value = float(inp)
  numlist.append(value)
average = sum(numlist)/len(numlist)
print('Average', average)