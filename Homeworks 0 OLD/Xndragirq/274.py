import random
def input_num(message):
	while True:
		try:
			n = int(input(message))
			return n
		except ValueError:
			print("Mutqagreq tiv!")
def rand_str_arr(n = 5):
	arr = []
	for i in range(n):
		arr.append(chr(random.randint(0,25) + 97))
	return arr
while True:
	n = input_num("Mutqagreq zuyg erkarutyuny (0 - elq): ")
	if n is 0:
		print("Hajoxutyun!")
		break
	arr = rand_str_arr(n)
	print("Array = ", arr)
	sm = 0
	for i in range(n):
		if 's' in arr[i]:
			sm += i
	print("Gumary =", sm)