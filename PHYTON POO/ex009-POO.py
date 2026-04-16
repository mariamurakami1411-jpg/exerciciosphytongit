class Latino:
    # Atributo de classe
    cont='America do Sul'

    def __init__(self, nome):
        self.nome= nome

    def outro(self):
         self.cont= ('América do Norte', 'América Central' 'Europa', 'África', 'Ásia', 'Oceania')
         return ('Não é da América do Sul.')

    @staticmethod
    def paises():
        substantivos= (
             'Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colombia',
             'Equador', 'Guiana', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela'
             )
        return tuple(f'{subst}'for subst in substantivos)
    
    @classmethod
    def is_brasileiro(cls):
         return cls.cont == cls.paises()[2]


class Argentina(Latino):
    cont = Latino.paises()[0]

class Bolivia(Latino):
    cont=Latino.paises()[1]

class Brasil(Latino):
    cont=Latino.paises()[2]

class Chile(Latino):
    cont=Latino.paises()[3]

class Colombia(Latino):
    cont=Latino.paises()[4]


gabriel = Argentina('Gabriel')
antonio = Brasil('Antonio')
print(f'Países América do Sul: {", ".join(Brasil.paises())}')
print(f'Gabriel é brasileiro? {Argentina.is_brasileiro()}')
print(f'Antonio é brasileiro? {Brasil.is_brasileiro()}')

    

