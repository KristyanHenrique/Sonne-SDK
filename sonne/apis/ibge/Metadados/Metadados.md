## IBGE
### Metadados

[Documentação oficial](https://servicodados.ibge.gov.br/api/docs/metadados?versao=2)

#### Métodos

Lista de métodos implementados para esta classe

1. metadadosPorPesquisaEPeriodo  
    Obtém os metadados de uma pesquisa para um período específico.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.Metadados.metadadosPorPesquisaEPeriodo(
        "CD",
        "2001"
    )
    ```

2. metadadosPorPeriodos  
    Obtém a lista de períodos disponíveis para uma pesquisa.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.Metadados.metadadosPorPeriodos(
        "CD"
    )
    ```

3. metadadosDePesquisas  
    Obtém a lista de pesquisas disponíveis no serviço de metadados.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.Metadados.metadadosDePesquisas()
    ```