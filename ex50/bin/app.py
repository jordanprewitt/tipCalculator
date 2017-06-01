#assertEqual


def totalCost(meal, tip):
	tipPercent = .2
	total = meal + (meal*tipPercent)
	print "Your total bill is: %d" %total
#	if meal == 10:
#		return "Success: " + str(tip)
#	if meal <10:
#		return "Success: " +str(tip)
#	else:
#		return "Success: " +str(tip)
	


def assertEqual(expected, actual):
	if (expected != actual):
		print "Failed. Expected "  + str(expected) + " but found " + str(actual)
	else:
		print "."
		

assertEqual(3,2)





totalCost(15,.2)
totalCost(5.99, .21)

assertEqual(13.944,13.944)
assertEqual(11,11)
assertEqual(12.0, 10+10*.2)
assertEqual(12, 6+6)



