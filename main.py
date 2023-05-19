def menor_indice(lista):
    menor_valor = min(lista)
    index = 0
    for elem in lista:
        if elem == menor_valor:
            return index
        index += 1


funcs = 0
salarios = []
valores = []
while True:
    nome, salario = input().split(",")
    salario = float(salario)

    if nome == "Fim":
        break

    dados = {
        "nome": nome,
        "salario": salario
    }

    salarios.append(dados)
    funcs += 1

if funcs == 0:
    resposta = "Não tem"
    print(resposta)
else:
    for element in salarios:
        valores.append(element["salario"])

    menor_index = menor_indice(valores)
    resposta = salarios[menor_index]["nome"]
    print(resposta)