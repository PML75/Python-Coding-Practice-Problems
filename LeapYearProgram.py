# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# on every year that is evenly divisible by 4 = T
# **except** every year that is evenly divisible by 100 = F
# **unless** the year is also evenly divisible by 400 = T 

y1 = bool(year % 4 == 0)
y2 = bool(year % 100 == 0)
y3 = bool(year % 400 == 0)

if (y1 == True and y2 == False and y3 == False):
    print("Leap year.")
elif(y1 == True and y2 == True and y3 == True):
    print("Leap year.")
elif(y1 == True and y2 == True and y3 == False):
    print("Not leap year.")
else:
    print("Not leap year.")



