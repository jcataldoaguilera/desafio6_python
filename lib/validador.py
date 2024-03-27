
def validate(opciones, eleccion):
    # Definir validación de eleccion
    ##########################################################################
    """_summary_

    Args:
        opciones (_list_): _Lista de opciones a validar_
        eleccion (_str_): _Eleccion de opciones_

    Returns:
        _type_: _description_
    """
    ##########################################################################
    if eleccion in opciones :
        return eleccion
    else:
        print('Opción no válida, ingrese una de las opciones válidas:')


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
