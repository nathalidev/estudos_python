import re

# Para usar regex em Python, você importa o módulo re e utiliza funções principais:
# • re.search(): Procura a primeira ocorrência do padrão em uma string.
# • re.findall(): Retorna uma lista com todas as partes do texto que correspondem ao padrão.
# • re.sub(): Substitui os trechos que casam com o padrão por outra string.
# • re.compile(): Compila a expressão regular em um objeto para reutilização.

# Imagine que você trabalha em uma triagem de cartas.

# Sem re:

# Python
# for caractere in texto:
# # analisar um por um

# Você abre carta por carta.

# Com re:

# Python
# re.findall(...)

# Você diz:

# "Me entregue todas as cartas que tenham o formato de um telefone."

# O trabalho pesado fica por conta da biblioteca.

# ditado = "Em terra de saci todo chute é voadora"

# print(re.search(r'saci', ditado))
# print(re.findall(r'saci', ditado))
# print(re.sub(r'saci', 'aleijado', ditado))

# regexp = re.compile(r'saci')
# regexp.search(ditado)

# nesse caso eu ja uso de dentro do search pois eu defini o regexp 
# como o regex do saci, e chamando o search nessa variavel o regex 
# ja está armazenado ali por si só.

#metacaracteres: .^$*+?{}[]\|()

# E o que são metacaracteres?

# Metacaracteres são caracteres que têm um significado especial dentro de uma expressão regular, funcionando como comandos ou curingas em vez de representarem a si mesmos como texto comum.

# O metacaractere OU (representado pela barra vertical |) não faz a busca parar na primeira palavra que encontrar. Ele apenas diz ao motor do regex que qualquer uma daquelas opções é um casamento válido a cada passo que ele dá pelo texto.

# O metacaractere . (ponto) é o curinga universal das expressões regulares e representa qualquer caractere único (seja letra, número, espaço ou símbolo), com uma única exceção por padrão: ele não casa com quebras de linha (\n).

# Os colchetes [] criam uma lista personalizada de caracteres permitidos (chamada de classe de caracteres).
# Ele funciona como um operador OU exclusivo para caracteres individuais. Por exemplo, [aeiou] significa "a, ou e, ou i, ou o, ou u".

# O range (intervalo) dentro dos colchetes [] funciona usando o hífen - para definir uma sequência contínua de caracteres.

# Em vez de você precisar escrever [0123456789], você escreve apenas [0-9] e o regex entende que deve aceitar qualquer caractere que esteja entre o 0 e o 9 nessa tabela.

# As flags (ou modificadores) são opções extras que você passa para o módulo re para alterar a forma como o motor do regex interpreta todo o padrão.
# Você passa a flag como o último argumento das funções (re.findall, re.search, re.compile, etc.). Se precisar combinar mais de uma, basta juntá-las usando o operador | (pipe).
# re.IGNORECASE (re.I)	Ignora a diferença entre letras maiúsculas e minúsculas.	Você não precisa escrever [a-zA-Z]. Escrever apenas [a-z] já passa a aceitar tanto a quanto A.


texto = '''Levando em conta a versão apresentada no filme Clayface (2026), a quebra psicológica de Matt Hagen acontece de forma gradual e trágica. Antes de se tornar o Clayface, Matt era um ator talentoso em ascensão, indicado ao Oscar e finalmente alcançando o sucesso pelo qual havia lutado desde sua infância difícil em Gotham. Sua identidade estava profundamente ligada à sua aparência, ao reconhecimento público e à promessa de um futuro brilhante.

Tudo muda quando ele é brutalmente desfigurado por um chefão do crime. Além de perder o rosto, Matt perde a carreira, a credibilidade e a confiança nas pessoas ao seu redor. Abandonado pela indústria, traído por aliados e ignorado pelo sistema de justiça, ele passa a enxergar o mundo como um lugar onde poder e crueldade sempre vencem.

Quando recorre a um tratamento experimental para recuperar sua aparência, ele acredita estar reconquistando a própria vida. Porém, conforme o procedimento sai do controle e seu corpo começa a se deformar novamente, o desespero dá lugar à obsessão. O medo de perder tudo pela segunda vez destrói o que restava de sua estabilidade emocional.

Como Clayface, Matt deixa de ser um homem em busca de recuperação e se transforma em alguém consumido pela dor, pelo ressentimento e pela necessidade de vingança. Sua tragédia não está apenas na mutação física, mas na perda completa de sua identidade. O ator que queria ser amado e reconhecido torna-se um monstro que acredita que a humanidade o traiu primeiro.'''

print(re.search(r'Matt', texto))
print(texto[88:92])
print(re.findall(r'Matt', texto))
personagem = re.compile(r'Matt')
print(personagem.search(texto))
print(re.findall(r'clayface', texto, flags=re.IGNORECASE))
print(re.findall(r'clayface|matt', texto,flags=re.IGNORECASE))
print(re.sub(r'Matt', 'BATMAN', texto))
print(re.sub(r'Matt|Clayface', '[VILÃO]', texto))
print(re.findall(r'\b[A-Z][a-zA-ZÀ-ÿ]*', texto))
print(re.findall(r'[0-9]+', texto))