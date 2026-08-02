from sonne.models.base import BaseModel


class cnae(BaseModel):
    pass


class cnae(BaseModel):

    def __init__(self, data):

        super().__init__(data)

        self.cnae = [
            cnae(item)
            for item in data.get("Cnae", [])
        ]