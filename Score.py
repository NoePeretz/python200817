score = int(input("grade:"))

if score >= 0 and score <= 100:
    if score >= 90:
        print("Level A")
    elif score >= 80:
        print("Level B")
    elif score >= 70:
        print("Level C")
    elif score >= 60:
        print("Level D")
else:
   print("error")