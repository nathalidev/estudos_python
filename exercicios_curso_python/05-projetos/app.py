from calculadora import somar, multiplicar

print(somar(11, 9))
print(multiplicar(6, 4))
print("Dentro de app.py:", __name__)

"""Observações referente a modularização:
modularização é o processo de dividir um programa em partes menores e independentes, chamadas de módulos, para facilitar manutenção, reutilização de código e organização;

módulo é um arquivo Python que contém funções, classes ou variáveis que podem ser importadas e utilizadas em outros arquivos;

sempre que eu executar o __name__ no arquivo em si ele será '__main__', pois isso indica que o arquivo está sendo executado diretamente como ponto de entrada do programa;

se eu tenho __name__ em um arquivo importado no arquivo da importação, esse __name__ vai vir como o nome do módulo importado, e não '__main__';

se eu importo funções de um arquivo mas não as acesso, vai rodar todo o código do arquivo que está fora das funções/classes (top-level);

se eu utilizo as funções importadas, só o código dentro das funções será executado, e o que estiver fora delas será ignorado se estiver protegido com 'if __name__ == "__main__":'.
"""
