"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')

# | Símbolo | Significado                                                         |
# | ------- | ------------------------------------------------------------------- |
# | `0=`    | Preenche com **zeros** à esquerda, **depois do sinal** (`+` ou `-`) |
# | `+`     | Sempre mostra o **sinal** (`+` positivo ou `-` negativo)            |
# | `10`    | A **largura total** do campo deve ser 10 caracteres                 |
# | `,`     | Coloca **vírgulas** como separador de milhar                        |
# | `.1f`   | Formato **float** com **1 casa decimal fixa**                       |
