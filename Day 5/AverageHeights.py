# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n]) 
# 🚨 Don't change the code above 👆
#student_heights is a list
hSum = 0
count = 0
for elem in student_heights:
    hSum += elem
    count += 1
    
average_height = hSum / count
print(round(average_height))

#Write your code below this row 👇




