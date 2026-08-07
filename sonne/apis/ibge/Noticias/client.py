import decimal

from sonne.base.endpoint import BaseEndpoint


class Noticias(BaseEndpoint):

    PATH = "/v3"

    def noticias(
        self,
        **params,
    ):
        return self.get(
            f"{self.PATH}/noticias/",
            params=params,
        )


