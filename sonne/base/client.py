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
            request = requests.Request(
                method=method,
                url=url,
                **kwargs,
            )

            prepared = self.session.prepare_request(request)

            print("\n" + "=" * 80)
            print(f"{prepared.method} {prepared.url}")
            print("-" * 80)

            print("HEADERS:")
            for key, value in prepared.headers.items():
                print(f"{key}: {value}")

            print("-" * 80)
            print("BODY:")

            body = prepared.body

            if body is None:
                print("<vazio>")
            elif isinstance(body, bytes):
                print(body.decode("utf-8", errors="ignore"))
            else:
                print(body)

            print("=" * 80 + "\n")

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
            endpoint,
            data=None,
            json=None,
            files=None,
    ):
        return self.request(
            "POST",
            endpoint,
            data=data,
            json=json,
            files=files,
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

    def _handle_response(self, response):

        response.raise_for_status()

        content_type = response.headers.get(
            "Content-Type",
            ""
        )

        if "application/json" in content_type:
            return response.json()

        if "text/" in content_type:
            return response.text

        return response.content