import os
from matematik_funktioner import *

# id:[name, description, function]
function_dict = {
		"1":["Kongruenssystem", "For dit system af 'x=a (mod m)' kongruenser, find m, M og y værdier.", kongruenssystem],
		"2":["gcd", "Find gcd(a, b)", gcd],
		"3":["Multiplikativ invers", "Find den multiplikative invers til a modulus m.", multiplikativ_invers],
		"4":["Løs kongruens", "Find x for en kongruens ax=b (mod m).", løs_kongruens],
		"5":["lcm", "Find lcm(a, b)", lcm],
		"6":["Delelighed", "Går a op i b? Hvis man ikke lige kan regne det ud i hovedet.", delelighed],
		"7":["Matrix multiplikation", "Udregn resultatet af at multiplicere to matricer A og B.", matrix_multiplikation],
		"8":["Boolsk produkt", "Udregn det boolske produkt af to matricer A og B.", boolsk_produkt]
		}

longest_name = ""
for info in function_dict.values():
	name = info[0]
	if len(name) > len(longest_name):
		longest_name = name

def clear_terminal():
	"""
	Rydder terminalen på win, mac, og linux.
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
	cmd = input("Vælg en kommando til dit problem (fx. skriv 2 for gcd funktion): ").strip()
	if cmd in function_dict.keys():
		function_dict[cmd][2]()
		input("Tryk enter for at vælge en ny kommando (bemærk: dette sletter dit sidste resultat).")
	else:
		print("Ups, det er ikke en valid kommando. Tryk enter for at prøve igen :)")
		input()