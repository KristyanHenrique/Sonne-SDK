from sonne.models.base import BaseModel


class localidade(BaseModel):
    pass


class localidade(BaseModel):

    def __init__(self, data):

        super().__init__(data)

        self.localidade = [
            localidade(item)
            for item in data.get("Localidade", [])
        ]