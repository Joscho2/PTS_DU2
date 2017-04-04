import random

print(3)
next_undo = random.randint(0, 10)
for i in range(0, 1000):
	if(i == next_undo):
		print("undo")
		next_undo += random.randint(0, 15)
	print("throw")
	print(str(random.randint(0,3)))
print("quit")
