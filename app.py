import random
import pyautogui as pg

def jogar():
    posicao_jogador = 0
    posicao_computador = 0
    meta = 30

    pg.alert(text=f"Bem-vindo à Corrida Virtual!\nObjetivo: Chegar na posição {meta}", title="Início da Corrida")

    while posicao_jogador < meta and posicao_computador < meta:
        
        # --- TURNO DO JOGADOR ---
        escolha = pg.confirm(text=f"Sua posição: {posicao_jogador}\nPosição PC: {posicao_computador}\n\nDeseja rolar o dado?", 
                            title="Sua Vez", buttons=['Rolar Dado', 'Desistir'])
        
        if escolha == 'Desistir' or escolha is None:
            pg.alert("Você abandonou a corrida!")
            return

        dado = random.randint(1, 6)
        posicao_jogador += dado 
        msg_jogador = f"Você tirou: {dado}\nNova posição: {posicao_jogador}"
        
        # Eventos especiais do Jogador
        if posicao_jogador in [5, 10, 15]:
            msg_jogador += "\n\n>> BÔNUS! Avançou +3 casas."
            posicao_jogador += 3
        elif posicao_jogador in [7, 13, 20]:
            msg_jogador += "\n\n>> QUE CHATO! Recuou -2 casas."
            posicao_jogador -= 2
        
        pg.alert(text=msg_jogador, title="Resultado da sua jogada")

        if posicao_jogador >= meta:
            break
        
        if dado == 6:
            pg.alert(">> SORTE! Tirou 6 e joga novamente!")
            continue

        # --- TURNO DO COMPUTADOR ---
        pg.alert("Agora é a vez do Computador...", title="Turno do PC", button="OK")
        
        dado_pc = random.randint(1, 6)
        posicao_computador += dado_pc
        msg_pc = f"O PC tirou: {dado_pc}\nPosição do PC: {posicao_computador}"

        if posicao_computador in [5, 10, 15]:
            posicao_computador += 3
            msg_pc += "\n>> PC ganhou bônus de +3."
        elif posicao_computador in [7, 13, 20]:
            posicao_computador -= 2
            msg_pc += "\n>> PC recuou -2."

        pg.alert(text=msg_pc, title="Resultado do Computador")

    # --- FIM DA CORRIDA ---
    if posicao_jogador >= meta:
        pg.alert(text=f"🏆 PARABÉNS! Você venceu a corrida!\nPlacar Final: {posicao_jogador} vs {posicao_computador}", title="Vitória!")
    else:
        pg.alert(text=f"💻 O Computador venceu.\nPlacar Final: {posicao_computador} vs {posicao_jogador}", title="Derrota")

if __name__ == "__main__":
    jogar()