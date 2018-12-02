from collections import Counter

def checksum(inp):
	with open(inp) as f:
		raw = f.read().split('\n')

	two_count = 0
	three_count = 0

	for i in raw:
		c = Counter()
		for char in i:
			c[char] += 1

		for k in c:
			if c[k] == 2:
				two_count += 1
				break

		for k in c:
			if c[k] == 3:
				three_count += 1
				break

	return two_count * three_count

print checksum('in_real.txt')