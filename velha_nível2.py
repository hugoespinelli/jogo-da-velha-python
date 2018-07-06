import random
import velha_nível1

#-------------------------------------------------------------------------------
# Funções utilizadas pelo programa 
#-------------------------------------------------------------------------------

# função que verifica filas com fechamento iminente.
# caso não encontre uma:
#      retorna zero
# caso contrário:
#      retorna a casa que bloqueia o fechamento
#-------------------------------------------------------------------------------

class VelhaMedio(velha_nível1.VelhaFacil):

    pesosFilas = ''    


    def __init__(self):
        super(VelhaMedio, self).__init__()
        self.pesosFilas = { 11: [3, [self.lins[0], self.cols[0], self.dgns[0]]],
                   12: [2, [self.lins[0], self.cols[1]]],
                   13: [3, [self.lins[0], self.cols[2], self.dgns[1]]],
                   21: [2, [self.lins[1], self.cols[0]]],
                   22: [4, [self.lins[1], self.cols[1], self.dgns[0], self.dgns[1]]],
                   23: [2, [self.lins[1], self.cols[2]]],
                   31: [3, [self.lins[2], self.cols[0], self.dgns[1]]],
                   32: [2, [self.lins[2], self.cols[1]]],
                   33: [3, [self.lins[2], self.cols[2], self.dgns[0]]]
                 }

    # função que obtém lance do computador
    #-------------------------------------------------------------------------------
    def processaLanceComputador(self):
        
        # contabiliza jogada do computador
        self.jogada += 1
        # verifica fechamento iminente do computador
        casa = self.fechamentoIminente('O')
        # verifica fechamento iminente do jogador
        if casa == 0:
            casa = self.fechamentoIminente('X')
        # se não fechou, escolhe casa com maior peso
        if casa == 0:
            casa = self.melhorCasa()
        # elimina casa escolhida da relação das casas disponíveis
        self.casasDisponíveis.remove(casa)
        # atualiza tabuleiro
        self.tabuleiro[casa//10-1][casa%10-1] = 'O'
        
        self.filas = self.atualizaFilas()
        return casa;
    

    def fechamentoIminente(self, oponente):
        global pesosFilas

        if oponente == 'X': jogador = 'O'
        else:               jogador = 'X'
        
        # verifica fechamento iminente nas linhas
        # e retorna a casa que bloqueia o fechamento
        for linha in self.lins:
            if linha.count(oponente) == 2 and linha.count(jogador) == 0:
                lin_idx = self.lins.index(linha) + 1
                col_idx = linha.index(' ') + 1
                casa = lin_idx*10 + col_idx
                # pesosFilas[casa][0] = 0
                return casa

        # verifica fechamento iminente nas colunas e
        # retorna casa que bloqueia o fechamento
        for coluna in self.cols:
            if coluna.count(oponente) == 2 and coluna.count(jogador) == 0:
                lin_idx = coluna.index(' ') + 1
                col_idx = self.cols.index(coluna) + 1
                casa = lin_idx*10 + col_idx
                # pesosFilas[casa][0] = 0
                return casa

        # verifica fechamento iminente nas diagonais e
        # retorna casa que bloqueia o fechamento
        for diagonal in self.dgns:
            if diagonal.count(oponente) == 2 and diagonal.count(jogador) == 0:
                dgn_idx = self.dgns.index(diagonal) + 1
                lin_idx = diagonal.index(' ') + 1
                if dgn_idx == 1:
                    col_idx = lin_idx
                else:
                    col_idx = 4 - lin_idx
                casa = lin_idx*10 + col_idx
                # pesosFilas[casa][0] = 0
                return casa

        # retorna zero se não houver fechamento iminente
        return 0

    # função que seleciona a melhor casa para jogada do computador
    #-------------------------------------------------------------------------------
    def melhorCasa(self):
        self.reponderaTabuleiro()
        # procura casa do tabuleiro com o maior peso
        maiorPeso = 0
        for casa in self.casasDisponíveis:
            peso  = self.pesosFilas[casa][0]
            if peso > maiorPeso: maiorPeso = peso
        self.pesosFilas[casa][0] = maiorPeso
        return casa

    def reponderaTabuleiro(self):
        
        for casa in self.casasDisponíveis:
            peso  = self.pesosFilas[casa][0]
            self.filas = self.pesosFilas[casa][1]
            for fila in self.filas:
                if 'X' in fila: self.pesosFilas[casa][0] = peso - 1

    def limpaJogo(self):
        super(VelhaMedio ,self).limpaJogo();
        self.pesosFilas = { 11: [3, [self.lins[0], self.cols[0], self.dgns[0]]],
                   12: [2, [self.lins[0], self.cols[1]]],
                   13: [3, [self.lins[0], self.cols[2], self.dgns[1]]],
                   21: [2, [self.lins[1], self.cols[0]]],
                   22: [4, [self.lins[1], self.cols[1], self.dgns[0], self.dgns[1]]],
                   23: [2, [self.lins[1], self.cols[2]]],
                   31: [3, [self.lins[2], self.cols[0], self.dgns[1]]],
                   32: [2, [self.lins[2], self.cols[1]]],
                   33: [3, [self.lins[2], self.cols[2], self.dgns[0]]]
                 }
        
