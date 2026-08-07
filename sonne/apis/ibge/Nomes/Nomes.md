## IBGE
### Nomes

[Documentação oficial](https://servicodados.ibge.gov.br/api/docs/nomes?versao=2)

#### Métodos

Lista de métodos implementados para esta classe

1. frequenciaPorNome  
    Obtém a frequência de ocorrência de um ou mais nomes, podendo ser filtrada por sexo.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.Nomes.frequenciaPorNome(
        "Pedro|jorge",
        sexo="F"
    )
    ```

2. rankingPorFrequencia  
    Obtém o ranking de frequência dos nomes, podendo ser filtrado por sexo e década.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.Nomes.rankingPorFrequencia(
        sexo="F",
        decada="1950"
    )
    ```