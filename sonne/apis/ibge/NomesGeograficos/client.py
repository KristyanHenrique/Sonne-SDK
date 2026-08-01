import decimal

from sonne.base.endpoint import BaseEndpoint


class NomesGeograficos(BaseEndpoint):

    PATH = "/v1/bngb"

    def listaCategoria(self):
        return self.get(f"{self.PATH}/listacategoria")

    def listaClasse(self):
        return self.get(f"{self.PATH}/listaclasse")

    def dicionario(self):
        return self.get(f"{self.PATH}/dicionario")

    def listaNomeGeo(self):
        return self.get(f"{self.PATH}/listanomegeo")

    def nomeGeografico(self, identificador: str):
        return self.get(f"{self.PATH}/nomegeografico/{identificador}")

    def nomeGeograficoPorPadrao(
            self,
            padrao: str,
            **params,
    ):

        return self.get(
            f"{self.PATH}/padrao/{padrao}/nomesgeograficos",
            params=params,
        )

    def nomeGeograficoPorMunicipio(
            self,
            geocodigo: str,
            **params,
    ):

        return self.get(
            f"{self.PATH}/municipio/{geocodigo}/nomesgeograficos",
            params=params,
        )

    def nomeGeograficoPorUF(
            self,
            sigla: str,
            **params,
    ):

        return self.get(
            f"{self.PATH}/uf/{sigla}/nomesgeograficos",
            params=params,
        )

    def nomeGeograficoPorProximidade(
            self,
            lat: decimal.Decimal,
            lon: decimal.Decimal,
            km: int,
            **params,
    ):

        return self.get(
            f"{self.PATH}/proximidade/{lat}/{lon}/{km}/nomesgeograficos",
            params=params,
        )

    def nomeGeograficoPorEnquadramento(
            self,
            lonW: decimal.Decimal,
            latS: decimal.Decimal,
            lonE: decimal.Decimal,
            latN: decimal.Decimal,
            **params,
    ):

        return self.get(
            f"{self.PATH}/enquadramento/{lonW}/{latS}/{lonE}/{latN}/nomesgeograficos",
            params=params,
        )

    def nomeGeograficoPorCategoria(
            self,
            categoria: str,
            **params,
    ):

        return self.get(
            f"{self.PATH}/categoria/{categoria}/nomesgeograficos",
            params=params,
        )

    def nomeGeograficoPorClasse(
            self,
            classe: str,
            **params,
    ):

        return self.get(
            f"{self.PATH}/classe/{classe}/nomesgeograficos",
            params=params,
        )