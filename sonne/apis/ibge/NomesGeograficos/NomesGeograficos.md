## IBGE
### Nomes Geográficos

[Documentação oficial](https://servicodados.ibge.gov.br/api/docs/bngb)

#### Métodos

Lista de métodos implementados para esta classe

1. listaCategoria  
    Obtém uma lista de categorias, de acordo com a EDGV 3.0, que estão contempladas no Banco de Nomes Geográficos do Brasil (BNGB)  

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.NomesGeograficos.listaCategoria()
    ```

2. listaClasse  
    Obtém uma lista de classes, de acordo com a EDGV 3.0, que estão contempladas no Banco de Nomes Geográficos do Brasil (BNGB).    

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.NomesGeograficos.listaClasse()
    ```

3. dicionario  
    Obtém traduções de termos da API para inglês, espanhol e descrições em português para uso como “labels” em portais  

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.NomesGeograficos.dicionario()
    ```

4. listaNomeGeo  
    Obtém a lista dos nomes geográficos que constam no BNGB  

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.NomesGeograficos.listaNomeGeo()
    ```

5. nomeGeografico  
    Obtém um único nome geográfico a partir do identificador informado.  

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.NomesGeograficos.nomeGeografico(198252)
    ```

6. nomeGeograficoPorPadrao  
    Obtém os nomes geográficos que tenham o padrão informado no nome.  

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.NomesGeograficos.nomeGeograficoPorPadrao(
        'sao paulo',
        statusValidacao='S'
    )
    ```

7. nomeGeograficoPorMunicipio  
    Obtém os nomes geográficos localizadas em um determinado município a partir do geocódigo informado.  

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.NomesGeograficos.nomeGeograficoPorMunicipio(
        3300100,
        categoria='Hidrografia'
    )
    ```

8. nomeGeograficoPorUF  
    Obtém os nomes geográficos localizados em um estado a partir da sigla de identificação da unidade da federação informada.  

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.NomesGeograficos.nomeGeograficoPorUF(
        'RJ',
        categoria='Hidrografia'
    )
    ```

9. nomeGeograficoPorProximidade  
    Obtém os nomes geográficos localizados próximos a coordenada informada, considerando uma distância em Km.  

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.NomesGeograficos.nomeGeograficoPorProximidade(
        -41.45,
        -20.75,
        5,
        padrao='Pireneu'
    )
    ```

10. nomeGeograficoPorEnquadramento  
    Obtém os nomes geográficos localizados no retângulo envolvente definido pelas coordenadas informadas.  

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.NomesGeograficos.nomeGeograficoPorEnquadramento(
        -44.0,
        -22.0,
        -43.0,
        -21.5
    )
    ```

11. nomeGeograficoPorCategoria  
    Obtém os nomes geográficos que pertencem a categoria informada.  

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.NomesGeograficos.nomeGeograficoPorCategoria(
        'Hidrografia',
        statusValidacao='S',
        padrao='São Paulo'
    )
    ```

12. nomeGeograficoPorClasse  
    Obtém os nomes geográficos que pertencem a classe informada.  

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.NomesGeograficos.nomeGeograficoPorClasse(
        'trecho_drenagem,vila',
        statusValidacao='S',
        padrao='São Paulo'
    )
    ```