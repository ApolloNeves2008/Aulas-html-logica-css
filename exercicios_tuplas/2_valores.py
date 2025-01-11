
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

   



