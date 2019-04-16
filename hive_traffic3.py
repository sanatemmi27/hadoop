import sys
import string

while True:
	line = sys.stdin.readline()
	if not line:
		break
	row = string.strip(line,'\n')
	year,kms,vans,trucks = string.split(row,'\t')
	totalfreight = float(vans)+float(trucks)
	print'\t'.join([year,kms,str(totalfreight)])

