operacao=input("Digite qual operação você deseja realizar (soma/sub/mult/div): ")

def captacao():
    x = int(input("Digite o primeiro valor: "))
    y = int(input("Digite o segundo valor: "))
    return x, y

if (operacao == "soma"):
    x, y = captacao()
    z = float(x) + float(y)
    print("O resultado da soma é {z}")

if (operacao=="sub"):
    x, y = captacao()
    z = float(x) - float(y)
    print("O resultado da subtracao é {z}")

if (operacao=="mult"):
    x, y = captacao()
    z = float(x) * float(y)
    print("O resultado da multiplicacao é {z}")

if (operacao=="div"):
    x, y = captacao()
    if y==0 :
        print("Divisão por zero não existe!")
    z = float(x) / float(y)
    print("O resultado da divisão é {z}")

else:
    print("Operação inválida. Tente novamente. ")





