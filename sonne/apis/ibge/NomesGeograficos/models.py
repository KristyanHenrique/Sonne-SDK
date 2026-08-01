from sonne.models.base import BaseModel


class NomesGeograficos(BaseModel):
    pass


class NomesGeograficos(BaseModel):

    def __init__(self, data):

        super().__init__(data)

        self.NomesGeograficos = [
            NomesGeograficos(item)
            for item in data.get("NomesGeograficos", [])
        ]