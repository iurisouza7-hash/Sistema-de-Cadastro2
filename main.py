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
            telefone = input("Telefone: Ex: (85)1234567890 ")
            
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
        

        case "3":
            email_nome_login = input("Nome ou E-mail: ")
            senha_login = input("Senha: ")

            try:
                usuarios = json.load(open(ARQUIVO))
            except:
                usuarios = []

            encontrado = False

            for usuario in usuarios:
                if (usuario["email"] == email_nome_login or usuario["nome"] == email_nome_login) and usuario["senha"] == senha_login:
                    print("✅ Login realizado!")
                    encontrado = True

                    quantidade_dados = int(input("\n1 -- Nome\n2 -- Idade\n3 -- E-mail\n4 -- Cidade\n5 -- Telefone\nQuantos dados deseja alterar: "))

                    for _ in range(quantidade_dados):
                        opcao = input("Escolha o campo (1 a 5): ")

                        match opcao:
                            case "1":
                                usuario["nome"] = input("Novo nome: ")
                            case "2":
                                usuario["idade"] = int(input("Nova idade: "))
                            case "3":
                                usuario["email"] = input("Novo email: ")
                            case "4":
                                usuario["cidade"] = input("Nova cidade: ")
                            case "5":
                                usuario["telefone"] = input("Novo telefone: ")

                    break  

            if not encontrado:
                print("❌ Dados incorretos!")

                
            with open(ARQUIVO, "w") as f:
                json.dump(usuarios, f, indent=4)
        
        case "4":
                    
            email_nome = input("Nome ou E-mail do usuário: ")
            senha = input("Senha: ")

            try:
                usuarios = json.load(open(ARQUIVO))
            except:
                usuarios = []

            encontrado = False

            for usuario in usuarios:
                if (usuario["email"] == email_nome or usuario["nome"] == email_nome) and usuario["senha"] == senha:
                    

                    confirm = input("Tem certeza? (s/sim): ").strip().lower()
                            
                    if confirm in ["s", "sim"]:
                        usuarios.remove(usuario)
                        print("🗑️ Usuário deletado!")
                        break
                    elif confirm in ["n", "nao", "não"]:
                        print("❌ Cancelado!")
                        break
                    else:
                        print("Digite apenas s/sim ou n/não")
                    

                if not encontrado:
                    print("❌ Usuário não encontrado ou senha incorreta!")

            with open(ARQUIVO, "w") as f:
                json.dump(usuarios, f, indent=4)
        case _:
            print("Opção inválida!")
            print("Escolha outra opção!!!!")
        
