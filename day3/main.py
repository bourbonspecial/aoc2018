size = 2000

grid = [[0 for __ in range(size)] for _ in range(size)]

with open('in.txt') as f:
	raw = f.read().split('\n')

for claim in raw:
	start_a = int(claim.split()[2].replace(':','').split(',')[0])
	start_b = int(claim.split()[2].replace(':','').split(',')[1])

	end_a = start_a + int(claim.split()[3].split('x')[0])
	end_b = start_b + int(claim.split()[3].split('x')[1])

	for i in range(start_a + 1, end_a + 1):
		for j in range(start_b + 1, end_b + 1):
			grid[i][j] += 1

for claim in raw:
	start_a = int(claim.split()[2].replace(':','').split(',')[0])
	start_b = int(claim.split()[2].replace(':','').split(',')[1])

	end_a = start_a + int(claim.split()[3].split('x')[0])
	end_b = start_b + int(claim.split()[3].split('x')[1])

	claim_sum = 0
	for i in range(start_a + 1, end_a + 1):
		for j in range(start_b + 1, end_b + 1):
			claim_sum += grid[i][j]

	if claim_sum == (end_a - start_a) * (end_b - start_b):
		print claim

# Part 1
# cnt = 0
# for r in grid:
# 	for c in r:
# 		if c == 1:
# 			cnt+= 1

