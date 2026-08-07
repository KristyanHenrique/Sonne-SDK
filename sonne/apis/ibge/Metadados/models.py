from sonne.models.base import BaseModel


class Metadados(BaseModel):
    pass


class Metadados(BaseModel):

    def __init__(self, data):

        super().__init__(data)

        self.Metadados = [
            Metadados(item)
            for item in data.get("Metadados", [])
        ]