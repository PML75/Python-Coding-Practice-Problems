import math

def paint_calc(height, width, cover):
  final = math.ceil((height * width) / cover)
  return final

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
print(f"You'll need {paint_calc(height=test_h, width=test_w, cover=coverage)} cans of paint.")


