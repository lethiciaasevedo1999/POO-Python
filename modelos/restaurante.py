#Estanciamente de uma classe 
# logo abaixo podemos ver seus atributos e definindo que tipo de valores elas irão receber
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca]

#vars - palavra reservada que vai imprimir a classe no console
print(vars(restaurante_praca.ativo))