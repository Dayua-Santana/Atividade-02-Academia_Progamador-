# 🏎️ Corrida Virtual: Player vs CPU (Interface Gráfica)

## 📝 Descrição do Projeto
Este projeto é um jogo de competição por turnos desenvolvido em Python. Ele simula uma corrida entre o usuário e o computador para atingir uma meta de 30 pontos. O grande diferencial desta versão é a substituição do terminal de texto por uma interface gráfica intuitiva baseada em janelas de interação (pop-ups).

---

## 🚀 Funcionalidades e Diferenciais
- **Interatividade Visual:** O jogador utiliza botões e caixas de diálogo para tomar decisões e acompanhar o progresso.
- **Lógica de Sorte e Recompensa:** Sistema de "casas especiais" que podem acelerar ou atrasar o competidor.
- **Mecânica de Turno Extra:** Implementação da regra do dado 6, onde o competidor que tira o valor máximo ganha um novo impulso.
- **Controle de Sessão:** O sistema permite que o usuário desista da corrida a qualquer momento de forma segura.

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Biblioteca de Interface:** PyAutoGUI (Responsável pelos menus e alertas visuais).
- **Biblioteca de Lógica:** Random (Utilizada para a geração aleatória dos movimentos).

---

## ⚙️ Como Instalar e Rodar
1. Baixe o código fonte do arquivo `.py`.
2. Certifique-se de ter o Python instalado em seu computador.
3. Instale a biblioteca necessária via terminal:
    pip install pyautogui
4. Execute o jogo com o comando:
    python nome_do_arquivo.py

## 📐 Lógica do Jogo 
O funcionamento da corrida segue critérios lógicos de movimentação:

Casas de Bônus (5, 10 e 15): Ao cair nestas posições, o competidor recebe um impulso extra de +3 casas.

Casas de Obstáculo (7, 13 e 20): Se o competidor parar nestas posições, ele sofre uma penalidade e recua -2 casas.

Regra do Dado Máximo: Se o jogador ou o PC tirar o número 6, ele ganha o direito de jogar novamente.

Critério de Vitória: O primeiro a somar 30 pontos ou mais é declarado o vencedor.
