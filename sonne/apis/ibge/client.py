from sonne.base.client import BaseClient
from .BancoGeodesico import BancoGeodesico
from .NomesGeograficos import NomesGeograficos
from .MalhasGeograficas import MalhasGeograficas
from .Calendario import calendario
from .Hgeohnor import hgeohnor
from .Localidade import localidade
from .Metadados import Metadados
from .Cnae import cnae
from .Agregados import Agregados
from .Nomes import Nomes
from .Noticias import Noticias


class IBGEClient(BaseClient):

    def __init__(
        self,
        timeout: int = 30,
        debug: bool = False,
    ):
        super().__init__(
            base_url="https://servicodados.ibge.gov.br/api/",
            timeout=timeout,
            debug=debug,
        )

        self.agregados = Agregados(self)
        self.BancoGeodesico = BancoGeodesico(self)
        self.NomesGeograficos = NomesGeograficos(self)
        self.calendario = calendario(self)
        self.cnae = cnae(self)
        self.hgeohnor = hgeohnor(self)
        self.localidade = localidade(self)
        self.MalhasGeograficas = MalhasGeograficas(self)
        self.Metadados = Metadados(self)
        self.Nomes = Nomes(self)
        self.Noticias = Noticias(self)


