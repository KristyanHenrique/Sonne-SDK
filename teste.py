from sonne import Sonne
sonne = Sonne()
dados = sonne.ibge.BancoGeodesico.estacoesPorEnquadramento(
    -44.0,
    -22.0,
    -43.0,
    -21.5
    # ,tipoEstacao = 'R',
    # codigoSituacao = '10',
    # tipoLocal = 'TV',
    # dataVisitaAntes = '28-08-2019',
    # dataVisitaApos = '26-08-2019',
    # nrMaxEstacoes = '100' # Max
)

from pprint import pprint
pprint(dados)