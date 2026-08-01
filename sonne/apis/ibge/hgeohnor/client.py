import json

from sonne.base.endpoint import BaseEndpoint


class hgeohnor(BaseEndpoint):

    PATH = "/v1/hgeohnor"

    def listarPontosPost(
            self,
            pontos,
            email=None,
    ):
        files = {
            "pontos": (
                None,
                json.dumps(pontos)
            )
        }

        if email:
            files["email"] = (
                None,
                email
            )

        return self.post(
            f"{self.PATH}/pontos",
            files=files
        )

    def listarPontosGet(
            self,
            pontos,
            email=None,
    ):
        params = {
            "pontos": json.dumps(pontos)
        }

        if email:
            params["email"] = email

        return self.get(
            f"{self.PATH}/pontos",
            params=params,
        )

    def coordenadasDoPontoEmGrauDecimal(
            self,
            **params,
    ):

        return self.get(
            f"{self.PATH}/ponto_dec",
            params=params,
        )

    def coordenadasDoPontoEmGrauSexagecimal(
            self,
            **params,
    ):

        return self.get(
            f"{self.PATH}/ponto_gms",
            params=params,
        )