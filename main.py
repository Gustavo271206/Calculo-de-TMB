def calcular_tmb():
    print("=== CÁLCULO DE TMB ===")
    genero = int(input("Digite seu gênero (1 para masculino, 2 para feminino): "))
    peso = float(input("Digite seu peso em kg: "))
    altura = int(input("Digite sua altura em centímetros: "))
    idade = int(input("Digite sua idade: "))
    if genero=1:
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
        print (f"Sua tbm é de {tmb.2f} calorias por dia.")
    else:        
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
        print (f"Sua tbm é de {tmb.2f} calorias por dia.")
    calcular_tmb()