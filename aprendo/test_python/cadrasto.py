# Lista para armazenar os cadastros
cadastros = []

def adicionar_pessoa():
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("E-mail: ")
    
    pessoa = {"Nome": nome, "Idade": idade, "Email": email}
    cadastros.append(pessoa)
    print(f"\n✅ {nome} foi cadastrado com sucesso!\n")

def listar_pessoas():
    if not cadastros:
        print("\n⚠️ Nenhuma pessoa cadastrada.\n")
    else:
        print("\n📋 Lista de Pessoas Cadastradas:")
        for i, pessoa in enumerate(cadastros, 1):
            print(f"{i}. {pessoa['Nome']} - {pessoa['Idade']} anos - {pessoa['Email']}")
        print()

def buscar_pessoa():
    nome_busca = input("Digite o nome para buscar: ")
    encontrados = [p for p in cadastros if p["Nome"].lower() == nome_busca.lower()]
    
    if encontrados:
        print("\n🔍 Resultado da busca:")
        for p in encontrados:
            print(f"Nome: {p['Nome']} - Idade: {p['Idade']} - E-mail: {p['Email']}")
    else:
        print("\n⚠️ Nenhuma pessoa encontrada com esse nome.\n")

def remover_pessoa():
    nome_remover = input("Digite o nome para remover: ")
    global cadastros
    cadastros = [p for p in cadastros if p["Nome"].lower() != nome_remover.lower()]
    print(f"\n✅ Cadastro de {nome_remover} removido com sucesso!\n")

# Menu principal
while True:
    print("📌 MENU:")
    print("1️⃣ - Adicionar pessoa")
    print("2️⃣ - Listar cadastros")
    print("3️⃣ - Buscar pessoa")
    print("4️⃣ - Remover pessoa")
    print("0️⃣ - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_pessoa()
    elif opcao == "2":
        listar_pessoas()
    elif opcao == "3":
        buscar_pessoa()
    elif opcao == "4":
        remover_pessoa()
    elif opcao == "0":
        print("👋 Saindo...")
        break
    else:
        print("⚠️ Opção inválida! Tente novamente.\n")