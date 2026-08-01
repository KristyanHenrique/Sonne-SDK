## IBGE
### Banco de Dados Geodésicos

[Documentação oficial](https://servicodados.ibge.gov.br/api/docs/bdg?versao=1)

#### Métodos

Lista de métodos implementados para esta classe

1. estacoesPorCodigo  
    Obtém uma ou mais estações geodésicas através dos códigos de identificação informados.

        from sonne import Sonne
        sonne = Sonne()
        dados = sonne.ibge.BancoGeodesico.estacoesPorCodigo('91500|4X')

2. local  
    Obtém uma lista com os tipos de locais em que as estações geodésicas são estabelecidas.
    
        from sonne import Sonne
        sonne = Sonne()
        dados = sonne.ibge.BancoGeodesico.local()

3. situacao  
     Obtém uma lista com as situações possíveis para as estações geodésicas.

        from sonne import Sonne
        sonne = Sonne()
        dados = sonne.ibge.BancoGeodesico.situacao()

4. tipoEstacoes  
    Obtém uma lista com os tipos de estações possíveis no BDG.

        from sonne import Sonne
        sonne = Sonne()
        dados = sonne.ibge.BancoGeodesico.tipoEstacoes()

5. estacoesPorMunicipio  
    Obtém as estações geodésicas localizadas em um determinado município do Brasil a partir do respectivo identificador.  

        from sonne import Sonne
        sonne = Sonne()
        dados = sonne.ibge.BancoGeodesico.estacoesPorMunicipio(
            3300100,
            tipoEstacao = 'R',
            codigoSituacao = '10',
            tipoLocal = 'TV',
            dataVisitaAntes = '28-08-2019',
            dataVisitaApos = '26-08-2019',
            nrMaxEstacoes = '100' # Max
        )

6. estacoesPorUF  
   Obtém as estações geodésicas localizadas em uma determinada Unidade da Federação (estado) do Brasil a partir da respectiva sigla.
   
        from sonne import Sonne
        sonne = Sonne()
        dados = sonne.ibge.BancoGeodesico.estacoesPorUF(
            'RJ',
            tipoEstacao = 'R',
            codigoSituacao = '10',
            tipoLocal = 'TV',
            dataVisitaAntes = '28-08-2019',
            dataVisitaApos = '26-08-2019',
            nrMaxEstacoes = '100' # Max
        )

7. estacoesPorProximidade  
     Obtém as estações geodésicas localizadas próximas a coordenada informada, considerando uma distância em Km.

        from sonne import Sonne
        sonne = Sonne()
        dados = sonne.ibge.BancoGeodesico.estacoesPorProximidade(
            -23.45,
            -44.75,
            100,
            tipoEstacao = 'R',
            codigoSituacao = '10',
            tipoLocal = 'TV',
            dataVisitaAntes = '28-08-2019',
            dataVisitaApos = '26-08-2019',
            nrMaxEstacoes = '100' # Max
        )

8. estacoesPorEnquadramento  
   Obtém as estações geodésicas localizadas no retângulo envolvente definido pelas coordenadas informadas.  

        from sonne import Sonne
        sonne = Sonne()
        dados = sonne.ibge.BancoGeodesico.estacoesPorEnquadramento(
            -44.0,
            -22.0,
            -43.0,
            -21.5
            # ,tipoEstacao = 'R',
            # codigoSituacao = '10',
            # tipoLocal = 'TV',
            # dataVisitaAntes = '28-08-2019',
            # dataVisitaApos = '26-08-2019',
            # nrMaxEstacoes = '100' # Max
        )