def compute_grade():
  try:
    score = float(input("Enter score: "))
    if score >= 0.9 and score <= 1.0:
      return "A"
    elif score >= 0.8 and score < 0.9:
      return "B"
    elif score >= 0.7 and score < 0.8:
      return "C"
    elif score >= 0.6 and score < 0.7:
      return "D"
    elif score < 0.6:
      return "F"
    else:
      return "Bad Score"
  except:
    print("Invalid score entered")
    
print(compute_grade())