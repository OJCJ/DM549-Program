from functools import reduce

########################
### Hjælpefunktioner ###
########################
def gcd_args(m: int, n: int) -> int:
	""" Finder gcd med argumenter i stedet for brugerinput.
	Bruges når andre udregninger skal bruge gcd af to tal.
	"""
	m = abs(m)
	n = abs(n)

	while m != n:
		if m < n:
			n -= m
		else:
			m -= n

	return m

def lcm_list(v: list[int]) -> int:
	""" Finder det lcm for en liste af et vilkårligt antal værdier.
	"""
	lcm = v[0]
	for i in range(1, len(v)):
		lcm = lcm*v[i]//gcd_args(lcm, v[i])
	return lcm

def multiplikativ_invers_args(a: int, m: int) -> int:
	""" Finder den mulitplikative med argumenter i stedet for brugerinput.
	Bruges når andre udregninger skal bruge gcd af to tal.
	"""
	invers = 1

	while (invers*a) % m != 1:
		invers = invers + 1

	return invers

def is_prime(x: int) -> bool:
	""" Returnerer om x er et primtal.
	"""
	divisors = []

	for i in range(1, x+1):
		if x%i == 0:
			divisors = divisors + [i]

	return len(divisors) == 2


############################
### Brugerens funktioner ###
############################
def gcd() -> None:
	""" Brugerens funktion til at finde den største fælles divisor
	for tallene a og b.
	"""
	a = int(input("Hvad er dit a?\n").strip())
	b = int(input("Hvad er dit b?\n").strip())

	print(f"\ngcd({a}, {b}) = {gcd_args(a, b)}\n")


def lcm() -> None:
	""" Brugerens funktion til at finde det mindste fælles multiplum
	for tallene a og b.
	"""
	a = int(input("Hvad er dit a?\n").strip())
	b = int(input("Hvad er dit b?\n").strip())
	
	print(f"\nlcm({a}, {b}) = {abs(a*b)//gcd_args(a, b)}\n")


def multiplikativ_invers() -> None:
	""" Brugerens funktion til at finde den multiplikative invers
	til a modulus m.
	"""
	a = int(input("Hvad er dit a?\n").strip())
	m = int(input("Hvad er dit m?\n").strip())

	if gcd_args(a, m) != 1:
		print(f"\n{a} og {m} er ikke relativt primiske så der findes ikke en mulitplikativ invers til {a} modulus {m}.\n")
		return

	print(f"\nDen multiplikative invers til {a} modulus {m} er {multiplikativ_invers_args(a, m)}.\n")


def løs_kongruens() -> None:
	""" Brugerens funktion til at løse en kongruens.
	"""
	a = int(input("Hvad er dit a?\n").strip())
	b = int(input("Hvad er dit b?\n").strip())
	m = int(input("Hvad er dit m?\n").strip())

	# hvis a og m er relativt primiske kan den multiplikative invers bruges
	if gcd_args(a, m) == 1:
		print(f"\nFor kongruensen {a}x ≡ {b} (mod {m}) er x = {(multiplikativ_invers_args(a, m)*b)%m}.\n")
		return

	modulo_list = []

	"""
	Hvis a og m ikke er relativt primiske er det kun måske der findes en løsning.
	Den eneste måde at vide om der ikke kommer en løsning er ved at tjekke om et
	mønster af rester kommer. Eksempelvis for 4x≡3 (mod 10) hvor mønstret for
	modulo-værdierne er 0, 4, 8, 2, 6 og det gentager sig igen og igen, så der
	er ingen måde at få 3. Derfor gemmes modulo resultaterne og der tjekkes om
	den første og anden halvdel er ens. For eksemplet ovenfor ville det kunne
	siges at der ikke er en løsning når listen er [4, 8, 2, 6, 0, 4, 8, 2, 6, 0].
	Ellers tjekker den bare x-værdier en ad gangen fra 1 og op.
	"""
	x = 1
	while True:
		length = len(modulo_list)
		if length%2 == 0 and length > 0:
			if modulo_list[:length//2] == modulo_list[length//2:]:
				print("\nDer er ingen løsning til denne kongruens.\n")
				break
		if (a*x)%m == b:
			print(f"\nLøsningen til {a}x ≡ {b} (mod {m}) er x = {x}.\n")
			break
		else:
			modulo_list = modulo_list + [(a*x)%m]
		x = x + 1


def kongruenssystem() -> None:
	""" Brugerens funktion til at finde den mindste (og nogle gange flere)
	løsninger til et system af kongruenser.
	"""
	a_list = input("Skriv dine a-værdier, separeret af mellemrum (fx. for x≡3 (mod 7) og x≡9 (mod 5), giv '3 9'):\n").strip().split(" ")
	m_list = input("Skriv dine m-værdier, separeret af mellemrum (fx. for x≡3 (mod 7) og x≡9 (mod 5), giv '7 5'):\n").strip().split(" ")

	if len(a_list) != len(m_list):
		print("\nDu har ikke givet lige mange a og m værdier.\n")
		return

	if len(a_list) == 1:
		print("\nDu skal angive mere end én kongruens i dit system (brug funktion 4 i stedet).\n")
		return

	system_size = len(m_list)

	# konvertere liste elementer til int
	a_list = [int(a) for a in a_list]
	m_list = [int(m) for m in m_list]

	chinese_method = True

	# tjek at input m'er er gyldigt
	for m in m_list:
		if m < 2:
			print(f"\nDu har angivet {m} som et af dine m'er, dette er ikke defineret.\n")
			return

	# tjekke om den kinesiske restklasse sætning skal bruges.
	# hvis alle m'er er parvist relativt primiske skal den.
	for i, m in enumerate(m_list[:-1]):
		for n in m_list[i+1:]:
			if gcd_args(m, n) != 1:
				chinese_method = False

	if chinese_method: # brug den kinesiske restklasse sætning
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

		# udregn x
		x = 0
		for i in range(system_size):
			x = x + (a_list[i]*M_list[i]*y_list[i])

		x = x % m_product # reducer x til det mindste mulige

		# print x
		print(f"\nx = {x}")
		print(f"\nAlle x = {x} + k * {m_product}, hvor k er et hvert heltal, er også løsninger (..., {x-(2*m_product)}, {x-m_product}, {x}, {x+m_product}, {x+(2*m_product)},...).\n")
	
	else: # hvis den kinesiske restklasse sætning kan bruges
		"""
		her benyttes det faktum at hvis der findes en løsning, findes der en løsning
		der ligger mellem 1 og det mindste fælles multiplum af m'erne (se slide 11 i "Noter uge 44-1").
		derfor behøver værdier i det interval kun tjekkes, og hvis der ikke er en løsning, er der slet ikke en.
		"""
		for x in range(1, lcm_list(m_list)+1):
			solution_ = [(x % m_list[i]) == a_list[i] for i in range(len(a_list))]
			solution_found = reduce(lambda a, b: a and b, solution_found, True)

			if solution_found:
				print(f"\nx = {x}\n")
				return
		print(f"\nDer er ingen løsning til dit kongruenssystem.\n")


def delelighed() -> None:
	""" Brugerens funktion til at finde ud af om a går op i b.
	"""
	a = int(input("Hvad er dit a?\n").strip())
	b = int(input("Hvad er dit b?\n").strip())

	if b%a == 0:
		print(f"\n{a} går op i {b}: {b} = {b//a} * {a}\n")
	else:
		print(f"\n{a} går ikke op i {b}: {b} = {b//a} * {a} + {b%a}\n")


def primtal() -> None:
	""" Brugerens funktion til at finde ud af om x er et primtal.
	"""
	x = int(input("Hvad er dit x?\n").strip())

	if is_prime(x):
		print(f"\n{x} er ikke et primtal, da følgende tal går op i det:\n\t{', '.join([str(i) for i in divisors])}\n")
		return
	else:
		print(f"\n{x} er et primtal\n")