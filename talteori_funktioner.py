from functools import reduce

########################
### Hjælpefunktioner ###
########################
def gcd_args(m: int, n: int) -> int:
	""" Finder gcdmed argumenter i stedet for brugerinput.
	Bruges når andre udregninger skal bruge gcd af to tal.
	"""
	while m != n:
		if m < n:
			n -= m
		else:
			m -= n

	return m


def multiplikativ_invers_args(a: int, m: int) -> int:
	""" Finder den mulitplikative med argumenter i stedet for brugerinput.
	Bruges når andre udregninger skal bruge gcd af to tal.
	"""
	invers = 1
	j = 1

	while invers*a-j*m != 1:
		if invers*a < j*m:
			invers = invers + 1
		else:
			j = j + 1

	return invers


############################
### Brugerens funktioner ###
############################
def gcd() -> None:
	a = int(input("Hvad er dit a?\n").strip())
	b = int(input("Hvad er dit b?\n").strip())

	print(f"gcd({a}, {b}) = {gcd_args(a, b)}")


def lcm() -> None:
	a = int(input("Hvad er dit a?\n").strip())
	b = int(input("Hvad er dit b?\n").strip())
	
	print(f"\nlcm({a}, {b}) = {abs(a*b)//gcd_args(a, b)}\n")


def multiplikativ_invers():
	a = int(input("Hvad er dit a?\n").strip())
	m = int(input("Hvad er dit m?\n").strip())

	if gcd_args(a, m) != 1:
		print(f"{a} og {m} er ikke relativt primiske så der findes ikke en mulitplikativ invers til {a} modulus {m}.")
		return

	print(f"\nDen multiplikative invers til {a} modulus {m} er {multiplikativ_invers_args(a, m)}.\n")


def løs_kongruens():
	a = int(input("Hvad er dit a?\n").strip())
	b = int(input("Hvad er dit b?\n").strip())
	m = int(input("Hvad er dit m?\n").strip())

	if gcd_args(a, m) == 1:
		print(f"\nFor kongruensen {a}x ≡ {b} (mod {m}) er x = {(multiplikativ_invers_args(a, m)*b)%m}.\n")
		return

	modulo_list = []

	x = 1
	while True:
		length = len(modulo_list)
		if length%2 == 0 and length > 0:
			if modulo_list[:length//2] == modulo_list[length//2:]:
				print("Der er ingen løsning til denne kongruens.")
				break
		if (a*x)%m == b:
			print(f"Løsningen til {a}x ≡ {b} (mod {m}) er x = {x}.")
			break
		else:
			modulo_list = modulo_list + [(a*x)%m]
		x = x + 1


def kongruenssystem():
	a_list = input("Skriv dine a-værdier, separeret af mellemrum (fx. for x≡3 (mod 7) og x≡9 (mod 5), giv '3 9'):\n").strip().split(" ")
	m_list = input("Skriv dine m-værdier, separeret af mellemrum (fx. for x≡3 (mod 7) og x≡9 (mod 5), giv '7 5'):\n").strip().split(" ")

	if len(a_list) != len(m_list):
		print("\nDu har ikke givet lige mange a og m værdier.\n")
		return

	system_size = len(m_list)

	# konvertere liste elementer til int
	a_list = [int(a) for a in a_list]
	m_list = [int(m) for m in m_list]

	# udregn m, M'er og y'er
	m_product = reduce(lambda x, y : x*y, m_list, 1)

	M_list = [m_product//m0 for m0 in m_list]
	
	y_list = []
	for i in range(system_size):
		y_list = y_list + [multiplikativ_invers_args(M_list[i], m_list[i])]

	# print m
	print(f"\nm = {' * '.join([str(m) for m in m_list])} = {m_product}\n")

	# print m_k, M_k, y_k
	for i in range(system_size):
		print(f"m_{i+1}={m_list[i]}, M_{i+1}={M_list[i]}, y_{i+1}={y_list[i]}")

	# print x
	x = 0
	for i in range(system_size):
		x = x + (a_list[i]*M_list[i]*y_list[i])

	x = x % m_product

	print(f"\nx = {x}")
	print(f"\nAlle x = {x} + k * {m_product}, hvor k er et hvert heltal, er også løsninger (..., {x-(2*m_product)}, {x-m_product}, {x}, {x+m_product}, {x+(2*m_product)},...).\n")

def delelighed():
	a = int(input("Hvad er dit a?\n").strip())
	b = int(input("Hvad er dit b?\n").strip())

	if b%a == 0:
		print(f"\n{a} går op i {b}: {b} = {b//a} * {a}\n")
	else:
		print(f"\n{a} går ikke op i {b}: {b} = {b//a} * {a} + {b%a}\n")