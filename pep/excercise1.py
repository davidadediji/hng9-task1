total = []
max = 0
min = None
while True:
  user_input = input("Enter a number: ")
  if user_input == 'done':
    break
  try:
    num1 = float(user_input)
  except:
    print('Invalid input')
    continue
  total.append(num1)
print(total)

for value in total:
  if value > max:
    max = value
print(max)

for value in total:
  if min is None or value < min:
    min = value
print(min)
  
