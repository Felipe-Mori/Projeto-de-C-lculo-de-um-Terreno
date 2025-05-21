
# importei o math para resolver o cálculo da raiz quadrada
import math

# Aqui o usuário irá inserir os valores
base_retangulo = float(input('Digite o valor da Base Retangulo: '))
altura_retangulo = float(input('Digite o valor da Altura: '))

# Aqui foram feitos os calculos da (Área, Perimetro e a Diagonal do retângulo)
area_retangulo = base_retangulo * altura_retangulo
perimetro_retangulo = 2*(base_retangulo + altura_retangulo)
diagonal_retangulo = math.sqrt(base_retangulo**2 + altura_retangulo**2)

#Arredondei o valor decimal para duas casas
diagonal_retangulo = round(diagonal_retangulo, 4)

#Pulei uma linha para facilitar a visualização
print()

# Mostrando os Resultados
print(f'O valor da Base Retangulo é {base_retangulo}')
print(f'O valor da Altura é {altura_retangulo}')
print(f'O valor da área do retangulo é {area_retangulo}')
print(f'O valor do perimetro do retangulo é {perimetro_retangulo:.4f}')
print(f'O valor da diagonal do retangulo é {diagonal_retangulo}')