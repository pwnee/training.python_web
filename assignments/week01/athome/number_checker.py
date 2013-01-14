def get_number():
	'''Prompts the user to input a number.  Will not be satisfied until a float or an int is passed'''
	while True:
		number = is_float_or_int(raw_input("Please enter a number: "))
		if not number:
			continue
		else:
			return number
			
def is_float_or_int(number):
	'''Checks to see whether the input is a number (float or int), returns the number or False if it is neither.'''
	try:
		if "." in number:
			number = float(number)
		else:
			number = int(number)		
	except ValueError:
		return False
	return number
	
def unit_tests():
	input = ["asdf.asdf","1","-1","1.0","-1.0","asdf","0","1.000003", "1230498", "-230845", "...", "1..0", ".5", ".00002347921"]	
	
	for i in input:
		print "Input:", i
		print "Output: ", is_float_or_int(i)
		print "The resulting type was: ", type(is_float_or_int(i))
		print "\n"
		
if __name__ == '__main__':
	#unit_tests()
	get_number()
	