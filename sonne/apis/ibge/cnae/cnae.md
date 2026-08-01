## IBGE
### CNAE

[Documentação oficial](https://servicodados.ibge.gov.br/api/docs/cnae?versao=2)

#### Métodos

Lista de métodos implementados para esta classe

1. listaClasses  
    Obtém o conjunto de classes

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.listaClasses()
    ```

2. classePorIdentificador  
    Obtém o conjunto de classes a partir dos respectivos identificadores  

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.classePorIdentificador(
        '01113|01121'
    )
    ```

3. classesPorDivisao  
    Obtém o conjunto de classes a partir dos identificadores das divisões

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.classesPorDivisao(
        '1|2'
    )
    ```
   
4. classesPorGrupo  
    Obtém o conjunto de classes a partir dos identificadores dos grupos

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.classesPorGrupo(
        '11|12'
    )
    ```

5. classesPorSecao  
    Obtém o conjunto de classes a partir dos identificadores das seções.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.classesPorSecao(
        'B|C'
    )
    ```

6. listaDivisoes  
    Obtém o conjunto de divisões.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.listaDivisoes()
    ```

7. divisaoPorIdentificador  
    Obtém o conjunto de divisões a partir dos respectivos identificadores.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.divisaoPorIdentificador(
        '05|06'
    )
    ```

8. divisoesPorSecao  
    Obtém o conjunto de divisões a partir dos identificadores das seções.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.divisoesPorSecao(
        'B|C'
    )
    ```

9. listaGrupos  
    Obtém o conjunto de grupos.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.listaGrupos()
    ```

10. gruposPorDivisao  
    Obtém o conjunto de grupos a partir dos identificadores das divisões.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.gruposPorDivisao(
        '2|3'
    )
    ```

11. grupoPorIdentificador  
    Obtém o conjunto de grupos a partir dos respectivos identificadores.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.grupoPorIdentificador(
        '21|22'
    )
    ```

12. gruposPorSecao  
    Obtém o conjunto de grupos a partir dos identificadores das seções.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.gruposPorSecao(
        'B|A'
    )
    ```

13. listaSecoes  
    Obtém o conjunto de seções.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.listaSecoes()
    ```

14. secaoPorIdentificador  
    Obtém o conjunto de seções a partir dos respectivos identificadores.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.secaoPorIdentificador(
        'B|C'
    )
    ```

15. listaSubclasses  
    Obtém o conjunto de subclasses.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.listaSubclasses()
    ```

16. subclassePorIdentificador  
    Obtém o conjunto de subclasses a partir dos respectivos identificadores.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.subclassePorIdentificador(
        '0500301'
    )
    ```

17. subclassesPorClasse  
    Obtém o conjunto de subclasses a partir dos identificadores das classes.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.subclassesPorClasse(
        '02101|02209'
    )
    ```

18. subclassesPorDivisao  
    Obtém o conjunto de subclasses a partir dos identificadores das divisões.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.subclassesPorDivisao(
        '1|2'
    )
    ```

19. subclassesPorGrupo  
    Obtém o conjunto de subclasses a partir dos identificadores dos grupos.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.subclassesPorGrupo(
        '21|22'
    )
    ```

20. subclassesPorSecao  
    Obtém o conjunto de subclasses a partir dos identificadores das seções.

    ```python
    from sonne import Sonne
    sonne = Sonne()
    dados = sonne.ibge.cnae.subclassesPorSecao(
        'E|R'
    )
    ```