import decimal

from sonne.base.endpoint import BaseEndpoint


class cnae(BaseEndpoint):

    PATH = "/v2/Cnae"

    def listaClasses(self):
        return self.get(f"{self.PATH}/classes")

    def classePorIdentificador(self, classe: str):
        return self.get(f"{self.PATH}/classes/{classe}")

    def classesPorDivisao(self, divisao: str):
        return self.get(f"{self.PATH}/divisoes/{divisao}/classes")

    def classesPorGrupo(self, grupo: str):
        return self.get(f"{self.PATH}/grupos/{grupo}/classes")

    def classesPorSecao(self, secao: str):
        return self.get(f"{self.PATH}/secoes/{secao}/classes")

    def listaDivisoes(self):
        return self.get(f"{self.PATH}/divisoes")

    def divisaoPorIdentificador(self, divisao: str):
        return self.get(f"{self.PATH}/divisoes/{divisao}")

    def divisoesPorSecao(self, secao: str):
        return self.get(f"{self.PATH}/secoes/{secao}/divisoes")

    def listaGrupos(self):
        return self.get(f"{self.PATH}/grupos")

    def gruposPorDivisao(self, divisao: str):
        return self.get(f"{self.PATH}/divisoes/{divisao}/grupos")

    def grupoPorIdentificador(self, grupo: str):
        return self.get(f"{self.PATH}/grupos/{grupo}")

    def gruposPorSecao(self, secao: str):
        return self.get(f"{self.PATH}/secoes/{secao}/grupos")

    def listaSecoes(self):
        return self.get(f"{self.PATH}/secoes")

    def secaoPorIdentificador(self, secao: str):
        return self.get(f"{self.PATH}/secoes/{secao}")

    def listaSubclasses(self):
        return self.get(f"{self.PATH}/subclasses")

    def subclassePorIdentificador(self, subclasse: str):
        return self.get(f"{self.PATH}/subclasses/{subclasse}")

    def subclassesPorClasse(self, classe: str):
        return self.get(f"{self.PATH}/classes/{classe}/subclasses")

    def subclassesPorDivisao(self, divisao: str):
        return self.get(f"{self.PATH}/divisoes/{divisao}/subclasses")

    def subclassesPorGrupo(self, grupo: str):
        return self.get(f"{self.PATH}/grupos/{grupo}/subclasses")

    def subclassesPorSecao(self, secao: str):
        return self.get(f"{self.PATH}/secoes/{secao}/subclasses")

































