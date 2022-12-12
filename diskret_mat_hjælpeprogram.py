import os
from talteori_funktioner import *
from matrix_funktioner import *
from tælleteknikker_funktioner import *

# id:[name, description, function]
function_dict = {
		"1":["Kongruenssystem", "For dit system af 'x≡a (mod m)' kongruenser, find m, M og y værdier.", kongruenssystem],
		"2":["gcd", "Find gcd(a, b)", gcd],
		"3":["Multiplikativ invers", "Find den multiplikative invers til a modulus m.", multiplikativ_invers],
		"4":["Løs kongruens", "Find x for en kongruens ax≡b (mod m).", løs_kongruens],
		"5":["lcm", "Find lcm(a, b)", lcm],
		"6":["Delelighed", "Går a op i b? Hvis man ikke lige kan regne det ud i hovedet.", delelighed],
		"7":["Primtal", "Er x et primtal?", primtal],
		"8":["Matrix multiplikation", "Udregn resultatet af at multiplicere to matricer A og B.", matrix_multiplikation],
		"9":["Boolsk produkt", "Udregn det boolske produkt af to matricer A og B.", boolsk_produkt],
		"10":["Permutationer", "Udregn P(n, r).", permutationer],
		"11":["Kombinationer", "Udregn C(n, r); n choose r.", kombinationer],
		"12":["Pascals trekant", "Find en eller flere rækker af Pascals trekant.", pascals_trekant]
		}

longest_name = ""
for info in function_dict.values():
	name = info[0]
	if len(name) > len(longest_name):
		longest_name = name

def clear_terminal() -> None:
	"""
	Rydder terminalen på win, mac, og linux. (Testet på win 10/11, mac og ubuntu)
	"""
	command = 'clear'
	if os.name in ('nt', 'dos'):
		command = 'cls'
	os.system(command)

def print_functions() -> None:
	""" Printer funktionerne brugeren kan bruge i
	formattet -> id navn:	 beskrivelse.
	"""
	print("-"*100)
	for f in function_dict.keys():
		print(f.ljust(3), function_dict[f][0], ":".ljust(6+len(longest_name)-len(function_dict[f][0])), function_dict[f][1], sep="")
		print("-"*100)
	print()

running = True
while running:
	clear_terminal()
	print_functions()
	cmd = input("Vælg en kommando til dit problem (fx. skriv 2 for gcd funktion): ").strip()
	if cmd in function_dict.keys():
		function_dict[cmd][2]()
		input("Tryk enter for at vælge en ny kommando (bemærk: dette sletter dit sidste resultat).")
	else:
		input("Ups, det er ikke en valid kommando. Tryk enter for at prøve igen :)")