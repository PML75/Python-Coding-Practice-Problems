# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# 1y = 365d, 52w, 12m, 90 yrs old

lDays = (90 - int(age)) * 365
lWeeks = (90 - int(age)) * 52
lMonths = (90 - int(age)) * 12

print("You have", lDays, "days,", lWeeks, "weeks, and", lMonths, "months left.")


