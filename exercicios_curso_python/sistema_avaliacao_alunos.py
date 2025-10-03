import sys

class Aluno:
    def __init__(self, nome, matricula, notas): # definindo atributos
        self.nome = nome
        self.matricula = matricula 
        self.notas = notas
        self.media = None 

    def __repr__(self): # definindo representação do objeto (no momento de print)
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}, Notas: {self.notas}, Média: {self.media}\n"

    def calculo_media(self): #metodo do objeto
        media = sum(self.notas)/len(self.notas)
        self.media = media
        return media
    
class Turma:
    def __init__(self, alunos):
        self.nome = "Turma A"
        self.alunos = alunos
    
    def calculo_media_geral(self, lista_de_alunos):
        media_geral = sum(aluno.media for aluno in lista_de_alunos) / len(lista_de_alunos)
        return media_geral

    def maior_media(self, lista_de_alunos):
        maior = max(lista_de_alunos, key=lambda aluno: aluno.media)
        return maior
    
    def menor_media(self, lista_de_alunos):
        menor = min(lista_de_alunos, key=lambda aluno: aluno.media)
        return menor
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def remover_aluno(self, aluno):
        self.alunos.remove(aluno)

lista_da_turma = [] # criação da lista que vai armazenar os alunos da turma
turma = Turma(lista_da_turma) # criação do objeto turma, vai receber a lista de alunos da turma
lista_de_alunos = [] #lista de alunos no geral seja de dentro ou fora da classe

while True: #loop infinito para adicionar alunos até o usuário decidir parar
    adicao_aluno = input("Deseja adicionar um aluno? (s/n) ")
    if adicao_aluno.lower() == 's':
        nome_aluno = input("Qual o nome do aluno? ")
        matricula_aluno = input("Qual o n° de matrícula do aluno? ")
        lista_notas = []
        aluno = Aluno(nome_aluno, matricula_aluno, lista_notas) # criação do objeto aluno, vai receber nome, matrícula e lista de notas
        lista_de_alunos.append(aluno)

        for i in range(3):
            nota = float(input("Digite a nota do aluno: "))
            lista_notas.append(nota)

        print(lista_de_alunos)
        aluno.calculo_media() # calculo e exibo a média de cada aluno
        print(f"A média do aluno {aluno.nome} é: {aluno.media}")

        opcao = input("Deseja adicionar o aluno a turma? (s/n) ")
        if opcao.lower() == 's':
            turma.adicionar_aluno(aluno)
            print(f"Alunos da turma {turma.nome}:\n {turma.alunos}")
            print(f"Alunos gerais:\n{lista_de_alunos}")
        elif opcao.lower() == 'n':
            remocao = input("Deseja remover algum aluno da turma? (s/n) ")
            if remocao.lower() == 's':
                if not turma.alunos:
                    print("Não há alunos na turma para remover.")
                    continue
                nome_remocao = input("Qual o nome do aluno que deseja remover? ")
                aluno_remover = next((aluno for aluno in turma.alunos if aluno.nome == nome_remocao), None)
                if aluno_remover:
                    turma.remover_aluno(aluno_remover)
                    print(f"Alunos da turma {turma.nome} após remoção:\n {turma.alunos}")
                else:
                    print("Aluno não encontrado.")
            elif remocao.lower() == 'n':
                continue
        else:
            print("Opção inválida")
            continue
    else:
        if len(lista_de_alunos)>0:
            turma.calculo_media_geral(lista_de_alunos)
            print(f"A média geral os alunos é: {turma.calculo_media_geral(lista_de_alunos)}")
        if len(turma.alunos)>0:
            turma.calculo_media_geral(turma.alunos)
            print(f"A média geral da turma é: {turma.calculo_media_geral(turma.alunos)}")
        print(f"O aluno com a maior média é: {turma.maior_media(lista_de_alunos)}")
        print(f"O aluno com a menor média é: {turma.menor_media(lista_de_alunos)}")
        print("Encerrando o programa.")
        sys.exit()


