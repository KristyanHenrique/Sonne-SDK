from sonne.apis import PROVIDERS


class Sonne:
    """
    Cliente principal da biblioteca Sonne.
    """

    def __init__(
        self,
        timeout: int = 30,
        debug: bool = False,
    ):
        self.timeout = timeout
        self.debug = debug

        self._providers = {}

    def __getattr__(self, name: str):
        if name in self._providers:
            return self._providers[name]

        provider = PROVIDERS.get(name)

        if provider is None:
            raise AttributeError(
                f"Provider '{name}' não encontrado."
            )

        instance = provider(
            timeout=self.timeout,
            debug=self.debug,
        )

        self._providers[name] = instance

        return instance