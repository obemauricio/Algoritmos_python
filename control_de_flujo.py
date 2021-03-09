def busca_pais(paises, pais):
    """
    Paises es un diccionario. Pais es la llave.
    Codigo con el permiso EAFP.
    """
    try:
        return paises[pais]
    except KeyError:
        return None

def run():
    paises = {
        'Mexico': 1,
        'Argentina': 2,
        'Bolivia': 3,
    }

    pais = input('Ingrese su pais: ')
    print(busca_pais(paises, pais))

if __name__ == '__main__':
    run()