### TODO: PREENCHA SUAS INFORMAÇÕES AQUI ###
# Nome #01 (quem entregou o código): Richard Henrique Dias Lima    [NOME COMPLETO #01] 
# RA #01 (quem entregou o código): 286263   [RA #01]
# Nome #02: Alice Fonseca dos Santos                            [NOME COMPLETO #02]
# RA #02: 233883          [RA #02]
from basic_players import Player
from judge import card_value

# Implemente neste arquivo seus jogadores para Truco

# Jogador que não faz nada. Substitua esta classe para criar as suas, devem herdar da classe Player
class NonePlayer(Player):
    # Se estiver dúvida sobre como começar olhe os players prontos em basic_players.py e o ReadMe
    def __init__(self):
        super().__init__(0, "CLT") # Nome do Jogador
           
    def adversario_gastou_manilha(self, play_hist, top_card):#adversario gastou manilha
        if not play_hist:
            return False
        minha_dupla = (self.position, (self.position + 2) % 4)
        for jogador, carta, _ in play_hist[-1]:
            if jogador not in minha_dupla:
                if card_value(carta, top_card) >= 1000:
                    return True
        return False    
    
    def cartas_fortes(self, top_card):#se tem cartas fortes
        fortes = 0
        for rank, suit in self.cards:
            if card_value((rank, suit), top_card) >= 1000:
                fortes += 1
            elif rank in ('3', '2'):
                fortes += 1
        return fortes 
    
    def empatou(self, play_hist, top_card):#se o primeiro round empatou
        # Ainda não terminaram as 4 jogadas da primeira rodada
        if len(play_hist) == 0 or len(play_hist[-1]) < 4:
            return False
        minha_dupla = (self.position, (self.position + 2) % 4)
        maior_minha = 0
        maior_adversario = 0
        # Apenas as jogadas da primeira rodada
        for jogador, carta, _ in play_hist[-1][:4]:
            valor = card_value(carta, top_card)
            if jogador in minha_dupla:
                if valor > maior_minha:
                    maior_minha = valor
            else:
                if valor > maior_adversario:
                    maior_adversario = valor
        return maior_minha == maior_adversario
    
    def ganhou_primeira(self, play_hist, top_card):#Descobre se minha dupla venceu a primeira rodada.
        if len(play_hist) == 0 or len(play_hist[-1]) < 4:
            return False
        minha_dupla = (self.position, (self.position + 2) % 4)
        maior_minha = 0
        maior_adversario = 0
        for jogador, carta, _ in play_hist[-1][:4]:
            valor = card_value(carta, top_card)
            if jogador in minha_dupla:
                if valor > maior_minha:
                    maior_minha = valor
            else:
                if valor > maior_adversario:
                    maior_adversario = valor
        return maior_minha > maior_adversario 
    
    def joga_por_ultimo(self, play_hist):# se eu jogo por ultimo
        if not play_hist:
            return False
        return len(play_hist[-1]) == 3
    
    def melhor_carta(self, top_card): #Retorna a melhor carta da mão.
        melhor = self.cards[0]
        maior_valor = card_value(melhor, top_card)
        for carta in self.cards:
            valor = card_value(carta, top_card)
            if valor>maior_valor:
                melhor = carta
                maior_valor = valor
        return melhor        

    def parceiro_esta_ganhando(self, play_hist, top_card):# se o parceiro jogou carta forte
        if not play_hist:
            return False
        rodada = play_hist[-1]
        if len(rodada) != 3:
            return False
        vencedor = None
        maior = -1
        for jogador, carta, _ in rodada:
            valor = card_value(carta, top_card)
            if valor > maior:
                maior = valor
                vencedor = jogador
        parceiro = (self.position + 2) % 4
        return vencedor == parceiro
    
    def meu_placar(self, score_hist):#descobre meu placar
        return score_hist[-1][self.position % 2]
    
    def placar_adversario(self, score_hist):#analisa placar do adversario
        return score_hist[-1][(self.position + 1) % 2]
    
    def pior_carta(self, top_card):#Retorna a pior carta da mão.
        pior = self.cards[0]
        menor_valor = card_value(pior, top_card)
        for carta in self.cards:
            valor = card_value(carta, top_card)
            if valor< menor_valor:
                pior = carta
                menor_valor = valor
        return pior        

    def pode_trucar(self, play_hist, score_hist):#se posso trucar
        if self.meu_placar(score_hist) == 12 or self.placar_adversario(score_hist) == 12:
            return False
        if not play_hist:
            return True
        minha_dupla = (self.position, (self.position + 2) % 4)
        # Procura o último pedido de truco
        for jogador, _, acao in reversed(play_hist[-1]):
            if acao in (3, 6, 9):# Se foi minha dupla que pediu, não posso pedir novamente
                return jogador not in minha_dupla
        # Nunca houve pedido de truco
        return True
    
    def perdeu_primeira(self, play_hist, top_card):# se perdeu o primeiro round
        # Ainda não terminou a primeira rodada
        if len(play_hist) == 0 or len(play_hist[-1]) < 4:
            return False
        minha_dupla = (self.position, (self.position + 2) % 4)
        maior_minha = 0
        maior_adversario = 0
        # Apenas as 4 jogadas da primeira rodada
        for jogador, carta, _ in play_hist[-1][:4]:
            valor = card_value(carta, top_card)
            if jogador in minha_dupla:
                if valor > maior_minha:
                    maior_minha = valor
            else:
                if valor > maior_adversario:
                    maior_adversario = valor
        return maior_adversario > maior_minha
    
    def truco_no_comeco(self, play_hist):#se adversario trucou no inicio
        if not play_hist or len(play_hist[-1]) == 0:
            return False
        _, _, acao = play_hist[-1][0]
        return acao in (3,6,9)

    def tem_casal(self, top_card):#Se tem duas manilhas
        casal = 0
        for carta in self.cards:
            if card_value(carta, top_card) >= 1000:
                casal += 1
        return casal >= 2
    
    def ultima_carta(self):#Retorna True quando resta apenas uma carta.
        return len(self.cards) == 1
    
        
    # Função para retornar o que você vai jogar em determinada mão
    def play(self, top_card, play_hist, score_hist):
        # Tratamentos de erro
        if not self.cards:
            return 1, None
        melhor = self.melhor_carta(top_card)
        pior = self.pior_carta(top_card)
        # Trucar quando tiver carta forte/casal
        if self.pode_trucar(play_hist, score_hist):
            if self.tem_casal(top_card):
                return 2, melhor
            if self.cartas_fortes(top_card) >= 3:
                return 2, melhor
        # Se perdeu a primeira rodada, tenta recuperar
        if self.perdeu_primeira(play_hist, top_card):
            return 1, melhor
        # Se ganhou a primeira, economiza carta boa
        if self.ganhou_primeira(play_hist, top_card):
            return 1, pior
        #Se empatou a primeira, joga a mais forte
        if self.joga_por_ultimo(play_hist):
            if self.parceiro_esta_ganhando(play_hist, top_card):
                return 1, pior
        if self.adversario_gastou_manilha(play_hist, top_card):#se adversario gfastou manilha, economizo carta
            return 1, pior    
        if self.empatou(play_hist, top_card):#se empatou, joga a melhor
            if self.pode_trucar(play_hist, score_hist) and self.cartas_fortes(top_card) >= 2:
                return 2, melhor
            return 1, melhor
        if self.ultima_carta():#ultima carta, joga a melhor
            return 1, melhor  
        # Estratégia padrão
        return 1, pior
        
        
    # Função para retornar o que você vai dar de resposta a trucos
    def respond(self, top_card, play_hist, score_hist):
        #Tratamento de erro
        if not self.cards:
            return 0     
        if self.truco_no_comeco(play_hist):#Se so tiver carta fraca, corro do truco
            if self.cartas_fortes(top_card) == 0:
                return 0
        if self.meu_placar(score_hist) >= 9:#se meu placar 
            if self.cartas_fortes(top_card) >= 2:
                return 1
            return 0
        # Se empatou, joga mais forte
        if self.empatou(play_hist, top_card):
            if self.tem_casal(top_card):
                return 2
            return 1
        # Casal forte
        if self.tem_casal(top_card):
            return 2
        # Uma carta muito forte
        if self.cartas_fortes(top_card) >= 1:
            return 1
        # Mão ruim   
        return 0


# Função que define o nome da dupla:
def pair_name():
    return "É os Profis"  # Defina aqui o nome da sua dupla


# Função que cria a dupla:
def create_pair():
    return (NonePlayer(), NonePlayer())  # Defina aqui a dupla de jogadores. Deve ser uma tupla com dois jogadores.
