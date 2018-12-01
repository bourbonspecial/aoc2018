def summer(inp):
	return sum([int(x) for x in inp.replace('+','').split('\n')])

def main():
	with open('in.txt') as f:
		print summer(f.read())

if __name__ == '__main__':
	main()