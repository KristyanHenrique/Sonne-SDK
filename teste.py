from sonne import Sonne
sonne = Sonne()

dados = sonne.ibge.calendario.calendarioPorPesquisa(
    '9173',
    qtd='3',
    de='2018-08-20'
)

from pprint import pprint
pprint(dados)