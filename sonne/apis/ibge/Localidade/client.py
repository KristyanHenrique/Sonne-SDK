import json

from sonne.base.endpoint import BaseEndpoint


class localidade(BaseEndpoint):

    PATH = "/v1/localidades"

    def listarRegioes(
            self,
            **params,
    ):
        return self.get(
            f"{self.PATH}/regioes",
            params=params,
        )

    def listarRegiao(
            self,
            regiao,
            **params,
    ):
        return self.get(
            f"{self.PATH}/regioes/{regiao}",
            params=params,
        )

    def listarMunicipiosDaRegiao(
            self,
            regiao,
            **params,
    ):
        return self.get(
            f"{self.PATH}/regioes/{regiao}/municipios",
            params=params,
        )

    def listarUFs(
            self,
            **params,
    ):
        return self.get(
            f"{self.PATH}/estados",
            params=params,
        )

    def listarUF(
            self,
            uf,
            **params,
    ):
        return self.get(
            f"{self.PATH}/estados/{uf}",
            params=params,
        )

    def listarMunicipiosDaUF(
            self,
            uf,
            **params,
    ):
        return self.get(
            f"{self.PATH}/estados/{uf}/municipios",
            params=params,
        )

    def listarMesorregioesDaUF(
            self,
            uf,
            **params,
    ):
        return self.get(
            f"{self.PATH}/estados/{uf}/mesorregioes",
            params=params,
        )

    def listarMicrorregioesDaUF(
            self,
            uf,
            **params,
    ):
        return self.get(
            f"{self.PATH}/estados/{uf}/microrregioes",
            params=params,
        )

    def listarRegioesIntermediariasDaUF(
            self,
            uf,
            **params,
    ):
        return self.get(
            f"{self.PATH}/estados/{uf}/regioes-intermediarias",
            params=params,
        )

    def listarRegioesImediatasDaUF(
            self,
            uf,
            **params,
    ):
        return self.get(
            f"{self.PATH}/estados/{uf}/regioes-imediatas",
            params=params,
        )

    def listarMunicipios(
            self,
            **params,
    ):
        return self.get(
            f"{self.PATH}/municipios",
            params=params,
        )

    def listarMunicipio(
            self,
            municipio,
            **params,
    ):
        return self.get(
            f"{self.PATH}/municipios/{municipio}",
            params=params,
        )

    def listarMunicipiosDaMesorregiao(
            self,
            mesorregiao,
            **params,
    ):
        return self.get(
            f"{self.PATH}/mesorregioes/{mesorregiao}/municipios",
            params=params,
        )

    def listarMunicipiosDaMicrorregiao(
            self,
            microrregiao,
            **params,
    ):
        return self.get(
            f"{self.PATH}/microrregioes/{microrregiao}/municipios",
            params=params,
        )

    def listarMunicipiosDaRegiaoIntermediaria(
            self,
            regiaoIntermediaria,
            **params,
    ):
        return self.get(
            f"{self.PATH}/regioes-intermediarias/{regiaoIntermediaria}/municipios",
            params=params,
        )

    def listarMunicipiosDaRegiaoImediata(
            self,
            regiaoImediata,
            **params,
    ):
        return self.get(
            f"{self.PATH}/regioes-imediatas/{regiaoImediata}/municipios",
            params=params,
        )

    def listarMesorregioes(
            self,
            **params,
    ):
        return self.get(
            f"{self.PATH}/mesorregioes",
            params=params,
        )

    def listarMesorregiao(
            self,
            mesorregiao,
            **params,
    ):
        return self.get(
            f"{self.PATH}/mesorregioes/{mesorregiao}",
            params=params,
        )

    def listarMicrorregioes(
            self,
            **params,
    ):
        return self.get(
            f"{self.PATH}/microrregioes",
            params=params,
        )

    def listarMicrorregiao(
            self,
            microrregiao,
            **params,
    ):
        return self.get(
            f"{self.PATH}/microrregioes/{microrregiao}",
            params=params,
        )

    def listarRegioesIntermediarias(
            self,
            **params,
    ):
        return self.get(
            f"{self.PATH}/regioes-intermediarias",
            params=params,
        )

    def listarRegiaoIntermediaria(
            self,
            regiaoIntermediaria,
            **params,
    ):
        return self.get(
            f"{self.PATH}/regioes-intermediarias/{regiaoIntermediaria}",
            params=params,
        )

    def listarRegioesImediatas(
            self,
            **params,
    ):
        return self.get(
            f"{self.PATH}/regioes-imediatas",
            params=params,
        )

    def listarRegiaoImediata(
            self,
            regiaoImediata,
            **params,
    ):
        return self.get(
            f"{self.PATH}/regioes-imediatas/{regiaoImediata}",
            params=params,
        )

    def listarDistritos(
            self,
            **params,
    ):
        return self.get(
            f"{self.PATH}/distritos",
            params=params,
        )

    def listarDistrito(
            self,
            distrito,
            **params,
    ):
        return self.get(
            f"{self.PATH}/distritos/{distrito}",
            params=params,
        )

    def listarSubdistritos(
            self,
            **params,
    ):
        return self.get(
            f"{self.PATH}/subdistritos",
            params=params,
        )

    def listarSubdistrito(
            self,
            subdistrito,
            **params,
    ):
        return self.get(
            f"{self.PATH}/subdistritos/{subdistrito}",
            params=params,
        )

    def listarPaises(
            self,
            **params,
    ):
        return self.get(
            f"{self.PATH}/paises",
            params=params,
        )

    def listarPais(
            self,
            pais,
            **params,
    ):
        return self.get(
            f"{self.PATH}/paises/{pais}",
            params=params,
        )