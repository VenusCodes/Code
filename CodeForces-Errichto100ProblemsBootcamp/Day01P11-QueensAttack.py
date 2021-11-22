#
#		these is not working
#

n,q = map(int,input().split())
chess_board = [[[0]*n]*n]
positions = []
for i in range(q):
	row,col = map(int,input().split())
	positions.append([row,col])
	#check if attacking any position or not
	#check the position itself
	#position allowed flag
	


	#check if the diagonals are occupied or not
	diagonal_occupied = 0
	# upper left diagonal it      ====> the diagonal that goes \
	ul_row,ul_col = row,col
	while( ul_row!=-1 or ul_col!=-1):
		if chess_board[ul_row][ul_col] == 1:
			diagonal_occupied = 1
			break
		ul_row -= 1
		ul_col -= 1
	# lower right diagonal ====> the diagonal that goes \
	lr_row,lr_col = row,col
	while(lr_row!=(n-1) or lr_col!=(n-1)):
		if chess_board[lr_row][lr_col] == 1:
			diagonal_occupied = 1
			break
		lr_row +=1
		lr_col +=1
	#upper right diagonal =====> the diagonal that goes /
	ur_row,ur_col = row,col
	while(ur_row!=0 or ur_col!=(n-1)):
		if chess_board[ur_row][ur_col] == 1:
			diagonal_occupied = 1
			break
		lr_row -=1
		lr_col +=1
	#lower left diagonal ======> the diagonal that goes /
	ll_row,ll_col = row,col
	while(ll_row!=0 or ll_col!=(n-1)):
		if chess_board[ll_row][ll_col] == 1:
			diagonal_occupied = 1
			break
		ll_row +=1
		ll_col -=1

	#check the row_status
	row_status = 0
	i = 0
	while(i!=(n-1)):
		if chess_board[i][col] == 1:
			row_status = 1
			break
		i +=1

	#check the col_status
	col_status = 0
	i = 0
	while(i!=(n-1)):
		if chess_board[row][i] == 1:
			col_status = 1
			break
		i +=1	

	# position itself , row , col , diagonal
	if ((chess_board[row][col] == 1) or (row_status == 1 or col_status ==1) or (diagonal_occupied ==1 )):
		print('NO')

	else:
		print('YES')

		#fill the row & col
		for i in range(n):
			chess_board[i][col] = 1
			chess_board[row][i] = 1

		#fill the \ ul diagonal
		ul_row,ul_col = row,col
		while( ul_row!=0 or ul_col!=0):
			chess_board[ul_row][ul_col] = 1
		
		# lower right diagonal ====> the diagonal that goes \
		lr_row,lr_col = row,col
		while(lr_row!=(n-1) or lr_col!=(n-1)):
			chess_board[lr_row][lr_col] = 1
		
		#upper right diagonal =====> the diagonal that goes /
		ur_row,ur_col = row,col
		while(ur_row!=0 or ur_col!=(n-1)):
			chess_board[ur_row][ur_col] = 1
	
		#lower left diagonal ======> the diagonal that goes /
		ll_row,ll_col = row,col
		while(ll_row!=0 or ll_col!=(n-1)):
			chess_board[ll_row][ll_col] = 1