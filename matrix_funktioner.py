from functools import reduce

########################
### Hjælpefunktioner ###
########################
def dimensions(m: list[list]) -> list[int]:
    """ Returnerer en liste med længden af alle elemter af m.
    >>> dimensions([[0, 0, 0], [0, 0], [0, 0, 0, 0, 0], [0], [0, 0, 0]])
    [3, 2, 5, 1, 3]
    """
    return list(map(lambda x: len(x), m))

def is_matrix(m: list[list]) -> bool:
	""" Returner om m er en matrix.
	"""
	return reduce(lambda x, y: x and y,
				  map(lambda x: x == len(m[0]),
					  dimensions(m)),
				  True)


def transpose(m: list[list]) -> list[list]:
	""" Returnere matricen m, transponeret.
	"""
	return [[m[column][row] for column in range(len(m))]
			for row in range(len(m[0]))]

def matrix_single_multiplication(v: list[int], w: list[int]) -> list[int]:
	""" Udfører multiplikationen for en enkelt plads i en matrix,
	hvor v er rækken fra den ene og w søjlen fra den anden.
	>>> matrix_single_multiplication([1, 2, 3, 4], [1, 2, 3, 4])
	30
	"""
	return sum([a*b for (a, b) in zip(v, w)])

def matrix_single_boolean_product(v: list[int], w: list[int]) -> list[int]:
	""" Udfører boolsk product for en enkelt plads i en matrix,
	hvor v er rækken fra den ene og w søjlen fra den anden.
	>>> matrix_single_multiplication([1, 2, 3, 4], [1, 2, 3, 4])
	30
	"""
	return sum([a and b for (a, b) in zip(v, w)]) > 0

############################
### Brugerens funktioner ###
############################
def matrix_multiplikation():
	A = input('''Angiv matricer sådan at hvis dette var din matrix
\t1 2 3
\t4 5 6
\t7 8 9
skulle du skrive "1 2 3,4 5 6,7 8 9."

Hvad er din matrix A?
''').strip()

	A = A.split(",")
	A = [[int(i) for i in a.split(" ")] for a in A]

	if not is_matrix(A):
		print("\nDen A du har givet er ikke en matrice.\n")
		return

	B = input("Hvad er din matrix B?\n").strip()
	B = B.split(",")
	B = [[int(i) for i in b.split(" ")] for b in B]

	if not is_matrix(B):
		print("\nDen B du har givet er ikke en matrice.\n")
		return

	if len(A[0]) != len(B):
		print("\nDe to matricer du har givet kan ikke multipliceres.\n")
		return

	B = transpose(B)

	result_matrix = []

	for a in A:
		row = []
		for b in B:
			row = row + [matrix_single_multiplication(a, b)]
		result_matrix = result_matrix + [row]

	print("\nDit AB =")
	for row in result_matrix:
		print("\t", end="")
		for n in row:
			print(f"{n} ", end="")
		print()


def boolsk_produkt():
	A = input('''Angiv matricer sådan at hvis dette var din matrix
\t1 0 0
\t1 0 1
\t0 1 1
skulle du skrive "1 0 0,1 0 1,0 1 1."

Hvad er din matrix A?
''').strip()
	A = A.split(",")
	A = [[int(i) for i in a.split(" ")] for a in A]

	if not is_matrix(A):
		print("\nDen A du har givet er ikke en matrice.\n")
		return

	B = input("Hvad er din matrix B?\n").strip()
	B = B.split(",")
	B = [[int(i) for i in b.split(" ")] for b in B]
	B = transpose(B)

	if not is_matrix(B):
		print("\nDen B du har givet er ikke en matrice.\n")
		return

	result_matrix = []

	for a in A:
		row = []
		for b in B:
			row = row + [matrix_single_multiplication(a, b)]
		result_matrix = result_matrix + [row]

	print("\nDit boolske produkt af A og B =")
	for row in result_matrix:
		print("\t", end="")
		for n in row:
			print(f"{n} ", end="")
		print()
		