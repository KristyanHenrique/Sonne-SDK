from sonne.base.client import BaseClient
from .BancoGeodesico import BancoGeodesico
from .agregados import Agregados


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