print("Bem Vindo!")
produtos = ["celular", "pc", "video", "telefone", "jogos"]

while True:  
    print("\nLista de produtos disponíveis:", produtos)
    respostaplayer = input("Digite um produto desejado (ou 'sair' para encerrar): ").strip().lower()
    
    if respostaplayer == "sair":
        print("Obrigado por usar!")
        break  

    if respostaplayer in produtos:
        print(f"Produto {respostaplayer} já existe, tente novamente!")
    
    else:
        produtos.append(respostaplayer) 
        print(f"O produto {respostaplayer} foi cadastrado com sucesso!")



'''
Crie um sistema de cadastro de produtos em uma lista de produtos
Seu sistema deve:
- Pegar o usuário qual produto vai ser cadastrado por meio de um input
- Garantir que se o usuário escrever com letra maiúscula ou minúscula, o produto continua sendo o mesmo produto
- Se o usuário inserir um produto que já existe na lista, o programa deve printar a mensagem "Produto já existente, tente novamente"
- Se o usuário inserir um produto que não existe na lista, o programa deve inserir na lista, printar a mensagem Produto X cadastrado com sucesso e em seguida printar a lista completa
'''





