# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Car:
    def __init__(self, name):
        self.name = name
        self._engine = None
        self._factory = None
    
    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, value):
        self._engine = value
    
    @property
    def factory(self):
        return self._factory
    
    @factory.setter
    def factory(self, value):
        self._factory = value


class Engine:
    def __init__(self, name):
        self.name = name


class Manufacturer:
    def __init__(self, name):
        self.name = name


opala = Car('Opala kk')
opala_engine = Engine('Opala engine kk')
chevrolet_factory = Manufacturer('Chevrolet')

opala.engine = opala_engine
opala.factory = chevrolet_factory
print(f'Nome do carro {opala.name} motor {opala.engine.name} fabrica {opala.factory.name}')