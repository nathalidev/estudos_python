import sys

class Aluno:
    def __init__(self, nome, matricula, notas, media):
        self.nome = nome
        self.matricula = matricula 
        self.notas = notas
        self.media = media

    def calculo_media(self):
        media = sum(self.notas)/len(self.notas)
        return media

nome_aluno = input("Qual o nome do aluno? ")

matricula_aluno = input("Qual o n° de matrícula do aluno? ")

lista_de_notas = []

for i in range(3):
    nota = float(input("Digite a nota do aluno: "))
    lista_de_notas.append(nota)

aluno = Aluno(nome_aluno, matricula_aluno, lista_de_notas)




