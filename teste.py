from sonne import Sonne
sonne = Sonne()

dados = sonne.ibge.agregados.variaveis(
    1712,
    localidades="BR",
    periodos="-12",
    classificacao="226[4844,96608,96609]|218[4780]",
    view = "flat"
)

from pprint import pprint
pprint(dados)








