## IBGE
### HGeoHNOR

[Documentação oficial](https://servicodados.ibge.gov.br/api/docs/hgeohnor?versao=1)

#### Métodos

Lista de métodos implementados para esta classe

1. coordenadasDoPontoEmGrauDecimal  
    Obtém as informações de normalização para um ponto informado em coordenadas geográficas no formato de graus decimais.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.hgeohnor.coordenadasDoPontoEmGrauDecimal(
        lat='-20',
        lon='-50'
    )
    ```

2. coordenadasDoPontoEmGrauSexagecimal  
    Obtém as informações de normalização para um ponto informado em coordenadas geográficas no formato de graus, minutos e segundos.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.hgeohnor.coordenadasDoPontoEmGrauSexagecimal(
        glat='-20',
        mlat='25',
        slat='30.000',
        glon='-51',
        mlon='20',
        slon='30.000'
    )
    ```

3. listarPontosPost  
    Obtém as informações de normalização para uma lista de pontos utilizando o método **POST**. Opcionalmente, é possível informar um e-mail para recebimento do processamento.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.hgeohnor.listarPontosPost(
        [
            {
                "lat": -20.33,
                "lon": -50.56,
            },
            {
                "lat": -19.12,
                "lon": -51.84,
            }
        ],
        'irrita.cp1@gmail.com'
    )
    ```

4. listarPontosGet  
    Obtém as informações de normalização para uma lista de pontos utilizando o método **GET**. Opcionalmente, é possível informar um e-mail para recebimento do processamento.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.hgeohnor.listarPontosGet(
        [
            {
                "lat": -20.33,
                "lon": -50.56,
            },
            {
                "lat": -19.12,
                "lon": -51.84,
            }
        ],
        'irrita.cp1@gmail.com'
    )
    ```