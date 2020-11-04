import random
from time import sleep
import sys

#Versão 1.1

#Texto dos numeros invalido
erro = "\nDigite um numero valido!"

def style(x): #Função que estiliza o texto
    for char in x: #X é considerado o texto
        sys.stdout.write(char)
        sys.stdout.flush()
        if char == "\n": #Quando encontra um paragrafo adiciona um timer a mais
            sleep(0.0)
        if char == ".": #Quando encontra um ponto adiciona um timer prolongado
            sleep(0.0)
        else: #Caso seja um texto comum ele passa rapido
            sleep(0.00)

def morte(): #Função de morte
    print("\033[31m\n"+10*"="+" VOCÊ MORREU "+10*"=") #Titulo
    while(True): #Loop da tela de morte
        try: #Caso o usuario não insira um numero inteiro
            print("\033[31m")
            style(texto[28])
            style(texto[29])
            print("[1] - Sim")
            print("[2] - Não")
            continuar = int(input("Escolha: ")) #Entrada da escolha de continuar
            print(33*"=")
            print("\033[m") #Fim da cor vermelha
            if continuar == 1: #Continuar no jogo
                continuar = 0 #Volta a variavel continuar a 0 novamente
                break #Quebra o loop da tela de morte
            elif continuar == 2: #Fechar o jogo
                continuar = 0 #Volta a variavel continuar a 0 novamente
                print("\nFechando...")
                exit() #Encerra
            else:
                print(erro) #Retorna ao loop Morte
        except ValueError:
                print(erro) #Retorna ao loop Morte

#Array dos textos
texto = [1 for y in range(155)] #Cria 138 arrays na variavel texto

#Tutorial
print("\033[36m\n"+10*"="+" Tutorial "+10*"=")
print("Para jogar é simples, digite o numero de sua escolha e confirme com [ENTER]")
print("Suas escolhas impactam na história e nos personagens")
print("Em alguns momentos, sua sorte também terá um impacto\n")
print("OBS: Não é possivel pular os textos\033[m")

#Titulo
print("\n"+10*"="+" Undead Nightmare "+10*"=")

#Incialização
while(True): #Inicio do loop Start
    print("\033[34m\nDigite [ENTER] para iniciar")
    start = str(input()) #Entrada do Start
    if start == "": #Caso o jogador tenha pressionado enter
        print("Carregando...\033[m")
        break #Fim do loop Start

#Variavel da contagem de Mortes
mortes = 0

#Variavel da reputação da criança e seu nome
rep_crianca = 0
crianca = "Criança"

#Narração1
texto[1] = "\n*Na calada da noite, você ouve um estrondo* \n\
*BOOOOOOOOOOM* \n\
*Quando você desce as escadas de sua casa e abre a porta da frente, você vê pessoas se atacando*\n"
style(texto[1])

#Choice1
texto[2] = "*Você tenta afastar as brigas* \n\
*Tentado afastar, você acaba vendo uma pessoa caida no chão... morta* \n\
*Seu estômago começa a se revirar*"

texto[3] = "\n*Você tentar passar pela briga procurando por alguem que possa ajudar* \n\
*Você acaba levando alguns empurrões e logo em seguida uma paulada na cabeça* \n\
*Sua cabeça começa a doer*"

while(True): #Loop do choice1
    try: #Caso o usuario não insira um numero inteiro
        print()
        print(25*"=")
        print("[1] - Tentar afastar a multidão")
        print("[2] - Tentar passar pela briga e pedir por ajuda")
        choice1 = int(input("Escolha: ")) #Entrada da Choice1
        print(25*"=")
        if choice1 == 1: #[1] - Tentar afastar a multidão
            print()
            style(texto[2])
            break #Fim do loop Choice1
        if choice1 == 2: #[2] - Tentar passar pela briga e pedir por ajuda
            style(texto[3])
            break #Fim do loop Choice1
        else:
            print(erro) #Retorna ao inicio do loop Choice1
    except ValueError:
        print(25*"=")
        print(erro) #Retorna ao inicio do loop Choice1

#Narração2
texto[4] = "\n*Você percebe alguns soldados proximos* \n\
*Um deles, olha em sua direção* \n\
Soldado: VAI PARA O CAMINHÃO AGORA!! \n\
*Ao olhar para o lado você ve algumas pessoas desesperadas perto do caminhão*\n"
style(texto[4])

#Choice2
texto[5] = "Soldado: NÃO ME IGNORE, ISSO É UMA ORDEM!! \n\
*Você se sente pressionado e resolve ir para o caminhão*"

texto[6] = "\n*Você resolve seguir as ordens do soldado e ir ao caminhão*"

while(True): #Incio do loop choice2
    try: #Caso o usuario não insira um numero inteiro
        print()
        print(25*"=")
        print("[1] - Ignorar o soldado")
        print("[2] - Obedecer o soldado")
        choice2 = int(input("Escolha: ")) #Entrada da Choice2
        print(25*"=")
        if choice2 == 1: #[1] - Ignorar o soldado
            print()
            style(texto[5])
            break #Fim do loop choice2
        if choice2 == 2: #[2] - Obedecer o soldado
            style(texto[6])
            break #Fim do loop choice2
        else:
            print(erro)
    except ValueError:
        print(25*"=")
        print(erro) #Retorna ao inicio do loop Choice2

#Narração 3
texto[7] = "\n*Chegando perto, você vê pessoas assustadas entrando no caminhão* \n\
*Você entra, estranhando tudo o que esta acontecendo* \n\
\n*Curioso, você resolve perguntar para o motorista para aonde estão indo* \n\
*O motorista não responde...* \n\
*Durante a viagem, você nota pessoas chorando, algumas com sangue em suas roupas* \n\
\n*Após algumas horas, o caminhão para em uma base militar* \n\
*Você percebe que todos os adultos entre 20 a 30 anos estão sendo levados a uma enorme fila* \n\
*Você é colocado nela*\n"
style(texto[7])

#Choice3
texto[8] = "*Após algumas poucas horas na fila, você finalmente chega ao que parece uma barraca*"

texto[9] = "*Ao tentar fugir você é barrado pelo próprio general que o convida para uma conversa* \n\
*Você então é levado ao que parece uma barraca*" 

while(True): #Incio do loop Choice3
    try: #Caso o usuario não insira um numero inteiro
        print()
        print(25*"=")
        print("[1] - Continuar na fila")
        print("[2] - Tentar escapar")
        choice3 = int(input("Escolha: ")) #Entrada da Choice3
        print(25*"=")
        if choice3 == 1: #[1] - Continuar na fila
            print()
            style(texto[8])
            break #Fim do loop Choice3
        if choice3 == 2: #[2] - Tentar escapar
            print()
            style(texto[9])
            break #Fim do loop Choice3
        else:
            print(erro) #Retorna ao inicio do loop Choice3
    except ValueError:
        print(25*"=")
        print(erro)

#Narração 4
texto[10] = "\n*Nessa barraca a alguns soldados com alguns papeis, fazendo varias anotações* \n\
\n*Quando chega a sua vez, o general 'Souza' lhe entrega uma ficha para você preencher* \n\
*A ficha aparenta ser uma convocação do exercito* \n\
*Ao te entregar, o general te explica toda a situação* \n\
\n*Uma pandemia se iniciou* \n\
*As pessoas infectadas atacam as pessoas comuns* \n\
*O general então sai da barraca e deixa a ficha em suas mãos* \n\
\n*Você nota naquele momento que possui um papel muito importante*\n"

style(texto[10])

#Nome do jogador
texto[11] = "Insira o seu nome na ficha: "

choice_name = 0 #Variavel para confirmação do nome
while(True): #Incio do loop
    try: #Caso o usuario não insira um numero inteiro
        print("")
        print(25*"=")
        style(texto[11])
        nome = input() #Pede o nome do jogador
        print(25*"=")
        if nome == "": #Caso o jogador não coloque nada
            print("Insira um nome valido!\n")
        else: #Verificação
            texto[12] = f"\nVocê se chama {nome}?\n"
            style(texto[12])
            print("[1] - Sim")
            print("[2] - Não")
            choice_name = int(input("Escolha: ")) #Escolha da verificação do nome
            print(25*"=")
            if choice_name == 1: #Caso Sim
                texto[13] = f"\n*Você coloca {nome} como seu nome na ficha de inscrição*"
                style(texto[13])
                break #Fim do loop do nome
            elif choice_name == 2: #Caso Não ele retorna a pergunta
                print()
            else:
                print(erro) #Retorna ao inicio do loop Choice_Name
    except ValueError:
        print(25*"=")
        print(erro)

#Narração 5
texto[15] = "\n** Um mês após a inscrição ** \n\
\n*O mundo foi dominado pelo virus* \n\
*As pessoas acordam todos os dias esperando por uma cura* \n\
\n*Voltando para o dormitório a noite* \n\
*Seus amigos estão sentados, planejando algo* \n\
*Ao se aproximar, você percebe que eles planejam roubar um pouco de comida* \n\
*Com fome, o que você faz?*\n"
style(texto[15])

#Choice4
texto[16] = "\n*Vocês decidem roubar*"

texto[17] = "\n*Ao tentarem roubar, os soldados percebem vocês* \n\
*Vocês voltam para o dormitório com dores pelos esporros* \n\
*e agora sabem que vão passar 1 semana com trabalhos extras* \n\
\n*Você acorda com dores no corpo todo*"

texto[18] = "\n*Após o roubo bem-sucedido, vocês comemoram no dormitório com duas garrafas de saquê* \n\
\n*Você acorda de ressaca*"

texto[19] = "\n*Você decide ficar no dormitório e não se envolver*"

texto[20] = "\n*Após algum tempo, você acorda com o barulho da porta se abrindo* \n\
*Você vê seus amigos feridos* \n\
*Neste momento você agradeçe por não ter ido* \n\
\n*Você acorda*"

texto[21] = "\n*Seus amigos comemoram a conquista e zombam de você por não ter ido* \n\
\n*Você acorda*"
#variavel aleatoria para decidir as chances do roubo (10%)
roubo1 = random.randint(1,10)

while(True): #Incio do loop Choice4
    try: #Caso o usuario não insira um numero inteiro
        print()
        print(25*"=")
        print("[1] - Roubar a cantina")
        print("[2] - Ignorar e ir dormir")
        choice4 = int(input("Escolha: ")) #Entrada da Choice4
        print(25*"=")
        if choice4 == 1: #[1] - Roubar a cantina
            style(texto[16])
            if roubo1 == 1: #Caso o numero decidido pelo PC seja 1
                style(texto[17])
                break #Fim do loop choice4
            elif roubo1 >= 2 and roubo1 <= 10: #Caso o numero decidido pelo PC seja entre 2 e 10
                style(texto[18])
                break #Fim do loop choice4
            else: #Caso o numero do pc ultrapasse os valores impostos
                print(f"Erro: Valor do 'roubo1' diferente do que deveria: {roubo1}")
        if choice4 == 2: #[2] - Ignorar e ir dormir
            print()
            style(texto[19])
            if roubo1 == 1: #Caso o numero decidido pelo PC seja 1
                style(texto[20])
                break #Fim do loop choice4
            elif roubo1 >= 2 and roubo1 <= 10: #Caso o numero decidido pelo PC seja entre 2 e 10
                style(texto[21])
                break #Fim do loop choice4
            else: #Caso o numero do pc ultrapasse os valores impostos
                print(f"Erro: Valor do 'roubo1' diferente do que deveria: {roubo1}")
        else:
            print(erro) #Retorna ao inicio do loop Choice4
    except ValueError:
        print(25*"=")
        print(erro)

#Narração 5
texto[22] = "\n*Após se arrumar, você encontra seu pelotão no helicóptero para ir a uma missão de resgate* \n\
\n*Chegando no destino você e seu grupo notam que no local não há nenhum sinal de vida* \n\
*Vocês por comando do capitão descem em uma rua, e começam a vasculhar a área* \n\
\n*Você e seu parçeiro entram em uma das casas da rua, enquanto os outros soldados entram nas outras* \n\
*A casa parece diferente das outras, essa casa esta mais organizada* \n\
*Ao começar a subir as escadas, vocês acabam encontrando um morto-vivo, ele se vira derrepente para vocês e começa a descer*\n"
style(texto[22])

#Choice5
choice5_loop = 0 #Criado pois existem escolhas dentro de escolhas
texto[23] = "Usar a faca ou a arma?\n"

texto[24] = "\n*Você se arma com sua faca e espera o zumbi descer para mata-lo* \n\
*O zumbi então tropeça e cai das escadas, você aproveita essa oportunidade e o elimina*"

texto[25] = f"\n*Você puxa sua Glock e mira no zumbi* \n\
*Atirando nele, você acaba fazendo um grande barulho no local* \n\
\nParçeiro: Por que você atirou {nome}? A gente tem que ser rapido, isso pode atrair mais! \n\
{nome}: Ele estava indo nos atacar!"

texto[26] = "\n*Você relata ao capitão com seu radio, o capitão então manda você dar cabo ao morto-vivo* \n\
*O morto vivo então, desajeitado, acaba tropeçando de cima das escadas e caindo em cima de você*"

texto[27] = "\n*Você tenta puxar sua faca, mas ela cai de suas mãos.* \n\
\n*Na tentativa de empurrar o zumbi ele acaba mordendo seu pescoço.*"

texto[28] = f"{nome} não desista!\n"

texto[29] = "Deseja Continuar?\n"

texto[30] = "\n*Você puxa sua faca rapidamente e acerta o zumbi, o eliminando ali*\n"

while choice5_loop == 0: #Incio do loop choice5
    try: #Caso o usuario não insira um numero inteiro
        print()
        print(25*"=")
        print("[1] - Matar o morto-vivo")
        print("[2] - Relatar ao capitão")
        choice5 = int(input("Escolha: ")) #Entrada da choice5
        print(25*"=")
        if choice5 == 1: #[1] - Matar o morto-vivo
            while(True): #Inicio do loop arma1
                try: #Caso o usuario não insira um numero inteiro
                    print()
                    print(25*"=")
                    style(texto[23])
                    print("[1] - Faca")
                    print("[2] - Arma")
                    arma1 = int(input("Escolha: ")) #Entrada da escolha de armas do jogador
                    print(25*"=")
                    if arma1 == 1: #[1] - Faca
                        style(texto[24])
                        choice5_loop = 1 #Fim do loop choice5
                        break #Fim do loop arma1
                    if arma1 == 2: #[2] - Arma
                        style(texto[25])
                        choice5_loop = 1 #Fim do loop choice5
                        break #Fim do loop arma1
                    else:
                        print(erro) #Retorna ao inicio do loop arma1
                except ValueError:
                    print(25*"=")
                    print(erro)
        elif choice5 == 2: #[2] - Relatar ao capitão
            print()
            style(texto[26])
            survival1 = random.randint(1,2) #Chances de sobrevivencia decidida pelo pc (50%)
            if survival1 == 1: #Caso o PC decida o numero 1
                style(texto[27])
                mortes = mortes + 1 #Adiciona +1 ao numero de mortes
                choice5 = 0
                morte()
            elif survival1 == 2: #Caso o PC decida o numero 2
                arma1 = 1 #Resgistra Como se o usuario escolhesse usar a arma
                style(texto[30])
                break #Fim do loop Choice5
            else:
                print(f"Erro: Valor da variavel 'survival1' invalido: {survival1}") #Caso a variavel survival1 seja diferente do esperado
        else:
            print(erro) #Retorna ao inicio do loop Choice5
    except ValueError:
        print(25*"=")
        print(erro)

#Narração 6
texto[31] = "\n*Após mata-lo, vocês sobem as escadas e vasculham os quartos* \n\
\n*Dentro de um deles, há uma criança um pouco assustada* \n\
*Aparentemente ela estava escondida do zumbi*\n"
style(texto[31])

#Choice6
texto[32] = "\n*A criança diz seu pai tentou ataca-la* \n\
*Você então acalma a criança e a leva para o helicóptero* \n\
\n** A criança se sente melhor **"

texto[33] = "\n*Você sem muitas perguntas, chama a criança e a leva para o helicóptero* \n\
\n** A criança esta indiferente em relação a você **"

while(True): #Incio do loop Choice6
    try: #Caso o usuario não insira um numero inteiro
        print()
        print(25*"=")
        print("[1] - Perguntar a criança se há alguem com ela")
        print("[2] - Leva-la ao helicóptero")
        choice6 = int(input("Escolha: ")) #Entrada da choice6
        print(25*"=")
        if choice6 == 1: #[1] - Perguntar a criança se há alguem com ela
            style(texto[32])
            rep_crianca = rep_crianca + 1 #Aumenta a reputação da criança
            break #Fim do loop Choice6
        if choice6 == 2: #[2] - Leva-la ao helicóptero
            style(texto[33])
            break #Fim do loop Choice6
        else:
            print(erro) #Retorna ao inicio do loop Choice6
    except ValueError:
        print(25*"=")
        print(erro)
        

#Narração 7
texto[34] = "\n*Indo ao helicóptero, vocês esperam os outros soldados terminarem a missão*"
style(texto[34])

#Textos if arma
texto[35] = "\nPiloto: O que aconteceu la dentro? Escutamos um tiro!\n"

texto[36] = f"\n{nome}: Não fomos nós que atiramos... \n\
Piloto: Estranho... talvez tenha sido os outros soldados."

texto[37] = f"\n{nome}: Não fomos nós que atiramos! \n\
Piloto: Olha, sabemos que foram vocês... só não façam mais isso."

texto[38] = f"\n{nome}: Precisavamos atirar, havia um zumbi lá dentro! \n\
Piloto: Eu vou deixar essa passar, mas nos alerte antes de fazer isso novamente.\n"

if arma1 == 2: #Caso o jogador use a arma para matar o zumbi na casa, este dialogo se inicia
    style(texto[35])
    #Choice7
    while(True): #Inicio do loop Choice7
        try: #Caso o usuario não insira um numero inteiro
            print()
            print(25*"=")
            print("[1] - Mentir")
            print("[2] - Contar a verdade")
            choice7 = int(input("Escolha: ")) #Entrada da Choice7
            print(25*"=")
            if choice7 == 1: #[1] - Mentir
                mentira1 = random.randint(1,5) #Decide se a mentira funciona (20%)
                if mentira1 == 5: #Caso a variavel mentira1 de 5 (20%)
                    style(texto[36])
                    break #Fim do loop Choice7
                elif mentira1 >= 1 and mentira1 <= 4: #Caso a variavel mentira1 de entre 1 e 4 (80%)
                    style(texto[37])
                    break #Fim do loop Choice7
                else:
                    print(f"Erro: valor da variavel 'mentira1' invalido: {mentira1}") #Caso a variavel mentira1 seja diferente do esperado
            if choice7 == 2: #[2] - Contar a verdade
                style(texto[38])
                break #Fim do loop Choice7
            else:
                print(erro) #Retorna ao inicio do loop Choice7
        except ValueError:
            print(25*"=")
            print(erro)

#Narração 8
texto[39] = "\n*Vocês voam até o abrigo para refugiados* \n\
*É um local menor que o quartel, mas não deixa de ser seguro* \n\
*Andando por lá, você percebe que a criança que resgatou esta sozinha em um canto*\n"
style(texto[39])

#Choice8
texto[40] = "\n*Você chama ela e começa a leva-la a um dormitório do abrigo* \n\
*Durante o caminho você tem uma leve conversa com ela* \n\
*Ela conta que na noite anterior o grupo em que ela ficava havia sido atacado por uma horda* \n\
*Você então tenta conforta-la dizendo que agora ela esta mais segura* \n\
\n** A criança se sente mais segura **\n"

texto[41] = "\n*Você chama ela e começa a leva-la a um dos dormitórios do abrigo* \n\
*Você evita conversar com ela durante o caminho* \n\
\n** A criança se sente indifirente com você **\n"

while(True): #Inicio do loop Choice8
    try: #Caso o usuario não insira um numero inteiro
        print()
        print(25*"=")
        print("[1] - Conforta-la")
        print("[2] - Deixar seus superiores falarem com ela")
        choice8 = int(input("Escolha: ")) #Entrada da Choice8
        print(25*"=")
        if choice8 == 1: #[1] - Conforta-la
            style(texto[40])
            rep_crianca = rep_crianca + 1 #Aumenta a reputação com a criança
            break #Fim do loop Choice8
        if choice8 == 2: #[2] - Deixar seus superiores falarem com ela
            style(texto[41])
            rep_crianca = rep_crianca - 1 #Perde reputação com a criança
            break #Fim do loop Choice8
        else:
            print(erro) #Retorna ao inicio do loop Choice8
    except ValueError:
        print(25*"=")
        print(erro)

#Narração 9
texto[42] = f"\n*Quase chegando no abrigo, você nota algo nela* \n\
*Uma ferida em seu tornozelo* \n\
\n{nome}: O que é isso no seu tornozelo? \n\
{crianca}: AH... Nada de mais! \n\
*Ela fala enquanto começa a esconder a ferida* \n\
\n*Ao entrarem no abrigo você nota que o local é mais vazio que o esperado* \n\
*Ao menos é mais seguro por chamar pouca atenção* \n\
\n*Se passa um dia, você, andando pelo abrigo, nota a criança afastada das outras*\n"
style(texto[42])

#Choice9
texto[43] = "\n*Você se aproxima dela, ela esta sentada em um banco, sozinha* \n\
*Você se senta ao lado dela*\n"

texto[44] = "\nVocê oberservando ao longe, percebe que ela tenta ao maximo não falar com os outros, sempre sentada no mesmo banco. \n\
\n** Você escolheu deixar a criança sozinha **\n"

dialogo = 0 #Variavel de dialogo opcional com a criança

while(True): #Inicio do loop Choice9
    try: #Caso o usuario não insira um numero inteiro
        print()
        print(25*"=")
        print("[1] - Conversar com ela")
        print("[2] - Observar")
        choice9 = int(input("Escolha: ")) #Entrada da Choice9
        print(25*"=")
        if choice9 == 1: #[1] - Conversar com ela
            style(texto[43])
            dialogo = 1 #O dialogo opcional sera possivel
            break #Fim do loop choice9
        if choice9 == 2: #[2] - Observar
            style(texto[44])
            rep_crianca = rep_crianca - 5 #Perde reputação com a criança pela perda de dialogo
            break #Fim do loop choice9
        else:
            print(erro) #Retorna ao inicio do loop Choice9
    except ValueError:
        print(25*"=")
        print(erro)

#Choice(10 a 13) e variaveis de verificação de escolhas
choice10 = 0
choice11 = 0
choice12 = 0
choice13 = 0
quest1 = 0
quest2 = 0
quest3 = 0

#O texto[46] foi colocado em cima pois os textos de baixo serão considerados com o nome da criança "Ellie"
texto[46] = f"\n{nome}: Qual seu nome mocinha? \n\
{crianca}: Você nem me disse o seu primeiro \n\
{nome}: Aí! Eu salvei sua vida! \n\
{crianca}: Achei que esse era seu papel mesmo, não algo pra cobrar de alguém depois... \n\
{nome}: ...\n"

if choice9 == 1: #Verifica se o jogador fez a escolha de conversar e troca o nome dela para "Ellie" nos proximos textos
    if crianca != "Ellie":
        crianca = "Ellie"

texto[45] = f"\n{nome}: Acho que agora temos um tempo para nos conhecermos melhor \n\
{nome}: Prazer, eu me chamo {nome}. E você? \n\
{crianca}: Ellie... me chamo Ellie \n\
{nome}: Nome bonito \n\
\n** {crianca} se sente um pouco mais animada **\n"

texto[47] = f"\n{crianca}: Mas se você quer saber, meu nome é Ellie \n\
{nome}: O meu é {nome} \n\
\n** {crianca} esta indiferente **\n"

texto[48] = f"\n{nome}: Por que está afastada das crianças? \n\
{crianca}: Não me dou bem com elas. \n\
{nome}: Por que não? \n\
{crianca}: Porque elas não gostam de mim... \n\
{crianca}: Elas tem medo. \n\
{nome}: Medo do que? \n\
{crianca}: De nada... \n\
\n*Então {crianca} esconde sua perna atras do banco* \n\
\n** {crianca} se sente um pouco melhor **\n"

texto[49] = f"\n{nome}: Como você está? \n\
{crianca}: Estou triste pelo que aconteceu com meus pais...\n"

texto[50] = f"\n{nome}: Sinto muito pelo o que aconteceu \n\
{nome}: Se precisar de alguém para conversar, pode contar comigo. Estamos juntos nessa. \n\
\n** {crianca} se sente mais confortavel **\n"

texto[51] = f"\n{nome}: infelizmente não podemos mudar o que aconteceu. O que nos resta é seguir em frente, eu e você \n\
\n** {crianca} se sente segura **\n"

texto[52] = f"\n{nome}: O que você acha deste lugar? \n\
{crianca}: Bem deprimente, ninguém por aqui parece estar bem de verdade... \n\
{crianca}: E você?\n"

texto[53] = f"\n{nome}: Na atual situação do mundo, não há realmente alguém que esteja bem \n\
\n** Você contou a verdade para {crianca} **\n"

texto[54] = f"\n{nome}: Pelo menos temos um lugar onde ficar, imagina ficar aí fora com estas coisas. \n\
\n** Você confortou {crianca} **\n"

texto[45] = f"\n{nome}: Acho que agora temos um tempo para nos conhecermos melhor \n\
{nome}: Prazer, eu me chamo {nome}. E você? \n\
{crianca}: Ellie... me chamo Ellie \n\
{nome}: Nome bonito \n\
\n** {crianca} se sente um pouco mais animada **\n"

if dialogo == 1: #Dialogo opcional com a criança
    while(True): #Inicio do loop choice10
        try: #Caso o usuario não insira um numero inteiro
            print()
            print(25*"=")
            print("[1] - Se apresentar")
            print("[2] - Perguntar o nome dela")
            choice10 = int(input("Escolha: ")) #Entrada do choice10
            print(25*"=")
            if choice10 == 1: #[1] - Se apresentar
                style(texto[45])
                rep_crianca = rep_crianca + 1 #Aumenta a reputação com a criança
                break #Fim do loop choice10
            if choice10 == 2: #[2] - Perguntar o nome dela
                style(texto[46])
                style(texto[47])
                rep_crianca = rep_crianca - 1 #Perde reputação com a criança
                break #Fim do loop choice10
            else:
                print(erro) #Retorna ao inicio do loop Choice10
        except ValueError:
            print(25*"=")
            print(erro)
    while(True): #Inicio do loop Choice11
        try: #Caso o usuario não insira um numero inteiro
            print()
            print(25*"=")
            if quest1 == 0: #Verifica se o jogador ja escolheu a opção 1 e não mostra a opção
                print("[1] - Sobre estar sozinha...")
            if quest2 == 0: #Verifica se o jogador ja escolheu a opção 2 e não mostra a opção
                print("[2] - Como você esta?")
            if quest3 == 0: #Verifica se o jogador ja escolheu a opção 3 e não mostra a opção
                print("[3] - Sobre o lugar...")
            if quest1 == 1 and quest2 == 1 and quest3 == 1: #Caso o jogador tenha feito todas as opções
                break #Fim do loop Choice11
            choice11 = int(input("Escolha: ")) #Entrada da Choice11
            print(25*"=")
            if choice11 == 1: #[1] - Sobre estar sozinha...
                if quest1 == 0: #O jogador esta indo para esta opção pela primeira vez
                    style(texto[48])
                    rep_crianca = rep_crianca + 1 #Aumenta a reputação com a criança
                    quest1 = 1 #Marca que o jogador ja fez esta opção 1 vez
                elif quest1 == 1: #Caso o jogador tente fazer a mesma opção
                    print(erro) #Retorna ao inicio do loop Choice11
                else:
                    print(f"Erro: Valor da variavel 'quest1' invalido: {quest1}") #Caso a variavel quest1 seja diferente do esperado
            elif choice11 == 2: #[2] - Como você esta?
                if quest2 == 0: #O jogador esta indo para esta opção pela primeira vez
                    style(texto[49])
                    while(True): #Incio do loop choice12
                        try: #Caso o usuario não insira um numero inteiro
                            print()
                            print(25*"=")
                            print("[1] - Consolar")
                            print("[2] - Animar")
                            choice12 = int(input("Escolha: ")) #Entrada da choice12
                            print(25*"=")
                            if choice12 == 1: #[1] - Consolar
                                style(texto[50])
                                rep_crianca = rep_crianca + 2 #Aumenta a reputação com a criança
                                quest2 = 1 #Marca que o jogador ja fez esta opção 1 vez
                                break #Fim do loop Choice12
                            elif choice12 == 2: #[2] - Animar
                                style(texto[51])
                                rep_crianca = rep_crianca + 1 #Aumenta a reputação com a criança
                                quest2 = 1 #Marca que o jogador ja fez esta opção 1 vez
                                break #Fim do loop Choice12
                            else:
                                print(erro) #Retorna ao inicio do loop Choice12
                        except ValueError:
                            print(25*"=")
                            print(erro)
                elif quest2 == 1: #Caso o jogador tente fazer a mesma opção
                    print(erro) #Retorna ao inicio do loop Choice12
                else:
                    print(f"Erro: Valor da variavel 'quest2' invalido: {quest2}") #Caso a variavel quest2 seja diferente do esperado
            elif choice11 == 3: #[3] - Sobre o lugar...
                if quest3 == 0: #O jogador esta indo para esta opção pela primeira vez
                    style(texto[52])
                    while(True): #Inicio do loop choice13
                        try: #Caso o usuario não insira um numero inteiro
                            print()
                            print(25*"=")
                            print("[1] - Realista")
                            print("[2] - Positivo")
                            choice13 = int(input("Escolha: ")) #Entrada da Choice13
                            print(25*"=")

                            if choice13 == 1: #[1] - Realista
                                style(texto[53])
                                rep_crianca = rep_crianca - 1 #Perde reputação com a criança
                                quest3 = 1 #Marca que o jogador ja fez esta opção 1 vez
                                break #Fim do loop Choice13
                            if choice13 == 2: #[2] - Positivo
                                style(texto[54])
                                rep_crianca = rep_crianca + 1 #Aumenta a reputação com a criança
                                quest3 = 1 #Marca que o jogador ja fez esta opção 1 vez
                                break #Fim do loop Choice13
                            else:
                                print(erro) #Retorna ao inicio do loop Choice13
                        except ValueError:
                            print(25*"=")
                            print(erro)
                elif quest3 == 1: #Caso o jogador tente fazer a mesma opção
                    print(erro) #Retorna ao inicio do loop Choice12
                else:
                    print(f"Erro: Valor da variavel 'quest3' invalido: {quest3}") #Caso a variavel quest3 seja diferente do esperado
            else:
                print(erro) #Retorna ao inicio do loop Choice11
        except ValueError:
            print(25*"=")
            print(erro)

#Narração 10
texto[55] = "\n** 1 Mês depois **\n"
style(texto[55])

texto[56] = f"\n*Você e a {crianca} se aproximam com o tempo*"

texto[57] = "\n*Com o passar do tempo, você e a criança acabam se conhecendo um pouco melhor* \n\
*O nome dela é Ellie.* \n\
*Você é a unica pessoa em que ela consegue falar por ali*\n"
if choice9 == 1: #Caso o jogador tenha escolhido conversar com a criança
    style(texto[56])
elif choice9 == 2: #Caso o jogador tenha escolhido apenas observar
    style(texto[57])
    crianca = "Ellie"
else:
    print("Erro: Valor da variavel 'choice' invalido")

#Narração 11
texto[58] = f"\n*Uma chuva forte molha vocês dois* \n\
*Você esta correndo, junto a {crianca}. Foi tudo muito rapido!* \n\
*O abrigo havia sido atacado por uma horda, você a pegou e correu o maximo que pode* \n\
*Vocês correm em direção ao quartel* \n\
\n*Após correrem por um tempo na estrada, vocês param para descansar em um posto abandonado* \n\
*Vocês estão sujos e molhados pela chuva. Alem disso começam a ter fome*\n"
style(texto[58])

#Choice14
texto[59] = "\n*Ao entrar no posto, surge um zumbi que os pega de surpresa!* \n\
*ELE CAI EM CIMA DE VOCÊ!* \n\
*Você derruba sua arma no chão* \n\
\n*Ele esta faminto e tenta te morder e te acertar de todas as formas!* \n\
*Fraco, você começa a seder. Você ve a morte pelos seus olhos.*\n"
quest4 = 0 #Variavel feita para verificar a escolha do jogador

texto[60] = "\n*Sua caçada se mostrou sem sucesso, mas há esperança que no posto tenha algo*\n"
while(True): #Inicio do loop Choice14
    try: #Caso o usuario não insira um numero inteiro
        print()
        print(25*"=")
        print("[1] - Investigar o posto")
        if quest4 == 0: #Verifica se o jogador ja fez esta opção alguma e vez e mostra a ele caso não
            print("[2] - Caçar algum animal")
        choice14 = int(input("Escolha: ")) #Entrada da choice14
        print(25*"=")
        if choice14 == 1: #[1] - Investigar o posto
            style(texto[59])
            break #Fim do loop Choice14
        if choice14 == 2: #[2] - Caçar algum animal
            if quest4 == 0: #Caso o jogador ainda não tenha feito esta opção
                style(texto[60])
                quest4 = 1 #Marca que o jogador fez esta opção 1 vez
            else: #Caso o jogador ja tenha feito esta opção 1 vez
                print(erro) #Retorna ao inicio do loop Choice14
        else:
            print(erro) #Retorna ao inicio do loop Choice11
    except ValueError:
        print(25*"=")
        print(erro)

#Narração 11
texto[61] = f"\n** Ellie ** \n\
\n*Você vê {nome} caido no chão, usando todas as suas forças para segurar o zumbi* \n\
*A arma de {nome} esta em seus pés, você nunca usou uma* \n\
*{nome} depende de você* \n\
*Você não quer ficar sozinha denovo* \n\
\nEllie, o que você faz?\n"
style(texto[61])

#Choice15
texto[62] = "\n*Com todas as suas forças você tenta tirar o zumbi de cima*"

texto[63] = f"\n*Você tenta empurrar o zumbi porém acaba piorando tudo* \n\
{nome} é mordido pelo zumbi!\n"

texto[64] = f"\n*Você empurra o zumbi e consegue tirar ele de cima de {nome}* \n\
*{nome} então puxa a faca e acerta o zumbi*"

texto[65] = "\n*Você pega a arma do chão e atira*"

texto[66] = f"\n*Pelo impacto da arma, a arma recocheteia na sua testa* \n\
*Você precisou de 5 tiros para acerta-lo* \n\
*O zumbi cai morto em cima de {nome}*\n"

texto[67] = f"\n*Você precisou de 5 tiros para acerta-lo* \n\
*O zumbi cai morto em cima de {nome}*\n"

choice15 = 0
tiro1 = 0 #Variavel para o tiro
empurrar1 = 0 #Variavel para o empurrão

while(True): #Inicio do loop Choice15
    try: #Caso o usuario não insira um numero inteiro
        print()
        print(25*"=")
        print("[1] - Empurrar o zumbi")
        print("[2] - Pegar a arma e atirar")
        choice15 = int(input("Escolha: ")) #Entrada da choice15
        print(25*"=")
        if choice15 == 1: #[1] - Empurrar o zumbi
            empurrar1 = random.randint(1,3) #Pega um valor aleatorio para determinar as chances do jogador (33%)
            style(texto[62])
            if empurrar1 == 1 or empurrar1 == 2: #Caso o valor seja 1 ou 2 (66%)
                style(texto[63])
                mortes = mortes + 1 #Aumenta o numero de mortes em 1
                choice15 = 0
                morte()
            elif empurrar1 == 3: #Caso o numero seja 3 (33%)
                style(texto[64])
                break #Fim do loop choice15
            else:
                print(f"Erro: Valor da variavel 'empurrar' invalida: {empurrar1}") #Caso a variavel empurrar1 seja diferente do esperado
        elif choice15 == 2: #[2] - Pegar a arma e atirar
            tiro1 = random.randint(1,3) #Pega um valor aleatorio para determinar as chances do jogador (33%)
            style(texto[65])
            if tiro1 == 1 or tiro1 == 2: #Caso o valor seja 1 ou 2 (66%)
                style(texto[66])
                break #Fim do loop choice15
            elif tiro1 == 3: #Caso o valor seja 3 (33%)
                style(texto[67])
                break #Fim do loop choice15
            else:
                print(f"Erro: Valor da variavel 'tiro1' invalida: {tiro1}") #Caso a variavel tiro1 seja diferente do esperado
        else:
            print(erro) #Retorna ao inicio do loop Choice15
    except  ValueError:
        print(erro)

#Narração 12
texto[68] = f"\n\n** {nome} **"
style(texto[68])

#Choice16
texto[69] = "\n*Você empurra o corpo do zumbi para o lado, deixando o mesmo caido ali no chão*"
dialogo_arma = 0 #Variavel do dialogo da escolha da arma

texto[70] = f"\n*Você olha para {crianca}. Ela ainda esta apontando a arma com a testa sangrando levemente* \n\
*Os dois estão ofegantes e assustados, você então se levanta*\n"

texto[71] = f"\n*Você olha para {crianca}. Ela ainda esta apontando a arma* \n\
*Os dois estão ofegantes e assustados, você então se levanta*\n"

texto[72] = f"\n{nome}: Calma... Ja passou... Esta tudo bem \n\
*{crianca} abaixa a arma e respira mais fundo*\n"

texto[73] = "\n*Você limpa a testa dela e coloca um curativo*\n"

texto[74] = f"\n** {crianca} esta calma e te entregou a arma **\n"

texto[75] = f"\n*Você chega até {crianca} e tenta pegar a arma das mãos dela* \n\
*Ela ainda em choque acaba, sem querer, pressionando o gatilho e te acertando*\n"

texto[76] = f"\n*Você chega até {crianca} e pega a arma de suas mãos* \n\
*Ela coloca a mão na testa e vê o sangue*\n"

texto[77] = f"\n*Você limpa a testa dela e coloca um curativo* \n\
\n** {crianca} se sente mais calma **\n"

texto[78] = f"\n{nome}: Não foi nada, isso vai passar \n\
{crianca}: Se você diz... \n\
{nome}:... \n\
\n** {crianca} continua preocupada **\n"

texto[79] = f"\n*Você chega até {crianca} e pega a arma de suas mãos* \n\
*{crianca} esta assustada*\n"

texto[80] = f"\n{nome}: Obrigado... Por me salvar \n\
{crianca}: ... \n\
{nome}:... \n\
\n** {crianca} se sente melhor **\n"

texto[81] = f"{crianca}: ... \n\
{nome}:... \n\
\n** {crianca} se sente desconfortavel **\n"

texto[82] = f"\n*Após mata-lo, você limpa a sua faca* \n\
*Ao olhar para trás, você nota {crianca} cansada*\n"

texto[83] = f"\n*Você vasculha o corpo e não encontra nada* \n\
\n** Você ignorou {crianca} **\n"

texto[84] = f"{nome}: Ei, valeu pela ajuda... sério. \n\
{crianca}: De boa... \n\
\n ** {crianca} se sente melhor **\n"

if tiro1 >= 1 and tiro1 <= 3: #Caso o jogador tenha escolhido atirar
    style(texto[69])
    if tiro1 == 1 or tiro1 == 2: #Caso o jogador tenha se ferido (66%)
        style(texto[70])
    if tiro1 == 3: #Caso o jogador não tenha se machucado (33%)
        style(texto[71])
    while dialogo_arma == 0: #Inicio do loop Choice16
        try: #Caso o usuario não insira um numero inteiro
            print()
            print(25*"=")
            print("[1] - Acalma-la")
            print("[2] - Pegar a arma")
            choice16 = int(input("Escolha: ")) #Entrada da choice16
            print(25*"=")
            if choice16 == 1: #[1] - Acalma-la
                style(texto[72])
                if tiro1 == 1 or tiro1 == 2: #Caso o jogador tenha ferido a testa (66%)
                    style(texto[73])
                style(texto[74])
                rep_crianca = rep_crianca + 1 #Aumenta a reputação da criança
                break #Fim do loop Choice16
            if choice16 == 2: #[2] - Pegar a arma
                tiro2 = random.randint(1,3) #Pega um valor entre 1 e 3 (33%)
                if tiro2 == 1: #Caso seja 1 (33%) a criança mata o jogador
                    style(texto[75])
                    mortes = mortes + 1 #Aumenta o numero de mortes
                    morte()
                elif tiro2 == 2 or tiro2 == 3: #Caso seja 2 ou 3 (66%) a criança não mata o jogador
                    if tiro1 == 1 or tiro1 == 2: #Caso o jogador tenha se ferido (66%)
                        style(texto[76])
                        while(True): #Inicio do loop choice17
                            try: #Caso o usuario não insira um numero inteiro
                                print()
                                print(25*"=")
                                print(f"[1] - Limpar a testa de {crianca}")
                                print('[2] - "Não foi nada..."')
                                choice17 = int(input("Escolha: ")) #Entrada da Choice17
                                print(25*"=")
                                if choice17 == 1: #[1] - Limpar a testa de {crianca}
                                    style(texto[77])
                                    rep_crianca = rep_crianca + 1 #Aumenta a reputação com a criança
                                    dialogo_arma = 1 #Quebra o loop Choice16
                                    break #Fim do loop choice17
                                if choice17 == 2: #[2] - "Não foi nada...
                                    style(texto[78])
                                    rep_crianca = rep_crianca - 1 #Aumenta a reputação com a criança
                                    dialogo_arma = 1 #Quebra o loop Choice16
                                    break #Fim do loop choice17
                                else:
                                    print(erro) #Retorna ao inicio do loop Choice17
                            except ValueError:
                                print(25*"=")
                                print(erro)
                    elif tiro1 == 3: #Caso o jogador não tenha se ferido (33%)
                        style(texto[79])
                        while(True): #Inicio do loop Choice18
                            try: #Caso o usuario não insira um numero inteiro
                                print()
                                print(25*"=")
                                print("[1] - Agradeçer")
                                print("[2] - Ficar quieto")
                                choice18 = int(input("Escolha: ")) #Entrada da Choice18
                                print(25*"=")
                                if choice18 == 1: #[1] - Agradeçer
                                    style(texto[80])
                                    rep_crianca = rep_crianca + 1 #Aumenta a reputação com a criança
                                    dialogo_arma = 1 #Quebra o loop Choice16
                                    break #Fim do loop choice18
                                if choice18 == 2: #[2] - Ficar quieto
                                    style(texto[81])
                                    rep_crianca = rep_crianca - 1 #Perde reputação com a criança
                                    dialogo_arma = 1 #Quebra o loop Choice16
                                    break #Fim do loop choice18
                                else:
                                    print(erro) #Retorna ao inicio do loop Choice18
                            except ValueError:
                                print(25*"=")
                                print(erro)
                    else:
                        print(f"Erro: Valor da variavel 'tiro1' invalida: {tiro1}") #Caso a variavel tiro1 seja diferente do esperado 
                else:
                    print(f"Erro: Valor da variavel 'tiro2' invalida: {tiro2}") #Caso a variavel tiro2 seja diferente do esperado
            else:
                print(erro) #Retor ao inicio do loop Choice16
        except ValueError:
            print(25*"=")
            print(erro)
if empurrar1 == 3: #Caso o jogador tenha escolhido empurrar
    style(texto[82])
    while(True): #Inicio do loop Choice19
        try: #Caso o usuario não insira um numero inteiro
            print()
            print(25*"=")
            print("[1] - Vasculhar o corpo...")
            print("[2] - Agradeçer")
            choice19 = int(input("Escolha: ")) #Entrada da Choice19
            print(25*"=")
            if choice19 == 1: #[1] - Acalma-la
                style(texto[83])
                rep_crianca = rep_crianca - 1 #Aumenta a reputação com a criança
                break #Fim do loop choice19
            if choice19 == 2: #[2] - Agradeçe-la
                style(texto[84])
                rep_crianca = rep_crianca + 1 #Aumenta a reputação com a criança
                break #Fim do loop choice19
            else:
                print(erro) #Retorna ao inicio do loop choice19
        except ValueError:
            print(25*"=")
            print(erro)

#Narração 13
texto[85] = f"\n*Entrando no posto, vocês encontram algumas garrafas de água e pacotes de salgadinhos* \n\
*Esta anoitecendo* \n\
*{crianca} parece estar cansada* \n\
*Você também esta exausto, com isso, resolvem passar a noite ali*\n"
style(texto[85])

#Choice20
texto[86] = "\n*Você resolve descansar também.*\n"

texto[87] = f"\n{crianca}: Foi minha primeira vez usando uma arma \n\
{nome}: Até que você foi bem pela primeira vez \n\
{crianca}: Serio?? \n\
{nome}: Eu não levei nenhum tiro, então sim... \n\
{crianca}:... \n\
\n** {crianca} se sente segura ** \n\
\n*Vocês descansam*\n"

texto[88] = f"{crianca}: Nunca usei uma arma... Por isso não usei \n\
{nome}: O que importa é que sobrevivemos, você foi forte \n\
{crianca}:... \n\
\n** {crianca} se sente forte ** \n\
*Vocês descansam*"

texto[89] = f"*Mesmo exausto, você resolve ficar de vigia* \n\
*{crianca} cai no sono* \n\
*Você acaba não durando muito e também cai no sono*\n"

while(True): #Inicio do loop Choice20
    try: #Caso o usuario não insira um numero inteiro
        print()
        print(25*"=")
        print("[1] - Descansar também")
        print("[2] - Ficar de Vigia")
        choice20 = int(input("Escolha: ")) #Entrada da Choice20
        print(25*"=")
        if choice20 == 1: #[1] - Descansar junto com a criança
            style(texto[86])
            if tiro1 >= 1 and tiro1 <= 3: #Caso o jogador tenha escolhido atirar
                style(texto[87])
                rep_crianca = rep_crianca + 1 #Aumenta a reputação com a criança
                break #Fim do loop Choice20
            if empurrar1 == 3: #Caso o jogador tenha escolhido empurrar
                style(texto[88])
                rep_crianca = rep_crianca + 1 #Aumenta a reputação com a criança
                break #Fim do loop Choice20
        if choice20 == 2: #] - Ficar de Vigia
            style(texto[89])
            break #Fim do loop Choice20
        else:
            print(erro) #Retorna ao inicio do loop Choice20
    except ValueError:
        print(25*"=")
        print(erro)

#Narração 14
texto[90] = "\n*Após acordarem, vocês continuam seguindo a estrada, rumo ao quartel* \n\
*Após 3 horas andando em uma chuva fina, vocês encontram uma pequena cidade* \n\
*Esta tudo destruido e abandonado* \n\
*Vocês então se deparam com um bando de zumbis perambulando pela rua*\n"
style(texto[90])

#Choice21
texto[91] = "\n*Vocês se esgueiram e tentam passar pelos zumbis* \n\
*No meio do caminho, vocês quase são percebidos* \n\
\n*Quando estão quase chegando*\n"
car = 0 #Variavel para contar a escolha

texto[92] = f"\n*Você acaba derrubando uma lata, {crianca} olha assustada para você! \n\
*Você olha para ela, e quando decide olhar para trás...* \n\
*Você é pego por um zumbi!*\n"

texto[93] = f"\n*{crianca} acaba derrubando algumas latas sem querer!* \n\
*Quando você olha para ela...* \n\
*Ela é pega por um zumbi!*\n"

texto[94] = "\n*Olhando em volta, vocês encontram um carro em uma garagem proxima* \n\
*Parece estar novo...*\n"

texto[95] = "\n*Vocês então resolvem ir até a garagem...*"

while(True):
    try: #Caso o usuario não insira um numero inteiro
        print()
        print(25*"=")
        print("[1] - Passar silenciosamente")
        if car == 0:
            print("[2] - Procurar outra maneira de passar")
        elif car == 1:
            print("[3] - Ir para a garagem")
        choice21 = int(input("Escolha: ")) #Entrada da Choice21
        print(25*"=")
        if choice21 == 1: #[1] - Passar silenciosamente
            who = random.randint(1,2) #Escolhe um numero entre 1 e 2 para decidir quem irá estragar o stealth
            style(texto[91])
            if who == 1:
                style(texto[92])
                mortes = mortes + 1  # Adiciona +1 ao numero de mortes
                morte()
            if who == 2:
                style(texto[93])
                mortes = mortes + 1  # Adiciona +1 ao numero de mortes
                morte()
        elif choice21 == 2: #[2] - Procurar outra maneira de passar
            if car == 0:
                style(texto[94])
                car = 1 #Marca que o jogador ja fez esta escolha uma vez
            else:
                print(erro)
        elif choice21 == 3: #[3] - Ir para a garagem
            if car == 0: #Caso o jogador ainda não tenha desbloqueado esta opção
                print(erro)
            if car == 1: #Permite o jogador desbloquear a opção
                style(texto[95])
                break #Fim do loop Choice21
        else:
            print(erro) #Retorna ao inicio do loop Choice21
    except ValueError:
        print(25*"=")
        print(erro)

#Narração 15
texto[96] = "\n*Ao chegarem lá, parece tudo bem bagunçado e empoeirado* \n\
*Checando o carro, vocês notam que ele esta trancado* \n\
\n*UM ZUMBI SURPREENDE VOCÊS* \n\
\n*Ele te pressiona contra uma bancada!* \n\
** Você sabe que não ira aguentar segura-lo por muito tempo! **\n"
style(texto[96])

#Choice22
texto[97] = "\n*Você perde suas forças e o zumbi acaba te matando!*\n"

texto[98] = "\n*Você pega a sua faca, porém, no desespero você acaba a derrubando*\n"

texto[99] = f"\n*Você chama {crianca}* \n\
*Ela sem armas, aponta para a bancada ao seu lado...*\n"

texto[100] = "\n*Você nota ao seu lado uma chave-de-fenda e uma garrafa de vidro*\n"

texto[101] = "\n*Você pega a chave-de-fenda e acerta o zumbi em cheio, ficando livre finalmente*\n"

texto[102] = "\n*Você acerta o zumbi com a garrafa, ela se quebra nele mas continua vivo!*\n"

texto[103] = "\n*Você acerta o zumbi com a garrafa, ele cai no chão* \n\
*Você aproveita para pegar sua faca e o elimina ali*\n"

texto[104] = "\n** O zumbi te pressiona, você esta perdendo suas forças **\n"

tentativas = 0
observar = 0
faca = 0
chamar = 0
garrafa = 0

while(True):
    try: #Caso o usuario não insira um numero inteiro
        if tentativas == 3: #Caso o jogador tenha feito 4 tentativas
            print(25 * "=")
            style(texto[97])
            tentativas = 0
            observar = 0
            faca = 0
            chamar = 0
            garrafa = 0
            mortes = mortes + 1  # Adiciona +1 ao numero de mortes
            morte() #Chama a função morte
        print()
        print(25*"=")
        if faca == 0:
            print("[1] - Puxar a faca")
        if chamar == 0:
            print(f"[2] - Chamar {crianca}...")
        if observar == 0:
            print("[3] - Olhar em volta...")
        if observar == 1:
            print("[4] - Pegar chave-de-fenda")
            if garrafa == 0:
                print("[5] - Pegar garrafa")
        choice22 = int(input("Escolha: ")) #Entrada da Choice22
        if choice22 == 1: #[1] - Puxar a faca
            print(25 * "=")
            style(texto[98])
            tentativas = tentativas + 1
            faca = 1 #Marca que o jogador ja escolheu essa opção
        elif choice22 == 2: #[2] - Chamar {crianca}...
            print(25 * "=")
            style(texto[99])
            tentativas = tentativas + 1
            chamar = 1 #Marca que o jogador ja escolheu essa opção
        elif choice22 == 3: #[3] - Olhar em volta...
            print(25 * "=")
            style(texto[100])
            tentativas = tentativas + 1
            observar = 1 #Marca que o jogador olhou para a bancada
        elif choice22 == 4: #[4] - Pegar chave-de-fenda
            if observar == 1:
                print(25 * "=")
                style(texto[101])
                tentativas = tentativas + 1
                break #Fim do loop choice22
            else:
                print(erro)
        elif choice22 == 5:  # [5] - Pegar garrafa
            if observar == 1:  # Verifica se o jogador observou a mesa
                if garrafa == 0:  # Verifica se o jogador ja pegou a garrafa
                    garrafa = random.randint(1, 2)  # Pega um valor aleatorio (50%)
                    if garrafa == 1:  # Caso o valor seja 1, a garrafa não funciona (50%)
                        tentativas = tentativas + 1
                        print(25*"=")
                        style(texto[102])
                    if garrafa == 2:  # Caso o valor seja 2, a garrafa funciona (50%)
                        style(texto[103])
                        break  # Fim do loop choice22
                else:  # Caso o jogador ja tenha pego a garrafa
                    print(25 * "=")
                    print(erro)
            else:
                print(25 * "=")
                print(erro)
        else:
            print(25 * "=")
            print(erro) #Retorna ao inicio do loop caso o numero seja invalido
    except ValueError:
        print(25*"=")
        print(erro)

#Narração 16
texto[105] = f"\n*Por muita sorte os zumbis do lado de fora não os viram* \n\
\n{nome}: Vamos ver como esse carro esta...\n"
style(texto[105])

#Choice23
texto[106] = "\n*Voce vai ate o carro...*\n"

texto[107] = "Encher o tanque?\n"

texto[108] = f"\n** Você encheu o tanque do carro ** \n\
\n{crianca}: Então é pra isso? \n\
{nome}: Sim! \n\
{crianca}: Que merda... \n\
{nome}: EI!"

texto[109] = f"\n** Você decide não encher o tanque ainda ** \n\
\n{crianca}: O que aconteceu? \n\
{nome}: É um recurso importante, temos que saber o que estamos fazendo... \n\
{crianca}: ...\n"

texto[110] = "Usar o estepe?\n"

texto[111] = f"\n{crianca}: O que você esta fazendo? \n\
{nome}: Trocando o pneu ué \n\
{crianca}: Não sabia que dava pra fazer isso... \n\
\n** Você troca o pneu **\n"

texto[112] = f"\nVocê decide não usar o estepe \n\
\n{crianca}: O que você esta fazendo? \n\
{nome}: Pensando...\n"

texto[113] = f"\n*Você entra no carro e torce para ele funcionar...* \n\
\n{crianca}: FUNCIONOU!! \n\
{nome}: Fala baixo! \n\
{crianca}: Desculpa me empolguei... AH MERDA! \n\
{nome}: OLHA O PALAVRÃO! \n\
\n*Os zumbis começam a ir em sua direção* \n\
*Você não perde tempo e acelera, desviando e atropelando alguns* \n\
*Vocês seguem a estrada, agora com um carro*\n"

texto[114] = f"\n{nome}: Ainda faltam mais alguns ajustes...\n"

texto[115] = f"\n*Ao procurar pela garagem, você encontra um estepe* \n\
\n{crianca}: Ei! O que é isso aqui? \n\
*Você vê {crianca} apontando para um galão de gasolina* \n\
{nome}: Isso pode ser util \n\
{crianca}: Mas o que é? \n\
{nome}: Você vai ver... \n\
\n*Você encontrou um estepe e um galão vazio*\n"

texto[116] = f"\n{nome}: Não há mais nada por aqui...\n"

texto[117] = "\n*Você decide vasculhar o corpo* \n\
*Você nota que a uma bala em sua cabeça, talvez ele tenha tentado...* \n\
\n** Você encontra a chave do carro **\n"

texto[118] = "\n*Voce nota em um carro quebrado do lado de fora... talvez ele tenha algo que sirva*\n"
texto[119] = "\n** Você ja esta usando um item **\n"

texto[120] = "\n** Você pega o estepe! **\n"

texto[121] = "\n** Você pega o galão vazio **\n"
texto[122] = "\n*Você vai ate o carro de fora* \n\
*Ele está bem quebrado*\n"

texto[123] = "\nEncher o galão com a gasolina?\n"

texto[124] = f"\n** Voce decide não encher o galão ** \n\
\n{crianca}: Eai? \n\
{nome}: Calma.\n"
texto[125] = "\n*Mas parece ter gasolina dentro*\n"

texto[126] = "\nAgora é apenas um carro quebrado\n"

texto[127] = f"\n{nome}: Aquele carro...\n"

texto[128] = f"\n*Usando uma mangueira, você puxa a gasolina do carro quebrado e coloca no galão* \n\
{crianca}: Eca! Por que você fez isso? \n\
{nome}: É necessário.\n"

galao_vazio = 0
galao_cheio = 0
estepe = 0
chave = 0
vasculhar1 = 0
vasculhar2 = 0
car_estepe = 0
car_galao = 0
puzzle = 0

while puzzle == 0: #Inicio do loop Puzzle
    try: #Caso o usuario não insira um numero inteiro
        print()
        print(25*"=")
        print("[1] - Checar o carro...")
        print("[2] - Vasculhar a garagem...")
        print("[3] - Vasculhar o corpo...")
        print("[4] - Observar ao redor...")
        if vasculhar1 == 1: #Verifica se o jogador desbloqueou a opção
            if estepe == 0 and car_estepe == 0: #Verifica se o jogador não tem os itens ou ja usou
                print("[5] - Pegar o estepe")
            if galao_vazio == 0 and galao_cheio == 0 and car_galao == 0: #Verifica se o jogador não tem os itens ou ja usou
                print("[6] - Pegar o Galão de gasolina")
        if vasculhar2 == 1: #Verifica se o jogador desbloqueou a opção
            print("[7] - Ir até o carro quebrado...")
        choice23 = int(input("Escolha: ")) #Entrada da Choice23
        print(25*"=")
        if choice23 == 1: #[1] - Checar o carro
            style(texto[106])
            if galao_cheio == 1: #Verifica se o jogador possui o galao cheio
                while(True): #Inicio do loop choice25
                    try: #Caso o usuario não insira um numero inteiro
                        print()
                        print(25*"=")
                        style(texto[107])
                        print("[1] - Sim")
                        print("[2] - Não")
                        choice25 = int(input("Escolha: ")) #Entrada da Choice25
                        print(25*"=")
                        if choice25 == 1: #[1] - Sim
                            galao_cheio = 0 #Retira o galao cheio
                            car_galao = 1 #Mostra que o jogador abasteceu o carro
                            style(texto[108])
                            break #Quebra o loop Choice25
                        elif choice25 == 2: #[2] - Não
                            style(texto[109])
                            break #Quebra o loop Choice25
                        else:
                            print(erro)
                    except ValueError:
                        print(25*"=")
                        print(erro)
            if estepe == 1: #Verifica se o jogador possui o estepe
                while(True): #Inicio do loop Choice26
                    try: #Caso o usuario não insira um numero inteiro
                        print()
                        print(25*"=")
                        style(texto[110])
                        print("[1] - Sim")
                        print("[2] - Não")
                        choice26 = int(input("Escolha: ")) #Entrada da Choice26
                        print(25*"=")
                        if choice26 == 1: #[1] - Sim
                            estepe = 0 #Retira o estepe do jogador
                            car_estepe = 1 #Coloca o estepe no carro
                            style(texto[111])
                            break #Quebra o loop Choice26
                        elif choice26 == 2: #[2] - Não
                            style(texto[112])
                            break #Quebra o loop Choice26
                        else:
                            print(erro)
                    except ValueError:
                        print(25*"=")
                        print(erro)
            if car_galao == 1 and car_estepe == 1 and chave == 1: #Verifica se o jogador possui todos os itens necessarios
                style(texto[113])
                puzzle = 1 #Quebra o loop Puzzle
            else: #Caso o jogador nao esteja pronto para ir
                style(texto[114])
        elif choice23 == 2: #[2] - Vasculhar a garagem
            if vasculhar1 == 0: #Caso o jogador esteja verificando pela primeira vez
                style(texto[115])
                vasculhar1 = 1 #Mostra que o jogador verificou uma vez
            else: #Caso o jogador ja tenha verificado
                style(texto[116])
        elif choice23 == 3: #[3] - Vasculhar o corpo
            if chave == 0: #Caso o jogador nao tenha pego a chave
                style(texto[117])
                chave = 1 #Adiciona a chave no inventario
            else: #Caso o jogador ja tenha a chave
                style(texto[116])
        elif choice23 == 4: #[4] - Observar ao redor
            if vasculhar2 == 0: #Caso o jogador não tenha vasculhado ainda
                style(texto[118])
                vasculhar2 = 1 #Mostra que o jogador verificou uma vez
            elif vasculhar2 == 1 and galao_cheio == 0 and car_galao == 0: #Caso o jogador ja tenha vasculhado mas não tenha feito o objetivo ainda
                style(texto[118])
            elif vasculhar2 == 1 and galao_cheio == 1 or car_galao == 1: #Caso ja tenha feito tudo no carro
                print(texto[126])
        elif choice23 == 5: #[5] - Pegar o estepe
            if vasculhar1 == 1 and car_estepe == 0: #Caso o jogador tenha a opção desbloqueada e não tenha feito o objetivo
                if galao_vazio == 1 or galao_cheio == 1: #Caso o o jogador possua o galao independete
                    style(texto[119])
                elif estepe == 0: #Verifica se o jogador ja tem o estepe
                    style(texto[120])
                    estepe = 1
                else: #Caso o jogador tente pegar novamente
                    print(erro)
            else: #Caso o jogador ja tenha feito o objetivo
                print(erro)
        elif choice23 == 6: #[6] - Pegar o Galão de gasolina
            if vasculhar1 == 1 and car_galao == 0: #Caso o jogador tenha desbloqueado e nao tenha o galao
                if estepe == 1: #Caso o jogador tenha o estepe
                    style(texto[119])
                elif galao_vazio == 0 and galao_cheio == 0: #Verifica se o jogador ja tem o galao
                    style(texto[121])
                    galao_vazio = 1 #Adiciona o galao no inventario
                else: #Caso o jogador tente pegar o item novamente
                    print(erro)
            else: #Caso o jogador tente pegar o item ja tendo completado o objetivo
                print(erro)
        elif choice23 == 7: #[7] - Ir até o carro quebrado...
            if vasculhar2 == 1 and galao_cheio == 0 and car_galao == 0: #Caso o jogador tenha a opção desbloqueada e nao tenha o galao
                style(texto[122])
                if galao_vazio == 1: #Caso o galao esteja vazio
                    while(True): #Inicio do loop Choice24
                        try: #Caso o usuario não insira um numero inteiro
                            print()
                            print(25*"=")
                            style(texto[123])
                            print("[1] - Sim")
                            print("[2] - Não")
                            choice24 = int(input("Escolha: ")) #Entrada da Choice24
                            print(25*"=")
                            if choice24 == 1: #[1] - Sim
                                style(texto[128])
                                galao_vazio = 0 #Tira o galao vazio
                                galao_cheio = 1 #Deixa o galao cheio
                                break #Quebra o loop Choice24
                            elif choice24 == 2: #[2] - Não
                                style(texto[124])
                                break #Quebra o loop Choice24
                            else: #Caso o jogador insira um numero invalido
                                print(erro)
                        except ValueError:
                            print(25*"=")
                            print(erro)
                else: #Caso o jogador tenha 
                    style(texto[125])
            elif vasculhar2 == 1 and galao_cheio == 1 or car_galao == 1: #Caso o jogador tente encher o galao novamente
                style(texto[126])
            else: #Caso o jogador tente entrar bloqueado
                print(erro)
        else: #Caso o jogador nao insira um numero valido
            print(erro)
    except ValueError:
        print(25*"=")
        print(erro)

#Narração 17
texto[128] = f"\n** Seguindo a estrada ** \n\
*Você dirige descansado enquanto a criança olha pela janela no banco de tras* \n\
\n{nome}: Sabe... Por que você sempre esconde essa ferida no tornozelo? \n\
{crianca}: Como assim? \n\
{nome}: No quartel, eu notei que você escondeu de mim \n\
{crianca}: Você viu... \n\
{nome}: ... \n\
{crianca}: Naquela casa... meu pai havia se transformado \n\
{crianca}: Eu não acreditava que aquilo tinha acontecido... \n\
{crianca}: Quando ele tentou me pegar eu corri para o quarto \n\
{crianca}: Eu acabei tropeçando e ele... me mordeu \n\
{crianca}: Por sorte, eu consegui escapar e me tranquei naquele quarto \n\
{nome}: Mas você não... Desde aquele dia?! \n\
{crianca}: ... \n\
{nome}: ...Ao menos você esta viva. \n\
{crianca}: Eu tenho medo que alguem descubra algum dia \n\
{crianca}: E se eles tentarem fazer algo... comigo? \n\
{nome}: Isso não vai acontecer \n\
{crianca}: Você... promete que não vai contar pra ninguem...? \n\
{nome}: ...Sim"
style(texto[128])

texto[129] = f'\n** Vocês chegam no quartel em meio a uma leve chuva ** \n\
*\nAo chegar, você desce rapidamente do carro* \n\
*Você deixa {crianca}, que esta dormindo no carro, com os guardas* \n\
*Ao entrar no quartel, você encontra o general Souza*\n \n\
\nGeneral Souza: Achei que você estava morto! \n\
{nome}: Tenho uma notícia, general \n\
General Souza: Além de estar vivo? \n\
{nome}: A garota que eu resgatei. Ela havia sido mordida, mas não se transformou! \n\
\n*O General então ergue seu braço e dá um tapa na sua cara* \n\
General Souza: COMO VOCÊ TEM TANTA CERTEZA?! \n\
General Souza: SE ELA SE TRANSFORMA AQUI, ESTAMOS CONDENADOS! \n\
General Souza: ... \n\
General Souza: Nós iremos leva-la. Vá ao seu dormitório, sua missão esta completa \n\
\n*O General então chama alguns medicos e vai até {crianca}* \n\
*"{crianca}: Você promete que não vai contar a ninguem?"* \n\
*As palavras dela passam pela sua cabeça* \n\
\n** Você traiu {crianca} ** \n\
\n** Após algum tempo, o general te chama a uma reunião ** \n\
\n{nome}: Onde ela esta!? \n\
General Souza: Eu apenas vim te avisar, que tudo a um preço... \n\
{nome}: O que aconteceu \n\
General Souza: Descobrimos como produzir a cura... mas para isso ela ira morrer no processo \n\
{nome}: Você está maluco!? Ela é apenas uma criança! \n\
General Souza: Precisamos de uma parte do cérebro dela para produzir a vacina \n\
General Souza: Desculpa, mas é necessario \n\
*O general então se vira e sai do dormitório* \n\
\n** Você esta em choque ** \n\
*Você irá perde-la e nem podera ao menos se despedir* \n\
\n** {nome}, O que você faz? **\n'
style(texto[129])

#Choice25
texto[130] = f"[1] - Sacrificar {crianca}"
texto[131] = "\n[2] - Salvar Ellie"

final = 0 #Variavel para definir o loop Fianl
while final == 0: #Inicio do loop Final
    try: #Caso o usuario não insira um numero inteiro
        print()
        print(25*"=")
        style(texto[130])
        if rep_crianca >= 5: #Caso a reputação com a criança esteja positivo
            style(texto[131])
        choice25 = int(input("\nEscolha: ")) #Entrada da Choice25
        print(25*"=")
        if choice25 == 1 or choice25 == 2: #Caso a escolha seja dentro das opções
            if choice25 == 2 and rep_crianca < 5:
                print(erro)
            else:
                while(True): #Inicio do loop Choice26
                    try: #Caso o usuario não insira um numero inteiro
                        print()
                        print("Você tem certeza?")
                        print("[1] - Sim")
                        print("[2] - Não")
                        choice26 = int(input("Escolha: ")) #Entrada da Choice26
                        print(25*"=")
                        if choice26 == 1: #[1] - Sim
                            if choice25 == 1: #[1] - Sacrificar {crianca}
                                final = 1 #Manda o jogador para o final 1 e quebra o loop final
                                break #Quebra o loop Choice26
                            elif choice25 == 2: #[2] - Salvar Ellie [Desbloqueado]
                                if rep_crianca >= 5:
                                    final = 2 #Manda o jogador para o final 2 e quebra o loop final
                                    break #Quebra o loop Choice26
                                else:
                                    print(erro)
                        if choice26 == 2: #[2] - Não
                            break #Quebra o loop Choice26
                        else: #Caso o jogador insira um numero invalido
                            print(erro)
                    except ValueError:
                        print(25*"=")
                        print(erro)
        else: #Caso o jogador insira um numero invalido
            print(erro)
    except ValueError:
        print(25*"=")
        print(erro)

#Final 1 (Sacrificar a Criança)
texto[132] = "\n** Você decidiu sacrificar a criança ** \n\
\n*Você decide que a melhor escolha é sacrifica-la pelo bem de todos* \n\
*Mesmo não podendo se despedir* \n\
\n** Após algum tempo, o primeiro protótipo de vacina é criado ** \n\
** ... ** \n\
\n** ...Porém... os primeiros testes acabam dando errado ** \n\
** O virus acabou ficando mais forte do que antes ** \n\
** O quartel então é atacado ** \n\
** Não existem mais esperanças ** \n\
\n=============== BAD ENDING ==============="

#Final 2 (Salvar a Criança)
texto[133] = "\n*Você então pega as suas coisas e sai escondido do dormitório em busca da criança* \n\
*Se eles vão remover um pedaço dela, ela provavelmente esta na sala de operações* \n\
\n*Você entra na parte interna do quartel e pega o elevador* \n\
*No que a porta do elevador se abre... a um guarda*\n"

texto[134] = "\n*Você tenta se disfarçar* \n\
*O guarda aponta a arma para você* \n\
Guarda: VOCÊ NÃO DEVERIA ESTAR AQUI SOLDADO! \n\
\n*Você então tenta desarma-lo*"

texto[135] = "\n*Ele dispara contra você!*\n"

texto[136] = "\n*Você o desarma e logo em seguida o acerta com sua faca*"

texto[137] = "\n*Você rapidamente o nocauteia no elevador*\n"

texto[138] = f"\n*Ao chegar na sala de operações você vê 3 medicos* \n\
*Junto a eles, {crianca} em uma maca, provalvemente anestesiada para fazer a cirurgia* \n\
\n*Você rende a todos com sua arma* \n\
*Você então retira {crianca} da maca e a pega no colo* \n\
\nMedico: Por que esta fazendo isso?? \n\
{nome}: Eu fiz uma promessa \n\
\n*Você pega o elevador novamente* \n\
*Sabendo que os veiculos sempre estão com as chaves para casos de emergencia, você decide ir a garagem* \n\
*Saindo do elevador, você escuta o alarme sendo acionado* \n\
*Você tem pouco tempo* \n\
*Você coloca {crianca} no carro mais proximo* \n\
\n*Quando você esta prestes a entrar no carro... o General puxa seu braço!!* \n\
\n*Você cai no chão!* \n\
\n*O Genera então começa a te estrangular* \n\
\nGeneral Souza: Eu tentei te alertar... \n\
General Souza: PENSE QUANTAS VIDAS PODEM SER SALVAS! \n\
General Souza: PENSE QUANTOS SERÃO MORTOS PELA SUA IGNORANCIA! \n\
\n*Ele fala enquanto te estrangula, seu ar esta acabando* \n\
*Sua visão começa a embaçar, sua audição começa a falhar* \n\
\n*A unica coisa que consegue ver é o que deveria ser o general tentando dizer algo para você* \n\
*...* \n\
\n*Derrepente o general para... e cai para o lado* \n\
*Ao cair, você ve... {crianca} esta com uma faca ensanguentada na mão* \n\
\n{crianca}: O QUE ESTA ACONTECENDO?? \n\
{nome}: Achei que tinha te perdido! \n\
{nome}: {crianca}... Eu te conto depois... precisamos sair \n\
\n** Vocês pegam o carro e saem quebrando o portão ** \n\
\n** Ao longe é possivel apenas escutar o alarme ** \n\
\n** Após um tempo **"

#Caso o jogador tenha um nome normal
texto[139] = f"\n{crianca}: E então? \n\
{nome}: E então o que? \n\
{crianca}: O que foi aquilo? Por que estavam nos atacando? \n\
{nome}: {crianca}... eu quebrei nossa promessa \n\
{crianca}: Como assim!? \n\
{nome}: Eu contei a eles sobre você... \n\
{nome}: Eles iriam tentar produzir uma cura \n\
{nome}: Mas para isso eles iriam te matar... \n\
{crianca}: Mas... era a cura! \n\
{nome}: Eu fiz uma promessa a você \n\
{nome}: Disse que iria te proteger... e eu fiz \n\
{crianca}: ...Obrigada... {nome} \n\
\n** {nome} e {crianca} passam suas vidas juntos, sobrevivendo neste mundo ** \n\
\n=============== TRUE ENDING ==============="

#Caso o jogador finalize com o nome Joel
texto[140] = f"\n{crianca}: E então? \n\
{nome}: E então o que? \n\
{crianca}: O que foi aquilo? Por que estavam nos atacando? \n\
{nome}: Eles descobriram sobre você \n\
{nome}: Queriam te levar para produzir uma cura... \n\
{nome}: Mas as chances eram minimas \n\
{nome}: E você morreria no processo... \n\
{crianca}: ... \n\
{nome}: Por muito tempo... tenho lutado para sobreviver \n\
{nome}: E você... seja o que for, você sempre encontra algo para viver \n\
{nome}: Eu fiz o que fosse necessario pra te tirar de lá \n\
{crianca}: Depois de tudo o que vivemos, o que fizemos, não pode ser nada... \n\
\n** {nome} e {crianca} passam suas vidas juntos, sobrevivendo neste mundo ** \n\
\n** {crianca} acredita em você ** \n\
\n=============== SECRET ENDING ==============="

def finalizar():
    while(True):
        print("\n\nDigite [ENTER] para sair")
        end = input()
        if end == "":
            exit()

if final == 1: #Sacrificar a Criança
    style(texto[132])
elif final == 2: #Salvar a Criança
    chance_guarda = random.randint(1, 2)  # Variavel aleatoria para definir se o jogador consegue se "disfarçar" (50%)
    style(texto[133])
    while(True): #Inicio do loop Choice27
        try: #Caso o usuario não insira um numero inteiro
            print()
            print(25*"=")
            print("[1] - Disfarçar-se")
            print("[2] - Nocautear")
            choice27 = int(input()) #Entrada da Choice27
            print(25*"=")
            if choice27 == 1: #[1] - Disfarçar-se
                style(texto[134])
                if chance_guarda == 1: #Caso o computador escolha 1 (50%)
                    style(texto[135])
                    mortes = mortes + 1 #Adiciona +1 ao numero de mortes
                    morte() #Chama a função Morte
                if chance_guarda == 2: #Caso o computador escolha 2 (50%)
                    style(texto[136])
                    break #Quebra o loop Choice27
            if choice27 == 2: #[2] - Nocautear
                    style(texto[137])
                    break #Quebra o loop Choice27
            else: #Caso o jogador insira um numero invalido
                print(erro)
        except ValueError:
            print(25*"=")
            print(erro)

    #Narração 18
    style(texto[138])
    if nome == "Joel":
        style(texto[140])
    else:
        style(texto[139])
else:
    print(f"Valor do final invalido! {final}")

texto[141] = "\n** Mortes durante o jogo **\n"
texto[142] = "Você completou o jogo sem morrer!"
texto[143] = "Durante o jogo você morreu 1 vez"
texto[144] = f"Durante o jogo você morreu {mortes} vezes"
texto[145] = f"\nNumero de mortes invalido: {mortes}"
texto[146] = f"\n\n** Relação com a {crianca} **\n"
texto[147] = "Sua relação com a criança foi Ruim"
texto[148] = "Sua relação com a criança foi Boa"
texto[149] = "Sua relação com a criança foi Perfeita"
texto[150] = "Sua relação com a criança foi Pessima"
texto[151] = f"\nNumero da reputação invalido: {rep_crianca}"

def tabela():
    print()
    style(texto[141])
    if mortes == 0:
        style(texto[142])
    elif mortes == 1:
        style(texto[143])
    elif mortes > 1:
        style(texto[144])
    else:
        style(texto[145])
    style(texto[146])
    if rep_crianca < 5 and rep_crianca > -7:
        style(texto[147])
    elif rep_crianca >= 5 and rep_crianca < 9:
        style(texto[148])
    elif rep_crianca >= 9:
        style(texto[149])
    elif rep_crianca <= -7:
        style(texto[150])
    else:
        style(texto[151])

texto[152] = "\n\n*** Creditos *** \n\
\nDavidson Ramos de Pádua \n\
Fabio Nakamoto Filho \n\
Gabriel Henrique Ninin \n\
Maurício Vitaliano Dolacio \n\
Lorenzo Marques Diogo\n"
texto[153] = f"\n{nome}, Obrigado por jogar!"
texto[154] = "\n\nObrigado por jogar!"

def creditos(name):
    style(texto[152])
    if name == "Joel":
        style(texto[154])
    else:
        style(texto[153])

#Tela final
tabela()
creditos(nome)
finalizar()
