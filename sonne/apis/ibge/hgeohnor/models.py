from sonne.models.base import BaseModel


class hgeohnor(BaseModel):
    pass


class hgeohnor(BaseModel):

    def __init__(self, data):

        super().__init__(data)

        self.hgeohnor = [
            hgeohnor(item)
            for item in data.get("hgeohnor", [])
        ]