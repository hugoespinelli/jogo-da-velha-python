from tkinter import *
import velha_nível1
import velha_nível2
import velha_nível3
import time

class Jogo(object):
    # Tamanho da tela
    LARGURA = 200;
    ALTURA = 300;

    # Tamanho dos botões
    TAMANHO_GRADE = 8;

    butoes = {};
    velha = None;
    tempo = 0
    deuVelha = False

    def __init__(self):
        self.root = Tk()
        self.root.geometry('%ix%i' % (self.LARGURA, self.ALTURA))
        self.root.title('Jogo da Velha')
        
        self.renderizaTelaEntrada()

        self.root.mainloop()

    def timer(self):
        self.tempo += 1
        texto = 'Tempo de partida: '+str(self.tempo)+'s'
        if(self.tempo != 1 and not self.deuVelha):
            self.timer_label.forget();
        if(not self.deuVelha):
            self.timer_label = Label(self.frame_principal, text = texto, pady=5)
            self.timer_label.pack()
            self.root.after(1000, self.timer);
        
        
    def renderizaTelaEntrada(self):
        self.frame=Frame(pady = 50)
        self.frame.pack()
        self.l = Label(self.frame, text = 'Bem vindo ao jogo da velha!', pady = 5)
        self.l.pack()
        self.l2 = Label(self.frame, text = 'Escolhe a opção desejada:')
        self.l2.pack()
        self.b_facil = Button(self.frame, text = 'Facil', width=10,command = lambda: self.renderizaJogoPrincipal('Facil'))
        self.b_medio = Button(self.frame, text = 'Medio', width=10,command = lambda: self.renderizaJogoPrincipal('Medio'))
        self.b_dificil = Button(self.frame, text = 'Dificil', width=10, command = lambda: self.renderizaJogoPrincipal('Dificil'))
        self.b_facil.pack()
        self.b_medio.pack()
        self.b_dificil.pack()

    def apagaTelaEntrada(self):
        self.frame.pack_forget();

    def carregaJogoDificuldade(self, nivel):
        if(nivel == "Facil"):
            return velha_nível1.VelhaFacil();
        if(nivel == "Medio"):
            return velha_nível2.VelhaMedio();
        if(nivel == "Dificil"):
            return velha_nível3.VelhaDificil();

    def renderizaJogoPrincipal(self, nivel):
        self.apagaTelaEntrada()
        self.nivel = nivel
        self.velha = self.carregaJogoDificuldade(nivel)
        self.velha.limpaJogo();
        self.frame_principal = Frame(pady = 30)
        self.frame_principal.pack()
        
        # Cria Botões
        for linha in range(1,4):
            self.frame_coluna=Frame(self.frame_principal)
            self.frame_coluna.pack()
            for coluna in range(1,4):
                posicao = linha*10 + coluna
                b = Button(self.frame_coluna, text = '  ',
                                padx = self.TAMANHO_GRADE*2,
                                pady = self.TAMANHO_GRADE,
                                width = 2)
                self.butoes[posicao] = b
                self.butoes[posicao]['command'] = lambda posicao = posicao: self.marcaJogada(posicao, 'X')
                b.pack(side = LEFT);

        self.timer()

                
    def marcaJogada(self, posicao, simbolo):
        self.butoes[posicao]['text'] = simbolo;
        self.butoes[posicao]['command'] = '';
        self.velha.processaLanceJogador(posicao);

        print(self.velha.verificaFechamento())
        
        if self.velha.verificaFechamento() or self.velha.deuVelha():
            self.terminaJogo();
            return
    
        
        jogada_computador = self.velha.processaLanceComputador();
        self.butoes[jogada_computador]['command'] = '';
        self.butoes[jogada_computador]['text'] = 'O';
        
        if self.velha.verificaFechamento():
            self.terminaJogo();
            return

    def terminaJogo(self):
        mensagem = ''
        velha = self.velha.deuVelha()
        
        if self.velha.verificaSeJogadorGanhou():
            mensagem += 'Parabéns, voce ganhou!'
        elif velha:
            mensagem += 'Deu velha!'
        else:
            mensagem += 'O Computador e melhor haha!'

        self.coloreFilaFechamento(mensagem)
        self.deuVelha = True
            
        l = Label(self.frame_principal, text= 'Jogo encerrado!', pady = 15)
        l = Label(self.frame_principal, text= mensagem, pady = 10)
        self.b = Button(self.frame_principal, text = 'Quero jogar de novo!', command = self.novoJogo)
        l.pack();
        self.retiraAcaoDosButoes();
        self.b.pack()

    def coloreFilaFechamento(self, mensagem):
        if(mensagem != 'Deu velha!'):
            if(mensagem == 'Parabéns, voce ganhou!'):
                cor = '#80ff80';
            if(mensagem == 'O Computador e melhor haha!'):
                cor = '#ff8566'
            posicao_fechamento = self.velha.pegaPosicaoFechamento()
            for pos in posicao_fechamento:
                self.butoes[pos]['bg'] = cor

    def retiraAcaoDosButoes(self):
        for bt in self.butoes:
            self.butoes[bt]['command']= ''
            
    def novoJogo(self):
        self.tempo = 0
        self.deuVelha = False
        self.frame_principal.destroy();
        self.renderizaJogoPrincipal(self.nivel)
              
Jogo()
