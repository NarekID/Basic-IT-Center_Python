def input_num(message):
	while True:
		try:
			n = int(input(message))
			return n
		except ValueError:
			print("Mutqagreq tiv!")
while True:
	k = input_num("Mutqagreq 0ic tarber tiv: ")
	if k is 0:
		print("Closing..")
		break
	arr = []
	for i in range(10, 100):
		if i % k is 0:
			arr.append(i)
	print("Array = ", arr)