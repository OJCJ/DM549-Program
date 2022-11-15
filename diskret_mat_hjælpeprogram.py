import os

########################
### Hjælpefunktioner ###
########################
def gcd_args(m: int, n: int) -> int:
	""" Finder gcd men med argumenter i stedet for brugerinput.
	Bruges når andre udregninger skal bruge gcd af to tal.
	"""
	while m != n:
		if m < n:
			n -= m
		else:
			m -= n

	return m


############################
### Brugerens funktioner ###
############################
def kongruenssystem():
	# x=y (mod m) -> m, M, y
	kongruensantal = input("Hvor mange kongruenser er der i dit system?\n")
	a_list = input("Skriv dine a-værdier, separeret af mellemrum (fx. for x=3 (mod 7) og x=9 (mod 5), giv 3 og 9):\n").strip().split(" ")
	m_list = input("Skriv dine m-værdier, separeret af mellemrum (fx. for x=3 (mod 7) og x=9 (mod 5), giv 7 og 5):\n").strip().split(" ")

def gcd() -> None:
	a = int(input("Hvad er dit a?\n"))
	b = int(input("Hvad er dit b?\n"))
	start_a = a
	start_b = b

	while a != b:
		if a < b:
			b -= a
		else:
			a -= b

	print(f"gcd({start_a},{start_b})={a}")

def lcm() -> None:
	a = int(input("Hvad er dit a?\n"))
	b = int(input("Hvad er dit b?\n"))
	
	print(f"\nlcm({a},{b})={abs(a*b)//gcd_args(a, b)}\n")

def multiplikativ_invers():
	invers = 1
	j = 1
	a = int(input("Hvad er dit a?\n"))
	m = int(input("Hvad er dit m?\n"))

	if gcd_args(a, m) != 1:
		print(f"{a} og {m} er ikke relativt primiske så der findes ikke en mulitplikativ invers til {a} modulus {m}.")
		return

	while invers*a-j*m != 1:
		if invers*a < j*m:
			invers = invers + 1
		else:
			j = j + 1

	print(f"\nDen multiplikative invers til {a} modulus {m} er {invers}.\n")

def løs_kongruens():
	pass

#############################
### Bruger interface kode ###
#############################
# id:[name, description, function]
function_dict = {
		"1":["Kongruenssystem", "For dit system af 'x=a (mod m)' kongruenser, find m, M og y værdier.", kongruenssystem],
		"2":["gcd", "Find gcd(a, b)", gcd],
		"3":["Multiplikativ invers", "Find den multiplikative invers til a modulus m.", multiplikativ_invers],
		"4":["Løs kongruens", "Find x for en kongruens ax=b (mod m).", løs_kongruens],
		"5":["lcm", "Find lcm(a, b)", lcm],
		}

longest_name = ""
for info in function_dict.values():
	name = info[0]
	if len(name) > len(longest_name):
		longest_name = name

def clear_terminal():
	"""
	Rydder terminalen på win, mac, og linux. TEST PÅ MAC OG LX
	"""
	command = 'clear'
	if os.name in ('nt', 'dos'):
		command = 'cls'
	os.system(command)

def print_functions():
	""" Printer funktionerne brugeren kan bruge i
	formattet -> id navn:	 beskrivelse.
	"""
	#print("Kommandoer:")
	print("-"*100)
	for f in function_dict.keys():
		print(f.ljust(3), function_dict[f][0], ":".ljust(6+len(longest_name)-len(function_dict[f][0])), function_dict[f][1], sep="")
		print("-"*100)
	print()

running = True
while running:
	clear_terminal()
	print_functions()
	cmd = input("Vælg en kommando til dit problem (fx. skriv 2 for gcd funktion): ")
	if cmd in function_dict.keys():
		function_dict[cmd][2]()
		input("Tryk enter for at vælge en ny kommando (bemærk: dette sletter dit sidste resultat).")
	else:
		print("Ups, det er ikke en valid kommando. Tryk enter for at prøve igen :)")
		input()