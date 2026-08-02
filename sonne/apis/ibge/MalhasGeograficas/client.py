import decimal

from sonne.base.endpoint import BaseEndpoint

class MalhasGeograficas(BaseEndpoint):

    PATH = "/v4/malhas"

    def malhasPorMunicipio(
            self,
            id: int,
            **params,
    ):

        return self.get(
            f"{self.PATH}/municipios/{id}",
            params=params,
        )

    def malhasPorUF(
            self,
            uf: str,
            **params,
    ):

        return self.get(
            f"{self.PATH}/estados/{uf}",
            params=params,
        )

    def malhasPorPais(
            self,
            id: str,
            **params,
    ):

        return self.get(
            f"{self.PATH}/paises/{id}",
            params=params,
        )

    def malhasPorRegiao(
            self,
            id: str,
            **params,
    ):

        return self.get(
            f"{self.PATH}/regioes/{id}",
            params=params,
        )

    def malhasPorRegiaoImediata(
            self,
            id: str,
            **params,
    ):

        return self.get(
            f"{self.PATH}/regioes-imediatas/{id}",
            params=params,
        )

    def malhasPorRegiaoIntermediaria(
            self,
            id: str,
            **params,
    ):

        return self.get(
            f"{self.PATH}/regioes-intermediarias/{id}",
            params=params,
        )

    def metadadosDaMalhaPorUF(self, id: str):
        return self.get(f"{self.PATH}/estados/{id}/metadados")

    def metadadosDaMalhaPorMunicipio(self, id: str):
        return self.get(f"{self.PATH}/municipios/{id}/metadados")

    def metadadosDaMalhaPorPais(self, id: str):
        return self.get(f"{self.PATH}/paises/{id}/metadados")

    def metadadosDaMalhaPorRegiao(self, id: str):
        return self.get(f"{self.PATH}/regioes/{id}/metadados")

    def metadadosDaMalhaPorRegiaoImediata(self, id: str):
        return self.get(f"{self.PATH}/regioes-imediatas/{id}/metadados")

    def metadadosDaMalhaPorRegiaoIntermediaria(self, id: str):
        return self.get(f"{self.PATH}/regioes-intermediarias/{id}/metadados")