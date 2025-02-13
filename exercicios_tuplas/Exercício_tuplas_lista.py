# Exercício 1
'''
Crie um sistema de cadastro de produtos em uma lista de produtos
Seu sistema deve:
- Pegar o usuário qual produto vai ser cadastrado por meio de um input
- Garantir que se o usuário escrever com letra maiúscula ou minúscula, o produto continua sendo o mesmo produto
- Se o usuário inserir um produto que já existe na lista, o programa deve printar a mensagem "Produto já existente, tente novamente"
- Se o usuário inserir um produto que não existe na lista, o programa deve inserir na lista, printar a mensagem Produto X cadastrado com sucesso e em seguida printar a lista completa
'''

import cgitb


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







# Exercício 2
'''
Crie um sistema de consulta de preços. Seu sistema deve:
- Pedir para o usuário o nome de um produto
- Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
- Ex: O produto celular custa R$1500
- Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente
'''


lista_de_produtos = ["celular", "pc", "tv"]
precos = [1500, 2000, 100]

print("Lista de valores dos produtos disponíveis:", lista_de_produtos)

while True:
    
    resposta_comprador = input("Digite qual produto deseja saber o valor (ou 'sair' para encerrar): ").strip().lower()

    if resposta_comprador == "sair":
        print("Obrigado pela preferência!")
        break
    elif resposta_comprador in lista_de_produtos:
        
        indice = lista_de_produtos.index(resposta_comprador)
        
        print(f"O valor do produto '{resposta_comprador}' custa {precos[indice]}")
    else:
        print("Produto inválido, tente novamente!")










# Exercício 3
'''
Crie um sistema de consulta de bônus dos funcionários
Seu sistema deve:
- Pegar o valor de vendas do funcinoário por meio de um input
- Calcular o bônus do funcionário de acordo com a seguinte regra:
- Se o funcionário vendeu mais de 1000 unidades, ele ganha R$2 de bonus
para cada unidade vendida
- Se o funcionário vendeu mais de 5000 unidades, ele ganha R$2 de bônus
para cada unidade + um valor fixo de R$1000
- Se o funcionário vendeu menos de 1000 unidades, ele não ganha bônus
- Printar no final o valor do bônus do funcionário
'''
  

print("Seja bem vindo")
c = 2
limite = 1000
bonus_fixo = 1000
limite_extra = 5000
sei = "deseja descubrir se alcançou o bonus?"
while True:
    print("\nola:", sei)
    resposta_funcionario = input("digite seu numero de vendas(ou digite sair para fechar a pagina!):").lower().strip()
    if resposta_funcionario == "sair":
        print("Obrigado por usar!")
        break 
    
    resposta_funcionario = int(resposta_funcionario)
    

    
    if resposta_funcionario > limite_extra :
        bonus = (resposta_funcionario) * c + bonus_fixo
        print(f"parabens você conseguiu um bonus de {bonus}")
    elif resposta_funcionario > limite:
        benus = (resposta_funcionario) * c
        print(f"parabens você recebeu o bonus maximo! o valor total foi de {benus}" )
    else:
        print(f"seu total foi de {resposta_funcionario} pois voce nao atingiu o bonus")
    
















# Exercícios de tuplas
'''
## 1. Análise de Vendas
Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.
Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.
meta = 10000
vendas = [
('João', 15000),
('Julia', 27000),
('Marcus', 9900),
('Maria', 3750),
('Ana', 10300),
('Alon', 7870),
]
'''

meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]


for vendedor, valor in vendas:
    if valor >= meta:
        print(f'{vendedor} bateu a meta com vendas de R${valor}')











# Exercícios de dicionário
# Exercício 1
'''
Crie um sistema de consulta de preços
Seu sistema deve:
- Pedir para o usuário o nome de um produto
- Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
- Ex: O produto celular custa R$1500
- Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente
precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}
'''

# Exercício 2
'''
Agora edite o programa anterior para fazer com que, caso não exista o produto, o programa pergunte se o usuário quer cadastrar o produto
Se ele responder sim, o programa deve pedir o nome do produto e o preco do produto e cadastrar no dicionário de preços
Em seguida do cadastro bem sucedido, o programa deve printar o dicionário de precos atualizado
'''
# Exercício 3
'''
Dada a lista de preços de produtos, uma loja resolveu fazer um reajuste nos preços dos produtos.
calcule o novo valor dos produtos com base nas seguintes regras:
Preços até 1.000 vão ter um reajuste de 10% (ou seja, o novo preço será 110% do preço atual)
Preços até maiores que 1.000 até 2.000 vão ter reajuste de 15%
Preços acima de 2.000 vão ter reajuste de 20%
precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}
'''