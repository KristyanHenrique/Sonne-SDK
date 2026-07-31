from sonne.models.base import BaseModel


class Agregado(BaseModel):
    pass


class PesquisaAgregado(BaseModel):

    def __init__(self, data):

        super().__init__(data)

        self.agregados = [
            Agregado(item)
            for item in data.get("agregados", [])
        ]