num_list = []
while True:
  user_input = input('Enter a number: ')
  if user_input == 'done':break
  try:
    number = int(user_input)
  except:
    print('Invalid value entered')
    continue
  num_list.append(number)
try:
	print(max(num_list))
	print(min(num_list))
except ValueError:
  print('No value found in list')
