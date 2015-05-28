import sys

def main():
	input = raw_input()
	input = input.split(" ")
	for x in input:
		if ( x == "2"):
			sys.stdout.write ("A")
		elif ( x == "22"):
			sys.stdout.write ("B")
		elif ( x == "222"):
			sys.stdout.write ("C")
		elif ( x == "3"):
			sys.stdout.write ("D")
		elif ( x == "33"):
			sys.stdout.write ("E")
		elif ( x == "333"):
			sys.stdout.write ("F")
		elif ( x == "4"):
			sys.stdout.write ("G")
		elif ( x == "44"):
			sys.stdout.write ("H")
		elif ( x == "444"):
			sys.stdout.write ("I")
		elif ( x == "5"):
			sys.stdout.write ("J")
		elif ( x == "55"):
			sys.stdout.write ("K")
		elif ( x == "555"):
			sys.stdout.write ("L")
		elif ( x == "6"):
			sys.stdout.write ("M")
		elif ( x == "66"):
			sys.stdout.write ("N")
		elif ( x == "666"):
			sys.stdout.write ("O")
		elif ( x == "7"):
			sys.stdout.write ("P")
		elif ( x == "77"):
			sys.stdout.write ("Q")
		elif ( x == "777"):
			sys.stdout.write ("R")
		elif ( x == "7777"):
			sys.stdout.write ("S")
		elif ( x == "8"):
			sys.stdout.write ("T")
		elif ( x == "88"):
			sys.stdout.write ("U")
		elif ( x == "888"):
			sys.stdout.write ("V")
		elif ( x == "9"):
			sys.stdout.write ("W")
		elif ( x == "99"):
			sys.stdout.write ("X")
		elif ( x == "999"):
			sys.stdout.write ("Y")
		elif ( x == "9999"):
			sys.stdout.write ("Z")	
		elif ( x == "0"):
			sys.stdout.write (" ")

	print "\n"
main()