#Função calculadora
def calculadora():

#Loop Infinito com 'while e True'
    while True:
#Menu de Operações
        print("\nOperações disponíveis: ")
        print("1: Soma")
        print("2: Substração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
#Escolha da Operação
        escolha = input("Escolha o número da operação desejada: ")
    
#Verificação da Escolha
        if escolha == '0':
            print("Sainda da calculadora. Até mais!")
            break
#Se o usuário escolher '0', o programa exibe uma mensagem de saída e sai do loop, encerrando a calculadora.

#Execução da Operação Escolhida
        elif escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))

#Realização da Operação e Exibição do Resultado
        if escolha == '1':
            resultado = num1 + num2
            print("Resultado da Soma:", resultado)

        elif escolha == '2':
            resultado = num1 - num2
            print("Resultado da subtração:", resultado)

        elif escolha == '3':
            resultado = num1 * num2
            print("Resultado da multiplicação:", resultado)

        elif escolha == '4':
            if num2 != 0:
                resultado = num1 / num2
                print("Resultado da Divisão:", resultado)

#Tratamento de Opções Inválidas
            else:
                print("Erro: Divisão por zero não permitida.")
#Se o usuário inserir uma escolha inválida (que não seja '0', '1', '2', '3' ou '4'), mostramos uma mensagem de erro e voltamos ao início do loop.

#Chamar a Função Calculadora
calculadora()