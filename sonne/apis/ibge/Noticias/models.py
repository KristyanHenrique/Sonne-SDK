from sonne.models.base import BaseModel


class Noticias(BaseModel):
    pass


class Noticias(BaseModel):

    def __init__(self, data):

        super().__init__(data)

        self.Noticias = [
            Noticias(item)
            for item in data.get("Noticias", [])
        ]