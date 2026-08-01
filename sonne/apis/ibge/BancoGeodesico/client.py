import decimal

from sonne.base.endpoint import BaseEndpoint


class BancoGeodesico(BaseEndpoint):

    PATH = "/v1/bdg"

    def estacoesPorCodigo(self, estacao: str):
        return self.get(f"{self.PATH}/estacoes/{estacao}")

    def tipoEstacoes(self):
        return self.get(f"{self.PATH}/tipo")

    def situacao(self):
        return self.get(f"{self.PATH}/situacao")

    def local(self):
        return self.get(f"{self.PATH}/local")

    def estacoesPorMunicipio(
            self,
            geocodigo: int,
            **params,
    ):

        return self.get(
            f"{self.PATH}/municipio/{geocodigo}/estacoes",
            params=params,
        )

    def estacoesPorUF(
            self,
            uf: str,
            **params,
    ):

        return self.get(
            f"{self.PATH}/estado/{uf}/estacoes",
            params=params,
        )

    def estacoesPorProximidade(
            self,
            lat: decimal.Decimal,
            lon: decimal.Decimal,
            km: int,
            **params,
    ):

        return self.get(
            f"{self.PATH}/proximidade/{lat}/{lon}/{km}/estacoes",
            params=params,
        )

    def estacoesPorEnquadramento(
            self,
            lonW: decimal.Decimal,
            latS: decimal.Decimal,
            lonE: decimal.Decimal,
            latN: decimal.Decimal,
            **params,
    ):

        return self.get(
            f"{self.PATH}/enquadramento/{lonW}/{latS}/{lonE}/{latN}/estacoes",
            params=params,
        )


