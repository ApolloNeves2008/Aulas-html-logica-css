'''Crie um sistema de consulta de preços
Seu sistema deve:
- Pedir para o usuário o nome de um produto
- Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
- Ex: O produto celular custa R$1500
- Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente
precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}'''

print("Bem vindo")

precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}


while True:
    print("\nprodutos disponiveis!:", precos )
    resposta_cliente = input("qual produto esta proucurando?").lower().strip()
    if resposta_cliente == "sair":
     print("Obrigado por usar")
    break

if resposta_cliente in precos:
    print(f"o produto {precos} custa {precos}")
else:
    print("tente novamente!")

      


