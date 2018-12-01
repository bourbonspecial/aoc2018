def summer(inp):
	return sum([int(x) for x in inp.replace('+','').split('\n')])

def counter(inp):
	s = 0
	dupe = None
	clean = [int(x) for x in inp.replace('+','').split('\n')]

	counter = {}

	while not dupe:
		for i in clean:
			if s in counter:
				dupe = s
				print dupe
				break
			else:
				counter[s] = 0

			s += i

def main():
	with open('in.txt') as f:
		counter(f.read())

if __name__ == '__main__':
	main()