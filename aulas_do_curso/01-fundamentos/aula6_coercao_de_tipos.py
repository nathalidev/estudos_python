# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print('1', type(int('1'))) # tipo do 1 string convertido para inteiro
print(type(float('1') + 1)) # tipo do 1 string convertido a float (1.0) + 1 ou seja 2.0
print(bool(' ')) # qualquer conteudo convertido a booleano é verdadeiro pois existe algo ali
print(str(11) + 'b') # string 11b