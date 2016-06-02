def chessboard(size):
	return [[(row+col) % 2 for row in range(0,size)] for col in range(0,size)]

board = chessboard(4)
print(board)
