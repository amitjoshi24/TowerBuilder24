h = int(input("Enter desired tower height: "))

n = int(input("Enter number of types of blocks (number of block heights): "))

karr = {int(amit) for amit in input("Enter block heights, separated by a space: ").split(" ")}

n = len(karr)

from collections import deque, defaultdict

nextValues = deque()
fromValues = deque()

backtracked = defaultdict(lambda: -1)

visited = set()

for ki in karr:
	nextValues.append(ki)
	fromValues.append(0)

foundSolution = False
while len(nextValues) > 0:
	#print (len(backtracked))
	cur = nextValues.popleft()
	
	fromVal = fromValues.popleft()
	if cur in visited or cur > h:
		continue
	
	visited.add(cur)
	backtracked[cur] = fromVal

	if cur == h:
		foundSolution = True
		print ("A possible sequence of blocks that adds up to " + str(h) + " is: ", end = "")
		res = list()
		amit = cur
		while amit != -1:
			joshi = backtracked[amit]
			if joshi == -1:
				break
			difference = amit - joshi
			res.append(str(difference))
			amit = joshi

		print (" ".join(res))
		break

	for ki in karr:
		new = cur + ki
		if new not in visited and new <= h:
			nextValues.append(new)
			fromValues.append(cur)
if foundSolution == False:
	print ("No possible sequence of blocks of the specified heights can add up to:", h)



