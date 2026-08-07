from pprint import pprint
from sonne import Sonne

sonne = Sonne()
dados = sonne.ibge.Noticias.noticias(
    tipo = "releases"
)

pprint(dados)