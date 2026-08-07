## IBGE
### Notícias

[Documentação oficial](https://servicodados.ibge.gov.br/api/docs/noticias?versao=3)

#### Métodos

Lista de métodos implementados para esta classe

1. noticias  
    Obtém as notícias publicadas pelo IBGE, permitindo filtrar pelo tipo de conteúdo.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.Noticias.noticias(
        tipo="releases"
    )
    ```