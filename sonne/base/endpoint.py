from __future__ import annotations
from typing import Any
from sonne.base.client import BaseClient


class BaseEndpoint:
    """
    Classe base para todos os endpoints da Sonne.
    """

    def __init__(self, client: BaseClient) -> None:
        self.client = client

    def get(self, endpoint: str, params: dict[str, Any] | None = None):
        return self.client.get(endpoint, params=params)

    def post(
            self,
            endpoint,
            data=None,
            json=None,
            files=None,
    ):
        return self.client.post(
            endpoint,
            data=data,
            json=json,
            files=files,
        )

    def put(self, endpoint: str, data: dict[str, Any] | None = None):
        return self.client.put(endpoint, data=data)

    def delete(self, endpoint: str):
        return self.client.delete(endpoint)