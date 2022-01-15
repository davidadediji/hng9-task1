def overtime():
  Pay = hours * (rate + 0.5)
  return Pay

try:
  hours = float(input("Enter Hours: "))
  rate = float(input("Enter Rate: "))
  if hours > 40:
    print(overtime())
  else:
    Pay = hours * rate
    print(f"Pay: {Pay} ")
except ValueError:
  print("Please enter numeric input")
  
  


