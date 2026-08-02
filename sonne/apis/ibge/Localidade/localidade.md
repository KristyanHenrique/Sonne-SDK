## IBGE
### Localidade

[Documentação oficial](https://servicodados.ibge.gov.br/api/docs/localidades?versao=1)

#### Métodos

Lista de métodos implementados para esta classe

## Regiões

1. listarRegioes  
    Obtém a lista de todas as regiões geográficas do Brasil.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarRegioes()
    ```

2. listarRegiao  
    Obtém as informações de uma região específica através do seu código identificador.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarRegiao(
        1
    )
    ```

3. listarMunicipiosDaRegiao  
    Obtém a lista de municípios pertencentes a uma determinada região.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarMunicipiosDaRegiao(
        1
    )
    ```

---

## UFs

4. listarUFs  
    Obtém a lista de todas as unidades federativas brasileiras.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarUFs()
    ```

5. listarUF  
    Obtém as informações de uma unidade federativa através do seu código identificador.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarUF(
        35
    )
    ```

6. listarMunicipiosDaUF  
    Obtém a lista de municípios pertencentes a uma determinada unidade federativa.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarMunicipiosDaUF(
        35
    )
    ```

7. listarMesorregioesDaUF  
    Obtém a lista de mesorregiões pertencentes a uma unidade federativa.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarMesorregioesDaUF(
        35
    )
    ```

8. listarMicrorregioesDaUF  
    Obtém a lista de microrregiões pertencentes a uma unidade federativa.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarMicrorregioesDaUF(
        35
    )
    ```

9. listarRegioesIntermediariasDaUF  
    Obtém a lista de regiões geográficas intermediárias pertencentes a uma unidade federativa.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarRegioesIntermediariasDaUF(
        35
    )
    ```

10. listarRegioesImediatasDaUF  
    Obtém a lista de regiões geográficas imediatas pertencentes a uma unidade federativa.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarRegioesImediatasDaUF(
        35
    )
    ```

---

## Municípios

11. listarMunicipios  
    Obtém a lista de todos os municípios brasileiros.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarMunicipios()
    ```

12. listarMunicipio  
    Obtém as informações de um município através do seu código identificador.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarMunicipio(
        3550308
    )
    ```

---

## Mesorregiões

13. listarMesorregioes  
    Obtém a lista de todas as mesorregiões brasileiras.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarMesorregioes()
    ```

14. listarMesorregiao  
    Obtém as informações de uma mesorregião através do seu código identificador.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarMesorregiao(
        3501
    )
    ```

15. listarMunicipiosDaMesorregiao  
    Obtém a lista de municípios pertencentes a uma determinada mesorregião.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarMunicipiosDaMesorregiao(
        3501
    )
    ```

---

## Microrregiões

16. listarMicrorregioes  
    Obtém a lista de todas as microrregiões brasileiras.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarMicrorregioes()
    ```

17. listarMicrorregiao  
    Obtém as informações de uma microrregião através do seu código identificador.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarMicrorregiao(
        35061
    )
    ```

18. listarMunicipiosDaMicrorregiao  
    Obtém a lista de municípios pertencentes a uma determinada microrregião.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarMunicipiosDaMicrorregiao(
        35061
    )
    ```

---

## Regiões Intermediárias

19. listarRegioesIntermediarias  
    Obtém a lista de todas as regiões geográficas intermediárias brasileiras.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarRegioesIntermediarias()
    ```

20. listarRegiaoIntermediaria  
    Obtém as informações de uma região geográfica intermediária através do seu código identificador.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarRegiaoIntermediaria(
        3501
    )
    ```

21. listarMunicipiosDaRegiaoIntermediaria  
    Obtém a lista de municípios pertencentes a uma região geográfica intermediária.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarMunicipiosDaRegiaoIntermediaria(
        3501
    )
    ```

---

## Regiões Imediatas

22. listarRegioesImediatas  
    Obtém a lista de todas as regiões geográficas imediatas brasileiras.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarRegioesImediatas()
    ```

23. listarRegiaoImediata  
    Obtém as informações de uma região geográfica imediata através do seu código identificador.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarRegiaoImediata(
        350001
    )
    ```

24. listarMunicipiosDaRegiaoImediata  
    Obtém a lista de municípios pertencentes a uma região geográfica imediata.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarMunicipiosDaRegiaoImediata(
        350001
    )
    ```

---

## Distritos

25. listarDistritos  
    Obtém a lista de todos os distritos brasileiros.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarDistritos()
    ```

26. listarDistrito  
    Obtém as informações de um distrito através do seu código identificador.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarDistrito(
        355030805
    )
    ```

---

## Subdistritos

27. listarSubdistritos  
    Obtém a lista de todos os subdistritos brasileiros.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarSubdistritos()
    ```

28. listarSubdistrito  
    Obtém as informações de um subdistrito através do seu código identificador.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarSubdistrito(
        35503080500
    )
    ```

---

## Países

29. listarPaises  
    Obtém a lista de países disponíveis na API de localidades do IBGE.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarPaises()
    ```

30. listarPais  
    Obtém as informações de um país através do seu código identificador.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.localidade.listarPais(
        76
    )
    ```