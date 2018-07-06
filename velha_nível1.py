import random

#-------------------------------------------------------------------------------
# Funções utilizadas pelo programa 
#-------------------------------------------------------------------------------

# função que atualiza a estrutura de dados que representa as filas de fechamento
#-------------------------------------------------------------------------------
class VelhaFacil(object):
    # inicializa a estrutura de dados que representa o tabuleiro
    tabuleiro = [[' ']*3, [' ']*3, [' ']*3]

    # define e inicializa a estrutura de dados que representa os padrões de fechamento
    fechamentos = [3*['X'], 3*['O']]
    casasDisponíveis = ''

    # seta a condição de encerramento do jogo
    jogada = False
    fechou = 0
    terminar = False

    lins = ''
    cols = ''
    dgns = ''
    filas = ''
    
    def __init__ (self):
        # inicializa a estrutura de dados que representa as filas de fechamento
        self.filas = self.atualizaFilas();
        # cria lista de casas disponíveis para lance
        self.casasDisponíveis = [i*10+j for i in range(1,4) \
                                   for j in range(1,4) \
                                       if self.tabuleiro[i-1][j-1] == ' ']
        
        

    def atualizaFilas(self):
           
        self.lins = [linha for linha in self.tabuleiro]

        self.cols = [
                [self.tabuleiro[linha][0] for linha in range(3)], \
                [self.tabuleiro[linha][1] for linha in range(3)], \
                [self.tabuleiro[linha][2] for linha in range(3)]  \
               ]

        self.dgns = [
                [self.tabuleiro[linha][linha]  for linha in range(3)],
                [self.tabuleiro[linha][coluna] for linha in range(3)
                                              for coluna in range(3)
                                                  if (linha+coluna) == 2]
               ]

        return(self.lins + self.cols + self.dgns)

    # função que verifica o fechamento do jogo
    #-------------------------------------------------------------------------------
    def verificaFechamento(self):

        self.filas = self.atualizaFilas()

        contador = 0

        # seta indicador de fechamento
        for fila in self.filas:
            if fila in self.fechamentos:
                status = True
                break
        else:
            status = False

        return status


    def pegaPosicaoFechamento(self):
        contador = 0
        fila_fechamento = []
        for fila in self.filas:
            contador += 1
            if fila in self.fechamentos:
                break;
        posicao = ''
        if(contador <= 3):
            posicao = 'linha';
        elif (contador > 3 and contador <= 6):
            posicao = 'coluna';
        else:
            posicao = 'diagonal';

        if(posicao == 'linha'):
           for i in range(0, 3):
               fila_fechamento.append(i+1+10*contador);
        if(posicao == 'coluna'):
            contador = contador - 3
            for i in range(0, 3):
               fila_fechamento.append(10*(i+1)+1*contador);

        if(posicao == 'diagonal'):
            if(contador == 7):
                fila_fechamento.append(11);
                fila_fechamento.append(22);
                fila_fechamento.append(33);
            else:
                fila_fechamento.append(31);
                fila_fechamento.append(22);
                fila_fechamento.append(13);
               
        return fila_fechamento;
        

    # função que obtém e processa lance do jogador
    #-------------------------------------------------------------------------------
    def processaLanceJogador(self, casa):

        # contabiliza jogada do jogador
        self.jogada += 1
        # exibe lista de casas disponíveis
        # print('\nNo momento, o tabuleiro está com as seguintes casas disponíveis:\n', \
              # self.casasDisponíveis, '\n')

        self.casasDisponíveis.remove(casa)
        
        # atualiza tabuleiro
        self.tabuleiro[casa//10-1][casa%10-1] = 'X'

        # atualiza a estrutura de dados que representa as filas de fechamento
        self.filas = self.atualizaFilas()

    # função que obtém lance do computador
    #-------------------------------------------------------------------------------
    def processaLanceComputador(self):
        
        # contabiliza jogada do computador
        self.jogada += 1
        # gera lance do computador
        casa = random.choice(self.casasDisponíveis)
        # elimina casa escolhida da relação das casas disponíveis
        self.casasDisponíveis.remove(casa)
        # atualiza tabuleiro
        self.tabuleiro[casa//10-1][casa%10-1] = 'O'
        # atualiza a estrutura de dados que representa as filas de fechamento
        self.filas = self.atualizaFilas()

        return casa;

    # função que exibe o tabuleiro
    #-------------------------------------------------------------------------------
    def exibeTabuleiro(self):
        print()
        print(' ' + self.tabuleiro[0][0] + ' |' + ' ' + self.tabuleiro[0][1] + ' |' + ' ' + self.tabuleiro[0][2] + ' \n' \
              '---+---+---\n' \
              ' ' + self.tabuleiro[1][0] + ' |' + ' ' + self.tabuleiro[1][1] + ' |' + ' ' + self.tabuleiro[1][2] + ' \n' \
              '---+---+---\n' \
              ' ' + self.tabuleiro[2][0] + ' |' + ' ' + self.tabuleiro[2][1] + ' |' + ' ' + self.tabuleiro[2][2] + ' \n' )
        

    def verificaSeJogadorGanhou(self):
        # em caso de fechamento, verifica vencedor e emite mensagem correspondente:
        print(self.jogada);
        # se o vencedor for o jogador:
        if self.jogada in [1, 3, 5, 7, 9] and not self.deuVelha():
            return True;
        # se o vencedor for o computador:
        else:
            return False;

    def deuVelha(self):
        if(not self.verificaFechamento() and self.jogada == 9):
            return True;
        return False;

    def limpaJogo(self):
        self.tabuleiro = [[' ']*3, [' ']*3, [' ']*3]
        self.fechamentos = [3*['X'], 3*['O']]
        self.casasDisponíveis = ''
        self.jogada = False
        self.fechou = 0
        self.terminar = False
        self.lins = ''
        self.cols = ''
        self.dgns = ''
        filas = self.atualizaFilas();
        # cria lista de casas disponíveis para lance
        self.casasDisponíveis = [i*10+j for i in range(1,4) \
                                   for j in range(1,4) \
                                       if self.tabuleiro[i-1][j-1] == ' ']
    

