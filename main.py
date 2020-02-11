

print('Wecome to sudoku')
puzzle = [[8, 7, 6, 9, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 6, 0, 0, 0], [0, 4, 0, 3, 0, 5, 8, 0, 0], [4, 0, 0, 0, 0, 0, 2, 1, 0], [0, 9, 0, 5, 0, 0, 0, 0, 0], [0, 5, 0, 0, 4, 0, 3, 0, 6], [0, 2, 9, 0, 0, 0, 0, 0, 8], [0, 0, 4, 6, 9, 0, 1, 7, 3], [0, 0, 0, 0, 0, 1, 0, 0, 4]]

count = 0
for i in range(len(puzzle)):
	if count > 0:
		print()
	for j in range(len(puzzle[i])):
		print(puzzle[i][j], end = ' ')
	count +=1

