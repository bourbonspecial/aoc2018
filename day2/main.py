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

def sim(w1,w2):
	"""
	Calculate the similarity between two words. Assumed to be equal length.
	"""

	cnt = 0
	for i, c in enumerate(w1):
		if c == w2[i]:
			cnt += 1

	return cnt

# Shit algorithm. O(n^2), can only get away with it because the word list is short.
with open('in_real.txt') as f:
	raw = f.read().split('\n')

max_sim = 0

for w1 in raw:
	for w2 in raw:
		if not w1 == w2:
			s = sim(w1,w2)
			if s >= max_sim:
				max_sim = s
				print w1, w2, s