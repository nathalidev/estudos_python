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

# O metacaractere {} é o quantificador ele define o número exato ou intervalo de repetições. Por exemplo {4} significa "exatamente quatro vezes", {2,4} significa "entre duas e quatro vezes" e {2,} significa "duas ou mais vezes".

# O metacaractere ^ (circunflexo) é usado para indicar que o padrão deve casar apenas no início da string. Por exemplo, ^Olá significa "Olá" no início da string.

# O metacaractere $ (cifrão) é usado para indicar que o padrão deve casar apenas no final da string. Por exemplo, mundo$ significa "mundo" no final da string.

# A principal diferença entre () (parênteses) e [] (colchetes) é que os parênteses buscam uma sequência exata ou grupo, enquanto os colchetes buscam qualquer um dos caracteres listados dentro deles. No re.findall, por exemplo, [aeiou] vai casar com qualquer vogal, enquanto (aeiou) vai casar apenas com a sequência "aeiou" exatamente como está.

# O metacaractere \ (barra invertida) é usado para escapar caracteres especiais, permitindo que você os trate como texto literal. Por exemplo, se você quiser buscar um ponto final (.) em uma string, você precisa usar \. no regex, caso contrário, o ponto seria interpretado como um curinga.

# O metacaractere \b é usado para indicar uma fronteira de palavra, ou seja, ele casa com a posição entre um caractere de palavra (letra, número ou sublinhado) e um caractere que não seja de palavra (como espaço ou pontuação). Por exemplo, \bpalavra\b vai casar apenas com a palavra "palavra" isolada, e não com "palavras" ou "minhapalavra".

# O metacaractere \d é usado para indicar qualquer dígito (0-9). Ele é equivalente a [0-9]. Por exemplo, \d{3} vai casar com exatamente três dígitos consecutivos.

# O metacaractere ? é usado para indicar que o elemento anterior é opcional, ou seja, ele pode aparecer zero ou uma vez. Por exemplo, colou?r vai casar com "color" e "colour".

# Os quantificadores são greedy (gananciosos) por padrão exatamente porque o motor de regex foi projetado para tentar consumir o maior trecho contínuo de texto possível antes de entregar um resultado.

# O range (intervalo) dentro dos colchetes [] funciona usando o hífen - para definir uma sequência contínua de caracteres.

# Em vez de você precisar escrever [0123456789], você escreve apenas [0-9] e o regex entende que deve aceitar qualquer caractere que esteja entre o 0 e o 9 nessa tabela.

# As flags (ou modificadores) são opções extras que você passa para o módulo re para alterar a forma como o motor do regex interpreta todo o padrão.
# Você passa a flag como o último argumento das funções (re.findall, re.search, re.compile, etc.). Se precisar combinar mais de uma, basta juntá-las usando o operador | (pipe).
# re.IGNORECASE (re.I)	Ignora a diferença entre letras maiúsculas e minúsculas.	Você não precisa escrever [a-zA-Z]. Escrever apenas [a-z] já passa a aceitar tanto a quanto A.


texto = '''Levando em conta a versão apresentada no filme Clayface (2026), a quebra psicológica de Matt Hagen acontece de forma gradual e trágica. Antes de se tornar o Clayface, Matt era um ator talentoso em ascensão, indicado ao Oscar e finalmente alcançando o sucesso pelo qual havia lutado desde sua infância difícil em Gotham. Sua identidade estava profundamente ligada à sua aparência, ao reconhecimento público e à promessa de um futuro brilhante.

Tudo muda quando ele é brutalmente desfigurado por um chefão do crime. Além de perder o rosto, Matt perde a carreira, a credibilidade e a confiança nas pessoas ao seu redor. Abandonado pela indústria, traído por aliados e ignorado pelo sistema de justiça, ele passa a enxergar o mundo como um lugar onde poder e crueldade sempre vencem.

Quando recorre a um tratamento experimental para recuperar sua aparência, ele acredita estar reconquistando a própria vida. Porém, conforme o procedimento sai do controle e seu corpo começa a se deformar novamente, o desespero dá lugar à obsessão. O medo de perder tudo pela segunda vez destrói o que restava de sua estabilidade emocional.

Como Clayface, Matt deixa de ser um homem em busca de recuperação e se transforma em alguém consumido pela dor, pelo ressentimento e pela necessidade de vingança. Sua tragédia não está apenas na mutação física, mas na perda completa de sua identidade. O ator que queria ser amado e reconhecido torna-se um monstro que acredita que a humanidade o traiu primeiro.'''

print(f"Aqui é exibido a primeira ocorrência de certa palavra mostrando a posição de inicio da ocorrência da palavra e sua posição final:\n{re.search(r'Matt', texto)}")

print(f"\nAqui levando em consideração a posição inicial de final da 1° ocorrência da palavra a ser buscada eu obtenho ela usando o fatiamento:\n{texto[88:92]}")
print(f"\nAqui podemos ver a palavra buscada pelo n° de vezes que ela aparece na string:\n{re.findall(r'Matt', texto)}")

personagem = re.compile(r'Matt') #regex ja pronto pra reutilização, boa prática ja fazer isso pra ele ficar compilado

print(f"Exibindo a primeira ocorrência da palavra a ser buscada porém  via compile dentro de variavel: \n{personagem.search(texto)}")

print(f"Todos os 'clayface' do texto independente de ser minusculo ou maiusculo:\n{re.findall(r'clayface', texto, flags=re.IGNORECASE)}")

print(f"Todos os 'clayface' ou 'matt' do texto independente de ser minusculo ou maiusculo:\n{re.findall(r'clayface|matt', texto,flags=re.IGNORECASE)}")

print(f"Imprimindo o texto substituindo 'Matt' por 'BATMAN':\n{re.sub(r'Matt', 'BATMAN', texto)}")

print(f"Imprimindo o texto substituindo 'Matt' ou 'Clayface' por '[VILÃO]':\n{re.sub(r'Matt|Clayface', '[VILÃO]', texto)}")

print(f"Pegando toda palavra do texto que começa com maiúscula e o resto minúscula:\n{re.findall(r'\b[A-Z][a-zA-ZÀ-ÿ]*', texto)}")

print(f"Pegando todo n° do texto:\n{re.findall(r'[0-9]+', texto)}")