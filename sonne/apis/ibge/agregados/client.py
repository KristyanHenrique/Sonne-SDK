from sonne.base.endpoint import BaseEndpoint


class Agregados(BaseEndpoint):

    PATH = "/v3/agregados"

    def listar(self):
        """Lista todos os agregados disponíveis."""
        return self.get(self.PATH)

    def metadados(self, agregado: int):
        """Retorna os metadados de um agregado."""
        return self.get(f"{self.PATH}/{agregado}/metadados")

    def periodos(self, agregado: int):
        """Retorna os períodos disponíveis para um agregado."""
        return self.get(f"{self.PATH}/{agregado}/periodos")

    def variaveis(
            self,
            agregado: int,
            **params,
    ):
        """
        Consulta o endpoint de variáveis.

        Todos os parâmetros adicionais são enviados
        como query string.
        """

        return self.get(
            f"{self.PATH}/{agregado}/variaveis",
            params=params,
        )

