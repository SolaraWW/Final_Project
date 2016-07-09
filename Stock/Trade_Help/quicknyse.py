handle = 'AMEX.txt'
fh = open(handle).read().splitlines()
AMEX = []

for line in fh:
    line=line.split()
    AMEX.append(line[0])

print AMEX



