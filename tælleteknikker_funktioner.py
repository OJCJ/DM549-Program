from functools import reduce

########################
### Hjælpefunktioner ###
########################
def factorial(n: int) -> int:
	""" Returnerer n!.
	"""
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

############################
### Brugerens funktioner ###
############################
def permutationer() -> None:
	""" Brugerens funktion til at finde P(n, r).
	"""
	n = int(input("Hvad er dit n?\n").strip())
	r = int(input("Hvad er dit r?\n").strip())

	print(f"\nP({n}, {r}) = {permutations_calc(n, r)}\n")

def kombinationer() -> None:
	""" Brugerens funktion til at finde C(n, r).
	"""
	n = int(input("Hvad er dit n?\n").strip())
	r = int(input("Hvad er dit r?\n").strip())

	print(f"\nC({n}, {r}) = {combinations_calc(n, r)}\n")

def pascal_række():
	""" Brugerens funktion til at finde den n'de række
	i Pascals trekant.
	"""
	n = int(input("Hvad er dit n?\n").strip())

	print(f"Den {n}'de række i Pascals trekant er:\n\n{' '.join([str(i) for i in pascal_calc(n)])}\n")