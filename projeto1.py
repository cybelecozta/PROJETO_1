alunos = []

#CRIAR UM PROGRAMA DE CADASTRO ESCOLAR

opcao = input("\nCOMO POSSO AJUDAR?\n1 - CADASTRAR ALUNO. \n2 - LISTAR ALUNOS. \n3 - BUSCAR ALUNO. \n4 - MÉDIA \n0 - SAIR\n\n")

if opcao == "1":
    nome = input("Nome: ")
    idade = input("Idade: ")
    nota = float(input("Nota: "))
elif opcao == "2":
    print("\nLISTA DE ALUNOS: ")
    for nome in alunos:
        print(f"Nome: {opcao['nome']}")
elif opcao == "3":
    busca = input("Buscar: ")
    encontrado = False
    for opcao in alunos:
        if opcao["nome"].lower():
            print(f"Nome: {opcao['nome']}, idade: {opcao['idade']}, Nota: {opcao['nota']}")
            encontrado = True
            break
    if not encontrado:
       print("Aluno não encontrado")
elif opcao == "4":
    if len(alunos)>0:
        soma_notas = sum(opcao['nota'] for opcao in alunos)
        media = soma_notas/len(alunos)
        print(f"Média da turma: {media:.2f}")
    else:
        print("Não há notas cadastradas.")
elif opcao == "0":
    print("Encerrando o programa.")

else:
    print("OPÇÃO INVALIDA")