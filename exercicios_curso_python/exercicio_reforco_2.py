# Cadastro simples

# Crie um dicionário chamado aluno com as chaves: "nome", "idade" e "curso".

# Depois, adicione a chave "nota_final" com um valor numérico.

# Atualize a idade para um número diferente.

# Por fim, percorra o dicionário imprimindo chave => valor.

# aluno = {}
# try:
#     aluno['Nome'] = input("Qual o nome do aluno?\n")
#     aluno['Idade'] = int(input("\nQual a idade do aluno?\n"))
#     aluno['Curso'] = input("\nQual o curso do aluno?\n")
#     aluno["Nota Final"] = float(input("\nQual a nota final do aluno?\n"))

# except Exception as e:
#     print(f"\nErro ao inserir dados: {e}\n")

# idade_nova = float(input("\nQual a nova idade do aluno:\n"))

# aluno.update({'idade': idade_nova})
# print("\n")
# for chave,valor in aluno.items():
#     print(f"{chave} : {valor}")

# ----------------------------------------------------------------------------------------------

palavras = ["python", "java", "python", "c", "python", "java"]

contagem = {}

# for palavra in palavras:   ideia do chatgpt            
#     contagem[palavra] = contagem.get(palavra, 0) + 1
    # .get() pega o valor atual da chave (0 se não existir) e soma 1
# VANTAGEM: percorre a lista apenas uma vez

# ------------------- Ideia com set() -------------------
contagem = {}

for palavra in set(palavras):  # percorre apenas palavras únicas
    contagem[palavra] = palavras.count(palavra)
    # .count() ainda percorre a lista inteira, mas só uma vez por palavra única
# VANTAGEM: evita repetir count para palavras duplicadas, mas ainda menos eficiente que .get() em listas grandes

print(contagem)

# -----------------------------------------------------------------------------------------------




