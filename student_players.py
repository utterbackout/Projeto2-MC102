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
        
    def melhor_carta(self, top_card):
        """Retorna a melhor carta da mão."""
        pass

    def pior_carta(self, top_card):
        """Retorna a pior carta da mão."""
        pass

    def valor_carta(self, carta, top_card):
        """Retorna a força de uma carta."""
        pass

    def cartas_fortes(self, top_card):
        """
        Conta quantas cartas fortes existem na mão.
        Exemplo:
        - manilhas
        - 3
        - 2
        """
        pass

    def tem_casal(self, top_card):
        """
        Verifica se possui um casal (duas cartas fortes).
        """
        pass

    def pode_trucar(self, play_hist, score_hist):
        """
        Verifica se ainda é possível pedir truco.
        """
        pass

    def ganhou_primeira(self, play_hist, top_card):
        """
        Descobre se minha dupla venceu a primeira rodada.
        """
        pass

    def perdeu_primeira(self, play_hist, top_card):
        """
        Descobre se minha dupla perdeu a primeira rodada.
        """
        pass

    def ultima_carta(self):
        """
        Retorna True quando resta apenas uma carta.
        """
        return len(self.cards) == 1    
    
    # Função para retornar o que você vai jogar em determinada mão
    def play(self, top_card, play_hist, score_hist):
        # Tratamentos de erro
        if not self.cards:
            return 1, None
        melhor = self.melhor_carta(top_card)
        pior = self.pior_carta(top_card)
        # Estratégia 1
        # Casal forte -> pedir truco
        if self.tem_casal(top_card):
            if self.pode_trucar(play_hist, score_hist):
                return 2, melhor
        # Estratégia 2
        # Se perdeu a primeira rodada, tenta recuperar
        if self.perdeu_primeira(play_hist, top_card):
            return 1, melhor
        # Estratégia 3
        # Se ganhou a primeira, economiza carta boa
        if self.ganhou_primeira(play_hist, top_card):
            return 1, pior
        # Estratégia padrão
        return 1, pior
        
    # Função para retornar o que você vai dar de resposta a trucos
    def respond(self, top_card, play_hist, score_hist):
        # Sem cartas
        if not self.cards:
            return 0
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


'''
play()
0 = jogar encoberta
1 = jogar normalmente
2 = pedir truco

respond():
0 = correr

1 = aceitar

2 = aumentar
'''