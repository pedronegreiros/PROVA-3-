#ALUNO: PEDRO NEGREIROS ANDRADE

alunos = {} 

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite o número de matrícula do aluno: ")
    alunos[matricula] = nome
    print(f"Aluno {nome} adicionado com sucesso!\n")

def remover_aluno():
    matricula = input("Digite o número de matrícula do aluno que deseja remover: ")
    if matricula in alunos:
        nome = alunos.pop(matricula)
        print(f"Aluno {nome} removido com sucesso!\n")
    else:
        print("Matrícula não encontrada.\n")

def visualizar_alunos():
    if alunos:
        print("Lista de Alunos:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")
        print()
    else:
        print("Nenhum aluno registrado.\n")

while True:
    print("Escolha uma opção:")
    print("1. Adicionar Aluno")
    print("2. Remover Aluno")
    print("3. Visualizar Alunos")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        adicionar_aluno()
    elif opcao == "2":
        remover_aluno()
    elif opcao == "3":
        visualizar_alunos()
    elif opcao == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.\n")

