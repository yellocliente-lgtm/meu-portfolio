while True:
    operacao = input("Digite a operação (+, -, *, /) ou 'saída' para encerrar: ")

    if operacao.lower() == "saída":
        print("Calculadora encerrada.")
        break

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        if numero2 == 0:
            print("Erro: não é possível dividir por zero.")
            continue numero1 = float(input("Digite o primeiro número: "))
        resultado = numero1 / numero2
    else:
        print("Operação inválida.")
        continue

    print("Resultado:", resultado)
    operacao = input("Digite a operação ou 'saída' para encerrar: ")

 saída