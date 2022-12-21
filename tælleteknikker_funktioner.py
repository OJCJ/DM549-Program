from functools import reduce

########################
### Hjælpefunktioner ###
########################
def factorial(n: int) -> int:
	""" Returnerer n!. """

	return reduce(lambda x, y: x*y, range(1, n+1), 1)


def permutations_calc(n: int, r: int) -> int:
	""" Returnerer P(n, r). """

	return factorial(n)//factorial(n-r)


def combinations_calc(n: int, r: int) -> int:
	""" Returnerer C(n, r). """

	return permutations_calc(n, r)//factorial(r)


def pascal_calc(n: int) -> list[int]:
	""" Returnerer den n'de liste af Pascals trekant i
	som en liste med n elementer.
	"""
	return [combinations_calc(n-1, r) for r in range(n)]


def pascal_triangle(n:int) -> str:
	""" Returnerer en string repræsentation af de første
	n rækker af pascals trekant. 
	"""
	triangle = ''
	for i in range(1, n+1):
		spaces_count = len(' '.join([str(i) for i in pascal_calc(n)])) - len(' '.join([str(i) for i in pascal_calc(i)]))
		
		triangle = triangle + (spaces_count//2)*' '
		triangle = triangle + ' '.join([str(i) for i in pascal_calc(i)])
		triangle = triangle + "\n"

	return triangle
		

############################
### Brugerens funktioner ###
############################
def permutationer() -> None:
	""" Brugerens funktion til at finde P(n, r).
	"""
	n = int(input("Hvad er dit n?\n").strip())
	r = int(input("Hvad er dit r?\n").strip())

	rep = input("Er det med repititioner (y/n)?\t(ikke det samme som indistinguishability)\n")

	if rep == 'y':
		print(f"\n{n}^{r} = {n**r}\n")

	elif rep == 'n':
		print(f"\nP({n}, {r}) = {permutations_calc(n, r)}\n")


def kombinationer() -> None:
	""" Brugerens funktion til at finde C(n, r).
	"""
	n = int(input("Hvor mange objekter er der?\n").strip())
	r = int(input("Hvor mange kasser er der?\n").strip())

	rep = input("Er det med repititioner (y/n)?\n")
	
	if rep == 'y':
		#types = int(input("Hvor mange typer objekter er der?\n").strip())

		print(f"\nC({n}+{r}-1, {n}) = {combinations_calc(n+r-1, n)}\n")

	elif rep == 'n':
		print(f"\nC({n}, {r}) = {combinations_calc(n, r)}\n")


def pascals_trekant():
	""" Brugerens funktion til at finde de første n rækker af
	eller den n'de række i Pascals trekant.
	"""
	
	mode = input("Hvilken mode vil du bruge?\nSkriv t hvis du vil have en trekant af de først n rækker.\nSkriv r hvis du kun vil have den n'de række.\n").strip()

	if mode != "t" and mode != "r":
		print("Ugyldig mode, prøv igen.")
		return

	n = int(input("Hvad er dit n?\n").strip())

	if mode == "t":
		print(f"\nDen {n}'de række i Pascals trekant er:\n")
		
		print(pascal_triangle(n))

	elif mode == "r":
		print(f"\nDen {n}'de række i Pascals trekant er:\n\n{' '.join([str(i) for i in pascal_calc(n)])}\n")


def distinguishability() -> None:
	""" Brugerens funktion til at udregne måder at fordele
	n objekter i k kasser, afhængigt af distinguishability.
	"""
	n = int(input("Hvor mange objekter er der?\n").strip())
	k = int(input("Hvor mange kasser er der?\n").strip())

	objects_dis = input("Er objekterne distinguishable? (y/n)\n").strip()

	if objects_dis not in ["y", "n"]:
		print("Ugyldigt svar på distinguishability, svar y eller n.")
		return

	boxes_dis = input("Er kasserne distinguishable? (y/n)\n").strip()

	if boxes_dis not in ["y", "n"]:
		print("Ugyldigt svar på distinguishability, svar y eller n.")
		return

	# Distinguishable objekter i indistinguishable kasser
	if objects_dis == "n" and boxes_dis == "y":
		print(f"\nDer er {combinations_calc(n+k-1, n)} måder at fordele {n} indistinguishable objekter i {k} distinguishable kasser.\n")

	# Indistinguishable objekter i distinguishable kasser
	elif objects_dis == "y" and boxes_dis == "n":
		
		supersum = 0

		for j in range(1, k+1):
			subsum = 0

			for i in range(j):
				subsum = subsum + (-1)**i * combinations_calc(j, i) * (j-i)**n

			supersum = supersum + (1/factorial(j)) * subsum

		print(f"\nDer er {int(supersum)} måder at fordele {n} distinguishable objekter i {k} indistinguishable kasser.\n")

	# Distinguishable objekter i distinguishable kasser
	elif objects_dis == "y" and boxes_dis == "y":
		print("Det er hurtigere at skrive formlen ind på en lommeregner.")
	
	# Indistinguishable objekter i indistinguishable kasser
	else:
		pass