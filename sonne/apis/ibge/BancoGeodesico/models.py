from sonne.models.base import BaseModel


class BancoGeodesico(BaseModel):
    pass


class BancoGeodesico(BaseModel):

    def __init__(self, data):

        super().__init__(data)

        self.BancoGeodesico = [
            BancoGeodesico(item)
            for item in data.get("BancoGeodesico", [])
        ]