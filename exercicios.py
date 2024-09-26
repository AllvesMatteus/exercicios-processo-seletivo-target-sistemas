def exercicio_1():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K += 1
        SOMA += K

    print(f"Resultado do Exercício 1 (SOMA): {SOMA}")


def exercicio_2():
    def is_fibonacci(num):
        a, b = 0, 1
        while a < num:
            a, b = b, a + b
        return a == num

    numero = int(input("Informe um número: "))
    
    if is_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

def exercicio_3():
    import json
    with open('dados.json', 'r') as file:
        faturamento_data = json.load(file)

    faturamento_valores = [dia["valor"] for dia in faturamento_data["dias"] if dia.get("valor", 0) > 0]

    if not faturamento_valores:
        print("Nenhum valor de faturamento disponível para análise.")
        return

    menor_faturamento = min(faturamento_valores)
    maior_faturamento = max(faturamento_valores)
    media_mensal = sum(faturamento_valores) / len(faturamento_valores)
    dias_acima_da_media = len([f for f in faturamento_valores if f > media_mensal])

    print(f"Menor faturamento: R${menor_faturamento:.2f}")
    print(f"Maior faturamento: R${maior_faturamento:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")


def exercicio_4():
    faturamento_por_estado = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    faturamento_total = sum(faturamento_por_estado.values())

    for estado, valor in faturamento_por_estado.items():
        percentual = (valor / faturamento_total) * 100
        print(f"{estado}: {percentual:.2f}%")


def exercicio_5():
    def inverte_string(string):
        invertida = ""
        for i in range(len(string)-1, -1, -1):
            invertida += string[i]
        return invertida

    entrada = input("Informe a string a ser invertida: ")
    print(f"String invertida: {inverte_string(entrada)}")


def menu():
    while True:
        print("\n--- Menu de Exercícios ---")
        print("1 - Exercício 1: Soma dos números até 13")
        print("2 - Exercício 2: Verificar se número pertence à sequência de Fibonacci")
        print("3 - Exercício 3: Faturamento diário de uma distribuidora")
        print("4 - Exercício 4: Percentual de faturamento por estado")
        print("5 - Exercício 5: Inverter string")
        print("6 - Sair")

        opcao = input("Escolha uma opção de 1 a 6: ")

        if opcao == "1":
            exercicio_1()
        elif opcao == "2":
            exercicio_2()
        elif opcao == "3":
            exercicio_3()
        elif opcao == "4":
            exercicio_4()
        elif opcao == "5":
            exercicio_5()
        elif opcao == "6":
            print("Desenvolvido por: Mateus - GitHub AllvesMatteus")
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()
