## IBGE
### Agregados

[Documentação oficial](https://servicodados.ibge.gov.br/api/docs/agregados?versao=3#api-_)

#### Métodos

Lista de métodos implementados para esta classe

1. Listar  
    Lista todos conjuntos de agregados

        from sonne import Sonne
        sonne = Sonne()
        dados = sonne.ibge.agregados.listar()

2. Metadados  
    Obtém os metadados associados ao agregado  
    
        from sonne import Sonne
        sonne = Sonne()
        dados = sonne.ibge.agregados.metadados(35)

3. Periodos  
     Obtém os períodos associados ao agregado  

        from sonne import Sonne
        sonne = Sonne()
        dados = sonne.ibge.agregados.periodos(35)

4. Variaveis  
    Função de consulta com filtros na API

        from sonne import Sonne
        sonne = Sonne()
        
        dados = sonne.ibge.agregados.variaveis(
            1712,
            localidades="BR",
            periodos="-12",
            classificacao="226[4844,96608,96609]|218[4780]",
            view = "flat"
        )