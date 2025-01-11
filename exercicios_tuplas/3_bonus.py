print("Seja bem vindo")
c = 2
limite = 1000
bonus_fixo = 1000
limite_extra = 5000
sei = "deseja descubrir se alcançou o bonus?"
while True:
    print("\nSeja Bem-Vindo:", sei)
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
    