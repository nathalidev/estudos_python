aluno = {}
try:
    aluno['Nome'] = input("Qual o nome do aluno?\n")
    aluno['Idade'] = int(input("\nQual a idade do aluno?\n"))
    aluno['Curso'] = input("\nQual o curso do aluno?\n")
    aluno["Nota Final"] = float(input("\nQual a nota final do aluno?\n"))

except Exception as e:
    print(f"\nErro ao inserir dados: {e}\n")

idade_nova = float(input("\nQual a nova nota final do aluno:\n"))

aluno.update({'idade': idade_nova})
print("\n")
for chave,valor in aluno.items():
    print(f"{chave} : {valor}")




