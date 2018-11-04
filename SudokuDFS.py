
import os
import time

# método recursivo que checa se o tabuleiro está completamente pronto ou não
def sudoku_pronto(tabuleiro):
	lin = 0
	col = 0

	# se o retorno da função lugar_disponivel for -1, significa que o tabuleiro está preenchido
	lin, col = lugar_disponivel(tabuleiro, lin, col)
	if lin == -1:
		print("Sudoku resolvido: ")
		printa_tabuleiro(tabuleiro)
		return True


	# caso ele não esteja preenchido, vamos procurar um número pra colocar naquela posição
	for num in range(1,10):
		# se houver um lugar possivel, ele coloca o numero 
		if lugar_possivel(tabuleiro, lin, col, num):
			tabuleiro[lin][col] = num
			printa_tabuleiro(tabuleiro)
			time.sleep(0.5)
			os.system('clear')
			# chamada recursiva para testar o próximo numero
			if (sudoku_pronto(tabuleiro)):
				return True

			# caso o número falhe ele apaga o número da posição para o backtracking
			tabuleiro[lin][col] = 0
			print("Backtracking!")
			printa_tabuleiro(tabuleiro)
			time.sleep(0.5)
			os.system('clear')

	return False

# método que checa se é possível colocar um número na posição escolhida
def lugar_possivel(tabuleiro, lin, col, num):
	resultado = (	nao_conflito_lin(tabuleiro, lin, num)
					and nao_conflito_col(tabuleiro, col, num)
					and nao_conflito_caixa(tabuleiro, lin, col, num))
	return resultado

# esse método está procurando lugares vazios no tabuleiro de sudoku, caso encontre
# "disponivel" guarda as coordenadas desse lugar no tabuleiro e o método retorna true
def lugar_disponivel(tabuleiro, lin, col):
	for lin_aux in range(lin, 9):
		for col_aux in range(col, 9):
			if tabuleiro[lin_aux][col_aux] == 0:
				return lin_aux, col_aux

	for lin_aux in range(0,9):
		for col_aux in range(0,9):
			if tabuleiro[lin_aux][col_aux] == 0:
				return lin_aux, col_aux
		
	return -1, -1


# método que checa se há conflito na linha
def nao_conflito_lin(tabuleiro, lin, num):
	conflito_lin = all([num != tabuleiro[lin][x] for x in range (9)])
	return conflito_lin

# método que checa se há conflito na coluna
def nao_conflito_col(tabuleiro, col, num):
	conflito_col = all([num != tabuleiro[x][col] for x in range(9)])
	return conflito_col

# método que checa se há conflito na caixa 3x3
def nao_conflito_caixa(tabuleiro, lin, col, num):

	lin = 3*(lin//3)
	col = 3*(col//3)

	for x in range(lin, lin+3):
		for y in range(col, col+3):
			if tabuleiro[x][y] == num:
				return False
	return True

# método que printa o tabuleiro no console
def printa_tabuleiro(tabuleiro):

	print("----------------------")
	for lin in range(0, 9):
		if lin == 3 or lin == 6:
			print("----------------------")
		for col in range(0, 9):
			if col == 3 or col == 6:
				print("|", end=" ")
			print(tabuleiro[lin][col], end=" ")
		print()
	print("----------------------")

def main():
	Sudoku = [[0 for x in range(9)] for x in range(9)] 
	Sudoku[0][0] = 0
	Sudoku[0][1] = 0
	Sudoku[0][2] = 0
	Sudoku[0][3] = 3
	Sudoku[0][4] = 0
	Sudoku[0][5] = 0
	Sudoku[0][6] = 2
	Sudoku[0][7] = 0
	Sudoku[0][8] = 0
	Sudoku[1][0] = 0
	Sudoku[1][1] = 0
	Sudoku[1][2] = 0
	Sudoku[1][3] = 0
	Sudoku[1][4] = 0
	Sudoku[1][5] = 8
	Sudoku[1][6] = 0
	Sudoku[1][7] = 0
	Sudoku[1][8] = 0
	Sudoku[2][0] = 0
	Sudoku[2][1] = 7
	Sudoku[2][2] = 8
	Sudoku[2][3] = 0
	Sudoku[2][4] = 6
	Sudoku[2][5] = 0
	Sudoku[2][6] = 3
	Sudoku[2][7] = 4
	Sudoku[2][8] = 0
	Sudoku[3][0] = 0
	Sudoku[3][1] = 4
	Sudoku[3][2] = 2
	Sudoku[3][3] = 5
	Sudoku[3][4] = 1
	Sudoku[3][5] = 0
	Sudoku[3][6] = 0
	Sudoku[3][7] = 0
	Sudoku[3][8] = 0
	Sudoku[4][0] = 1
	Sudoku[4][1] = 0
	Sudoku[4][2] = 6
	Sudoku[4][3] = 0
	Sudoku[4][4] = 0
	Sudoku[4][5] = 0
	Sudoku[4][6] = 4
	Sudoku[4][7] = 0
	Sudoku[4][8] = 9
	Sudoku[5][0] = 0
	Sudoku[5][1] = 0
	Sudoku[5][2] = 0
	Sudoku[5][3] = 0
	Sudoku[5][4] = 8
	Sudoku[5][5] = 6
	Sudoku[5][6] = 1
	Sudoku[5][7] = 5
	Sudoku[5][8] = 0
	Sudoku[6][0] = 0
	Sudoku[6][1] = 3
	Sudoku[6][2] = 5
	Sudoku[6][3] = 0
	Sudoku[6][4] = 9
	Sudoku[6][5] = 0
	Sudoku[6][6] = 7
	Sudoku[6][7] = 6
	Sudoku[6][8] = 0
	Sudoku[7][0] = 0
	Sudoku[7][1] = 0
	Sudoku[7][2] = 0
	Sudoku[7][3] = 7
	Sudoku[7][4] = 0
	Sudoku[7][5] = 0
	Sudoku[7][6] = 0
	Sudoku[7][7] = 0
	Sudoku[7][8] = 0
	Sudoku[8][0] = 0
	Sudoku[8][1] = 0
	Sudoku[8][2] = 9
	Sudoku[8][3] = 0
	Sudoku[8][4] = 0
	Sudoku[8][5] = 5
	Sudoku[8][6] = 0
	Sudoku[8][7] = 0
	Sudoku[8][8] = 0

	printa_tabuleiro(Sudoku)
	sudoku_pronto(Sudoku)



if __name__ == '__main__':
	main()
