from random import choice
player_win = 0
pc_win = 0

def option_player():
    esc_jogador = input('escolha Pedra, Papel ou Tesoura: ')
    esc_jogador.lower()
    if esc_jogador == 'pedra':
        return esc_jogador
    elif esc_jogador == 'papel':
        return esc_jogador
    elif  esc_jogador == 'tesoura':
        return esc_jogador
    else: 
        print('opção inválida, tente novamente')
        option_player()
    
def option_pc():
    esc_pc = choice(['pedra','papel', 'tesoura'])
    return esc_pc
    
    
while True:
    print('-'*30)
    esc_jogador = option_player()
    esc_pc = option_pc()
    print('-'*30)

    if (esc_jogador == 'pedra') and (esc_pc == 'tesoura') \
        or (esc_jogador == 'papel') and (esc_pc == 'pedra') \
            or (esc_jogador == 'tesoura') and (esc_pc == 'papel'):
                #jogador ganha 
                print(f'jogador escolheu {esc_jogador} e o  jogador 2 escolheu{esc_pc}'
                "você ganhou :D")
                player_win += 1
    elif esc_pc == esc_jogador: 
        #empate
        print(f'jogador escolheu {esc_jogador} e o  jogador 2 escolheu {esc_pc}'
                "Empate :l")
    
    else: 
        #maquina ganha
        
        print(f'jogador escolheu {esc_jogador} e o  jogador 2 escolheu {esc_pc}'
                "Você Perdeu :(")
        pc_win += 1
    print('-'*30)
    print(f'player win: {player_win}')
    print(f'machine win: {pc_win}')
    print('-'*30)
    esc_jogador = input('você quer jogar novamente ?')
    if esc_jogador in ['SIM', 'Sim', 'sim', 'S', 's']:
        pass 
    elif esc_jogadorin ['NAO','Nao', 'nao', 'N ', 'n']:
        break
    else:
        break