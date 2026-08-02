## IBGE
### Malhas Geográficas

[Documentação oficial](https://servicodados.ibge.gov.br/api/docs/malhas?versao=4)

#### Métodos

Lista de métodos implementados para esta classe

1. malhasPorUF  
   Obtém a malha referente a uma determinada Unidade da Federação (estado) do Brasil a partir do respectivo identificador. No caso das Unidades da Federação do Brasil, é possível usar a respectiva sigla em vez do identificador  
    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.MalhasGeograficas.malhasPorUF(
        'MG',
        intrarregiao='Municipio'
    )
    ```

2. malhasPorMunicipio  
    Obtém a malha referente a um determinado município do Brasil a partir do respectivo identificador.  

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.MalhasGeograficas.malhasPorMunicipio(
        '3304557',
        qualidade='minima'
    )
    ```

3. malhasPorPais  
    Obtém a malha referente a um determinado país. Na presente versão, só está disponível o Brasil, cujo identificador é BR. À medida que as malhas dos demais países forem disponibilizadas, informaremos através das notas de liberação  
    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.MalhasGeograficas.malhasPorPais(
        'BR',
        intrarregiao='Municipio'
    )
    ```

4. malhasPorRegiao  
    Obtém a malha referente a uma determinada região do Brasil a partir do respectivo identificador. No caso das regiões do Brasil, é possível usar a respectiva sigla (N, NE, SE, S, CO) em vez do identificador

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.MalhasGeograficas.malhasPorRegiao(
        '2',
        intrarregiao='Municipio'
    )
    ```

5. malhasPorRegiaoImediata  
    Obtém a malha referente a uma determinada região imediata do Brasil a partir do respectivo identificador.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.MalhasGeograficas.malhasPorRegiaoImediata(
        '110001',
        qualidade='intermediaria'
    )
    ```

6. malhasPorRegiaoIntermediaria  
    Obtém a malha referente a uma determinada região intermediária do Brasil a partir do respectivo identificador.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.MalhasGeograficas.malhasPorRegiaoIntermediaria(
        '1101',
        qualidade='minima'
    )
    ```

---

### Metadados

7. metadadosDaMalhaPorUF  
    Obtém os metadados da malha referente a uma determinada Unidade da Federação (estado) do Brasil a partir do respectivo identificador. No caso das Unidades da Federação do Brasil, é possível usar a respectiva sigla em vez do identificador

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.MalhasGeograficas.metadadosDaMalhaPorUF(
        'MG'
    )
    ```

8. metadadosDaMalhaPorMunicipio  
    Obtém os metadados da malha referente a um determinado município do Brasil a partir do respectivo identificador.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.MalhasGeograficas.metadadosDaMalhaPorMunicipio(
        '3304557'
    )
    ```

9. metadadosDaMalhaPorPais  
    Obtém os metadados da malha referente a um determinado país. Na presente versão, só está disponível o Brasil, cujo identificador é BR. À medida que as malhas dos demais países forem disponibilizadas, informaremos através das notas de liberação

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.MalhasGeograficas.metadadosDaMalhaPorPais(
        'BR'
    )
    ```

10. metadadosDaMalhaPorRegiao  
    Obtém os metadados da malha referente a uma determinada região do Brasil a partir do respectivo identificador. No caso das regiões do Brasil, é possível usar a respectiva sigla (N, NE, SE, S, CO) em vez do identificador

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.MalhasGeograficas.metadadosDaMalhaPorRegiao(
        '2'
    )
    ```

11. metadadosDaMalhaPorRegiaoImediata  
    Obtém os metadados da malha referente a uma determinada região imediata do Brasil a partir do respectivo identificador.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.MalhasGeograficas.metadadosDaMalhaPorRegiaoImediata(
        '110001'
    )
    ```

12. metadadosDaMalhaPorRegiaoIntermediaria  
    Obtém os metadados da malha referente a uma determinada região intermediária do Brasil a partir do respectivo identificador.

    ```python
    from sonne import Sonne
    sonne = Sonne()

    dados = sonne.ibge.MalhasGeograficas.metadadosDaMalhaPorRegiaoIntermediaria(
        '1101'
    )
    ```