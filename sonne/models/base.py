class BaseModel:

    def __init__(self, data: dict):

        self._data = data

        for key, value in data.items():
            setattr(
                self,
                key,
                self._parse_value(value)
            )

    def _parse_value(self, value):

        if isinstance(value, dict):
            return BaseModel(value)

        if isinstance(value, list):
            return [
                self._parse_value(item)
                for item in value
            ]

        return value