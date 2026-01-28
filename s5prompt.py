import numpy as np
from astropy.table import Table

def main():

	#x values:
	x = np.linspace(0,2* np.pi,1000)

	#sin(x):
	sin_x = np.sin(x)

	#table:
	table = Table()
	table['x'] = x
	table['sin(x)'] = sin_x

	print(table)

if __name__ == "__main__":
	main()