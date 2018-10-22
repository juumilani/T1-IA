
# TO-DO: descobrir como desenhar a interface e como rodam programas em python rs


# método recursivo que checa se o tabuleiro está completamente pronto ou não
def sudoku_pronto(tabuleiro)
	lin = 0
	col = 0

	# se o retorno da função lugar_disponivel for -1, significa que o tabuleiro está preenchido
	lin, col = lugar_disponivel(tabuleiro, lin, col)
	if lin == -1:
		return True


	# caso ele não esteja preenchido, vamos procurar um número pra colocar naquela posição
	for num in range(1,10):
		# se houver um lugar possivel, ele coloca o numero 
		if lugar_possivel(tabuleiro, lin, col, num):
			tabuleiro[lin][col] = num
			# chamada recursiva para testar o próximo numero
			if (sudoku_pronto(tabuleiro)):
				return True

			# caso o número falhe ele apaga o número da posição para o backtracking
			tabuleiro[lin][col] = '*'

	return False

# método que checa se é possível colocar um número na posição escolhida
def lugar_possivel(tabuleiro, linha, col, num):
	resultado = (	nao_conflito_lin(tabuleiro, lin, num)
					and nao_conflito_col(tabuleiro, col, num)
					and nao_conflito_caixa(tabuleiro, lin, col, num))
	return resultado

# esse método está procurando lugares vazios no tabuleiro de sudoku, caso encontre
# "disponivel" guarda as coordenadas desse lugar no tabuleiro e o método retorna true
def lugar_disponivel(tabuleiro, lin, col):
	for lin_aux in range(lin, 9):
		for col_aux in range(col, 9):
			if tabuleiro[lin_aux][col_aux] == '*':
				return lin_aux, col_aux

	for lin_aux in range(0,9):
		for col_aux in range(0,9):
			if tabuleiro[x][y] == '*':
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
			if tabuleiro[x][y] != num:
				return True
	return False
