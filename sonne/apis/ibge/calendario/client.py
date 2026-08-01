import decimal

from sonne.base.endpoint import BaseEndpoint


class calendario(BaseEndpoint):

    PATH = "/v3"

    def calendarioPorPesquisa(
            self,
            pesquisa: str,
            **params,
    ):

        return self.get(
            f"{self.PATH}/calendario/{pesquisa}",
            params=params,
        )