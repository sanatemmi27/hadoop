@outputSchema("hi_out:{(year:float,miles:float,vans:float,trucks:float)}")

def hi_miles(traff):
	year,kms,vans,trucks=traff.split(' ')
	miles = float(kms)*0.62
	return year,miles,vans,trucks
