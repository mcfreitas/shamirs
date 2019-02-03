from fractions import Fraction 
from random import randint as rand

def split(val, n, k):
	# val is the secret (the value when x = 0).
	# n is the number of points to distribute.
	# k is the number of points needed to reconstruct the polynomial.
	# Return a list of n random points such that x != 0 for every point.
	
	points = []
	rval = []

	for h in range(k-1):
		r = rand(-100,100)
		rval.append(r)
	
	for i in range(1, n+1):
		x = i
		y = val

		for j in range(1, k):
			degree = j
			term = rval[j-1]*(x**degree)
			y = y + term

		points.append((x,y))

	return points

def interpolate(points, x):
	# points is a list of shares.
	# x is the x-coordinate in which to compute the secret at.
	# Return the computed secret value.
	xlist = []
	ylist = []

	for count, (xval, yval) in enumerate(points):
		xlist.append(xval)
		ylist.append(yval)


	num = []
	den = []

	#subtract all x-val's besides the current xval from 0
	#multiply these numbers all together and add to
	#the list of numerator values
	for c in range(count + 1):
		currx = xlist[c]
		xlist.remove(xlist[c])
		prod = 1
		for xval in xlist:
			prod *= (x-xval)
		prod *= ylist[c]
		num.append(prod)
		xlist.insert(c, currx)

	#subtract all xval's from the current xval 
	#multiply these numbers all together and add to
	#the list of denominator values
	for c in range(count + 1):
		currx = xlist[c]
		xlist.remove(xlist[c])
		prod = 1
		for xval in xlist:
			prod *= (currx-xval)
		den.append(prod)
		xlist.insert(c, currx)

	#compute the secret value 
	f = 0
	for i in range(len(num)):
		f += Fraction(num[i], den[i])
	
	return f



	
