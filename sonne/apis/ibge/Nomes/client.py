import decimal

from sonne.base.endpoint import BaseEndpoint


class Nomes(BaseEndpoint):

    PATH = "/v2/censos/nomes"

    def frequenciaPorNome(
        self,
        nome: str,
        **params,
    ):
        return self.get(
            f"{self.PATH}/{nome}",
            params=params,
        )

    def rankingPorFrequencia(
            self,
            **params
    ):
        return self.get(
            f"{self.PATH}/ranking",
            params=params,
        )


