English = int(input("What is your English grade?:"))
Math = int(input("What is your math grade?:"))

if Math >= 90 and English >= 90:
    print("You passed! You have earned 50 cents")
if Math <= 60 or English >= 60:
    print("You can do it!")
if Math >= 60 or English <= 60:
    print("You can do it!")
if Math <= 60 and English <= 60:
    print ("No devices for you until you get your grades up.")