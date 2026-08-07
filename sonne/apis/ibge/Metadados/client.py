import decimal

from sonne.base.endpoint import BaseEndpoint


class Metadados(BaseEndpoint):

    PATH = "/v2/metadados"

    def metadadosPorPesquisaEPeriodo(
            self,
            pesquisa: str,
            YYYY: str,
            MM: str = None,
            order: str = 0,
            **params
    ):
        if MM is None:
            return self.get(
                f"{self.PATH}/{pesquisa}/{YYYY}",
                params=params
            )
        else:
            return self.get(
                f"{self.PATH}/{pesquisa}/{YYYY}/{MM}/{order}",
                params=params
            )


    def metadadosPorPeriodos(self,pesquisa: str):
        return self.get(f"{self.PATH}/pesquisas/{pesquisa}/periodos")

    def metadadosDePesquisas(self):
        return self.get(f"{self.PATH}/pesquisas")