import numpy as np 
import pygame
import sys
import math
ROW_COUNT = 6
COLUMN_COUNT = 7

YELLOW = (255,255,100)
WIGHT = (240,240,240)
RED = (255,0,0)
BLACK = (0,0,0)

game_over = False
turn = 0


	# create a matrix of zeros to represent the board
def create_board():
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board


	# checks if the choosen column is valid
def is_valid_location(board, place):
	return board[ROW_COUNT - 1,place] == 0


	# where in column to put the coin
def get_available_hole(board, place):
	for r in range(ROW_COUNT):
		if board[r][place] == 0 :
			return r


	# putting the coin
def drop_coin(board, row, col, coin):
	board[row][col] = coin


def show_board(board):
	print(np.flip(board, 0))

def winning_move(board, piece):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True



def draw_board(board):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, YELLOW, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, WIGHT, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()

board = create_board()
show_board(board)

pygame.init()

SQUARESIZE = 100
myfont = pygame.font.SysFont('malgungothic',75)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)
RADIUS = int(SQUARESIZE / 2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, WIGHT,(0,0,width,SQUARESIZE))
			posx = pygame.mouse.get_pos()
			if turn == 0:
				pygame.draw.circle(screen, RED,(posx[0], int(SQUARESIZE/2)), RADIUS)
			else:
				pygame.draw.circle(screen, BLACK,(posx[0], int(SQUARESIZE/2)), RADIUS)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, WIGHT,(0,0,width,SQUARESIZE))
			# getting player1 place to put the coin
			if turn == 0:
				posx = pygame.mouse.get_pos()
				place = int(math.floor(posx[0]/ SQUARESIZE))

				if is_valid_location(board, place):
					row = get_available_hole(board, place)
					drop_coin(board, row, place, 1)
					
					if winning_move(board, 1):
						label = myfont.render("PLAYERS 1 WINS !!!!",1,RED)
						screen.blit(label,(40,10))
						game_over = True
			
			
			# getting player2 place to put the coin
			else:
				posx = pygame.mouse.get_pos()
				place = int(math.floor(posx[0]/ SQUARESIZE))

				if is_valid_location(board, place):
					row = get_available_hole(board, place)
					drop_coin(board, row, place, 2)
					
					if winning_move(board, 2):
						label = myfont.render("PLAYERS 2 WINS !!!!",1,BLACK)
						screen.blit(label,(40,10))
						game_over = True


			show_board(board)
			draw_board(board)
			# to switch the turn between the two players
			turn += 1
			turn = turn % 2
			if game_over:
					pygame.time.wait(3000)






pygame.draw.rect()