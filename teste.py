from sonne import Sonne
sonne = Sonne()

dados = sonne.ibge.hgeohnor.coordenadasDoPontoEmGrauDecimal(
    lat='-20',
    lon='-50',
)

dados = sonne.ibge.hgeohnor.coordenadasDoPontoEmGrauSexagecimal(
    glat='-20',
    mlat='25',
    slat='30.000',
    glon='-51',
    mlon='20',
    slon='30.000'
)

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

from pprint import pprint
pprint(dados)