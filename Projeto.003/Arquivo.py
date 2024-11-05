nome = (input('Nome: '))
idade = int(input('Idade: '))
peso = float(input('Peso: '))
altura = float(input('Altura: '))
nascionalidade = (input('Nascionalidade: '))
profissao = (input('Profissão: '))

usuario = {
    "nome": nome,
    "idade": idade,
    "peso": peso,
    "altura": altura,
    "nacionalidade": nascionalidade,
    "profissao": profissao
}

print("\nInformações do usuário:")
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}")
