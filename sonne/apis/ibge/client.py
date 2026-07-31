from sonne.base.client import BaseClient

from .agregados import Agregados


class IBGEClient(BaseClient):

    def __init__(
        self,
        timeout: int = 30,
        debug: bool = False,
    ):
        super().__init__(
            base_url="https://servicodados.ibge.gov.br/api/v3",
            timeout=timeout,
            debug=debug,
        )

        self.agregados = Agregados(self)