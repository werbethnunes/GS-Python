def qtd_C02(cons_mensal):
    #Calcula a emissão mensal de CO2 com base no consumo.
    emisskwh = 0.233  # Emissão média de CO2 por kWh
    return cons_mensal * emisskwh

def qtd_painel(cons_mensal):
    #Calcula o número de painéis solares necessários para suprir o consumo mensal.
    gerapainel = 40  # Cada painel gera aproximadamente 40 kWh por mês (média)
    return cons_mensal / gerapainel

def calc_economia(val_conta, anos=25):
    #Calcula a economia total ao longo de 25 anos utilizando energia solar.
    return val_conta * 12 * anos

def salvar_txt(nome, dados_usuario, resultados, beneficios):
    #Salva os dados, resultados e benefícios no arquivo de texto.
    try:
        with open("relatorio.txt", "a") as arquivo:  
            arquivo.write(f"Relatorio Energetico - {nome}\n")
            arquivo.write("=" * 40 + "\n")
            for chave, valor in dados_usuario.items():
                arquivo.write(f"{chave}: {valor}\n")
            arquivo.write("\nResultados:\n")
            for chave, valor in resultados.items():
                arquivo.write(f"{chave}: {valor}\n")
            arquivo.write("\nBeneficios de Utilizar Energia Solar:\n")
            for beneficio in beneficios:
                arquivo.write(f"- {beneficio}\n")
            arquivo.write("=" * 40 + "\n\n")
        print(f"\nRelatório salvo para {nome}!")
    except Exception as e:
        print(f"\nErro ao salvar o relatório: {e}")

print("Olá Bem-vindo ao Simulador de Impacto Energético!")
print("Vamos te ajudar a migrar para uma energia mais limpa e sustentável.")
print()

while True:
    try:
        # Entrada de dados do usuário
        nome = input("Digite seu nome: ")
        cons_mensal = float(input("Digite seu consumo mensal em kWh: "))
        val_conta = float(input("Digite o valor da sua conta de energia em R$: "))
        
        if cons_mensal <= 0 or val_conta <= 0:
            raise ValueError("Os valores devem ser maiores que zero.")
        
        # Processa os cálculos das funções
        emissaodeCO2 = qtd_C02(cons_mensal)
        num_paineis = qtd_painel(cons_mensal)
        economia_total = calc_economia(val_conta)

        # Armazena os resultados do usuário
        resultados = {
            "Emissao de CO2 (kg/mes)": f"{emissaodeCO2:.2f}",
            "Numero de Paineis Necessarios para seu consumo": f"{num_paineis:.1f}",
            "Economia Total em 25 anos, se comecar a utilizar Energia Solar (R$)": f"{economia_total:.2f}"
        }

        # Beneficios de usar energia solar
        beneficios = [
            "Reducao significativa nos custos de energia eletrica.",
            "Diminuicao na emissao de gases do efeito estufa (CO2).",
            "Independencia da rede eletrica em casos de aumento tarifario.",
            "Contribuicao para um futuro mais sustentavel e limpo.",
        ]

        # Exibe os resultados
        print(f"\nResultados para {nome}:")
        for chave, valor in resultados.items():
            print(f"{chave}: {valor}")
        
        print("\nBeneficios de Utilizar Energia Solar:")
        for beneficio in beneficios:
            print(f"- {beneficio}")

        # Salva os resultados e benefícios no arquivo
        dados_usuario = {
            "Nome": nome,
            "Consumo Mensal (kWh)": cons_mensal,
            "Valor da Conta (R$)": val_conta
        }
        salvar_txt(nome, dados_usuario, resultados, beneficios)
    
    except ValueError as ve:
        print(f"Erro de entrada: {ve}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    
    # Pergunta se deseja continuar para outra pessoa
    continuar = input("\nDeseja realizar o cálculo para outra pessoa? (s/n): ").lower()
    if continuar != 's':
        print("Encerrando o simulador. Obrigado!")
        break
