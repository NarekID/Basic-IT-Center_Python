import random
def input_num(message):
	while True:
		try:
			n = int(input(message))
			return n
		except ValueError:
			print("Mutqagreq tiv!")
def rand_arr(n = 5, a = 0, b = 5):
	arr = []
	for i in range(n):
		arr.append(random.randint(a,b))
	return arr
while True:
	n = input_num("Mutqagreq zangvaci erkarutyuny (0 - elq): ")
	if n is 0:
		print("Hajoxutyun!")
		break
	if n < 0:
		print("Esrkarutyuny chi karox linel bacasakan!")
		continue
	a = input_num("Mutqagreq random min: ")
	b = input_num("Mutqagreq random max: ")
	while b <= a:
		print("max chi karox linel poqr kam havasar min!")
		b = input_num("Mutqagreq random max: ")
	arr = rand_arr(n, a, b)
	print("Array = ",arr)
	arr2 = []
	mx = arr[0]
	arr2.append(0)
	for i in range(0, n):
		if mx < arr[i]:
			mx = arr[i]
	for i in range(1, n):
		if i % 3 is 0:
			arr2.append(0)
		arr2.append(arr[i])
	print("Array2 = ", arr2)