from sonne.models.base import BaseModel


class Nomes(BaseModel):
    pass


class Nomes(BaseModel):

    def __init__(self, data):

        super().__init__(data)

        self.Nomes = [
            Nomes(item)
            for item in data.get("Nomes", [])
        ]