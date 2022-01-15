try:
  temp = float(input("Enter the celcius temperature: "))
  Fahrenheit = (9/5) * temp + 32
  print(f"The temperature in Fahrenheit is: {Fahrenheit}")
except ValueError:
  print("Please enter a number")
  