from sonne.models.base import BaseModel


class MalhasGeograficas(BaseModel):
    pass


class MalhasGeograficas(BaseModel):

    def __init__(self, data):

        super().__init__(data)

        self.MalhasGeograficas = [
            MalhasGeograficas(item)
            for item in data.get("MalhasGeograficas", [])
        ]