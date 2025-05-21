import chess
import chess.pgn
from stockfish import Stockfish

# path of Stockfish module
stockfishPath = r'path-to-stockfish-module\stockfish\stockfish-windows-x86-64-avx2.exe'  
stockfish = Stockfish(stockfishPath)
stockfish.set_skill_level(20)

# load a game from a .pgn file
gamePath = r'path-to-game-.pgn\partita2.pgn'
	
with open(gamePath) as f:
       	game = chess.pgn.read_game(f)

board = game.board()	#starts the game from the initial position
print(game)
print("\n")
print(board)
print("\n")

for move in game.mainline_moves():
	board.push(move)	# do the move on the chessboard
	print(board)
	print("\n")
	
	# analyse position with stockfish
	# it returns centipawn (cp) (+100 = white in little advance of 1 pawn, -50 = black in little advance of half pawn
	# arduino sends the FEN notation of the board, in this code is identified with board.fen()
	stockfish.set_fen_position(board.fen())
	score = stockfish.get_evaluation()

	print(f"the score is: {score['value']}, the move is: {move}\n")

if score['type'] == 'mate' :
	print("checkM8\n")

	print("end of the game\n")