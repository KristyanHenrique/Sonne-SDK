from requests import Session


class BaseClient:

    def __init__(
        self,
        base_url: str,
        timeout: int = 30,
        debug: bool = False,
    ) -> None:

        self._base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.debug = debug

        self.session = Session()

    @property
    def base_url(self) -> str:
        return self._base_url

    def build_url(
        self,
        endpoint: str
    ) -> str:

        return f"{self.base_url}{endpoint}"

    def request(
            self,
            method: str,
            endpoint: str,
            **kwargs,
    ):
        url = self.build_url(endpoint)

        if self.debug:
            print(f"{method} {url}")

            if kwargs.get("params"):
                print(f"Params: {kwargs['params']}")

        response = self.session.request(
            method=method,
            url=url,
            timeout=self.timeout,
            **kwargs,
        )

        return self._handle_response(response)

    def get(
        self,
        endpoint: str,
        params: dict | None = None,
    ):

        return self.request(
            "GET",
            endpoint,
            params=params,
        )

    def post(
        self,
        endpoint: str,
        json: dict | None = None,
    ):

        return self.request(
            "POST",
            endpoint,
            json=json,
        )

    def put(
        self,
        endpoint: str,
        json: dict | None = None,
    ):

        return self.request(
            "PUT",
            endpoint,
            json=json,
        )

    def delete(
        self,
        endpoint: str,
    ):

        return self.request(
            "DELETE",
            endpoint,
        )

    def _handle_response(
        self,
        response,
    ):

        response.raise_for_status()

        return response.json()