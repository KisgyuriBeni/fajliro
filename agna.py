numbers = range(0, 10)

filename = "output_numbers.txt"

#w tells python we are opening the file to write into it
outfile = open(filename, 'w')

for number in numbers:
	outfile.write(str(number))

outfile.close() #Close the file when we’re done!