from os import *

def rc():
	name = "diaperd33r"
	style = "d33rfav"

	if style == "d33rfav":
		style = name + "@spsh $ "

	return name, style

def main():
	name, style = rc()

	cmd = input(style)


main()