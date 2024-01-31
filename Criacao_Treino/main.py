lista_exercicio_perna=[]
lista_exercicio_peito=[]
lista_exercicio_braço=[]
lista_exercicio_ombro=[]
lista_exercicio_costas=[]
def criar_lista_de_exercicio_perna():

    while True:
        item = input('Digite um exercício para seu treino de Perna ou digite "sair" para encerrar: ')

        if item.lower() == 'sair':
            break

        else:
            lista_exercicio_perna.append(item)
    return lista_exercicio_perna

criar_lista_de_exercicio_perna()

def criar_lista_de_exercicio_peito():

    while True:
        item = input('Digite um exercício para seu treino de Peito ou digite "sair" para encerrar: ')

        if item.lower() == 'sair':
            break

        else:
            lista_exercicio_peito.append(item)
    return lista_exercicio_peito


criar_lista_de_exercicio_peito()

def criar_lista_de_exercicio_Braço():

    while True:
        item = input('Digite um exercício para seu treino de Braço ou digite "sair" para encerrar: ')

        if item.lower() == 'sair':
            break

        else:
            lista_exercicio_braço.append(item)
    return lista_exercicio_braço


criar_lista_de_exercicio_Braço()

def criar_lista_de_exercicio_ombro():

    while True:
        item = input('Digite um exercício para seu treino de Ombro ou digite "sair" para encerrar: ')

        if item.lower() == 'sair':
            break

        else:
            lista_exercicio_ombro.append(item)

    lista_exercicio_ombro

criar_lista_de_exercicio_ombro()


def criar_lista_de_exercicio_Costas():

    while True:
        item = input('Digite um exercício para seu treino de Costas ou digite "sair" para encerrar: ')

        if item.lower() == 'sair':
            break

        else:
            lista_exercicio_costas.append(item)

    lista_exercicio_costas

criar_lista_de_exercicio_Costas()

Treino_de_hoje=(input('Para ver o treino de pernas digite Perna\nPara ver o treino de peito digite Peito\nPara ver o treino de braço digite Braço\nPara ver o treino de costas digite Costas\nPara ver o treino de ombro digite Ombro\nqual treino você deseja consultar?'))

Lista_Exercicio_FinalPrint = {
    'Perna': lista_exercicio_perna,
    'Peito': lista_exercicio_peito,
    'Braço': lista_exercicio_braço,
    'Ombro': lista_exercicio_ombro,
    'Costas': lista_exercicio_costas

}


if Treino_de_hoje == 'Perna':
    print('Lista de Exercicio de Perna:')
    for item in Lista_Exercicio_FinalPrint[Treino_de_hoje]:
        print(f'- {item}')

elif Treino_de_hoje == 'Peito':
    print('Lista de Exercicio de Peito:')
    for item in Lista_Exercicio_FinalPrint[Treino_de_hoje]:
        print(f'- {item}')


elif Treino_de_hoje == 'Braço':
    print('Lista de Exercicio de Braço:')
    for item in Lista_Exercicio_FinalPrint[Treino_de_hoje]:
        print(f'- {item}')

elif Treino_de_hoje == 'Ombro':
    print('Lista de Exercicio de Ombro:')
    for item in Lista_Exercicio_FinalPrint[Treino_de_hoje]:
        print(f'- {item}')


elif Treino_de_hoje == 'Costas':
    print('Lista de Exercicio de Costas:')
    for item in Lista_Exercicio_FinalPrint[Treino_de_hoje]:
        print(f'- {item}')
else:
    print('DIGITE NOVAMENTE')



