import json

ARQUIVO = "usuarios.json"

while True:
    
    print("\n=== MENU ===")
    print("0 - Sair")
    print("1 - Adicionar usuário")
    print("2 - Listar usuários")
    print("3 - Editar usuário")
    print("4 - Deletar usuário")
    
    opcao = input("Escolha: ")


    match opcao:
        case "0":
            print("Encerrando...")
            break
        case "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            email = input("Email: ")
            telefone = input("Telefone: ")
            cidade = input("Cidade: ")
            senha = input("Senha: ")

          
            try:
                with open(ARQUIVO, "r") as f:
                    usuarios = json.load(f)
            except:
                usuarios = []

            
            novo_usuario = {
                "nome": nome,
                "idade": idade,
                "email": email,
                "telefone": telefone,
                "cidade": cidade,
                "senha": senha
            }

            
            usuarios.append(novo_usuario)

            
            with open(ARQUIVO, "w") as f:
                json.dump(usuarios, f, indent=4)

            print("✅ Usuário salvo!")

        case "2":
            
            try:
                usuarios = json.load(open(ARQUIVO))
            except:
                usuarios = []
            if usuarios:
                for usuario, dados in enumerate(usuarios):
                    print(f"{usuario} - Nome: {dados['nome']} | Idade: {dados['idade']} | Email: {dados['email']} | Tel: {dados['telefone']} | Cidade: {dados['cidade']}")
            else:
                print("Nenhum usuário cadastrado.")
            
        case _:
            print("Opção inválida!")
            print("Escolha outra opção!!!!!")
        
