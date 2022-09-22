# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower1 = name1.lower()
lower2 = name2.lower()

t = lower1.count("t") + lower2.count("t")
r = lower1.count("r") + lower2.count("r")
u = lower1.count("u") + lower2.count("u")
e1 = lower1.count("e") + lower2.count("e")
total1 = t + r + u + e1

l = lower1.count("l") + lower2.count("l")
o = lower1.count("o") + lower2.count("o")
v = lower1.count("v") + lower2.count("v")
e2 = lower1.count("e") + lower2.count("e")
total2 = l + o + v + e2

score = int(f"{total1}{total2}")

if (score <= 10 or score >= 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif(score >= 40 and score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
