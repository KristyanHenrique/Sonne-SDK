from sonne.models.base import BaseModel


class calendario(BaseModel):
    pass


class calendario(BaseModel):

    def __init__(self, data):

        super().__init__(data)

        self.calendario = [
            calendario(item)
            for item in data.get("calendario", [])
        ]