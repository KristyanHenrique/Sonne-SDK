## IBGE
### Nomes Geográficos

[Documentação oficial](https://servicodados.ibge.gov.br/api/docs/calendario)

#### Métodos

Lista de métodos implementados para esta classe

1. calendarioPorPesquisa  
    Obtém o calendário de divulgações de uma pesquisa

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.calendario.calendarioPorPesquisa(
        '9173',
        qtd='3',
        de='2018-08-20'
    )
    ```