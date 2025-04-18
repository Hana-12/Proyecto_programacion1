
def validar_correo(correo):
    """
    Valida si un correo electrónico tiene el formato básico correcto.

    La función verifica que:
        - El correo contenga exactamente un '@'.
        - El nombre de usuario (antes del '@') no esté vacío.
        - El dominio (después del '@') contenga al menos un punto '.'.
        - El dominio no empiece ni termine con un punto.

    Args:
        correo (str): Correo electrónico a validar.

    Returns:
        bool: True si el correo tiene un formato válido, False en caso contrario.
    """
    if '@' not in correo or correo.count('@') != 1:
        return False
    usuario, dominio = correo.split('@')
    return bool(usuario) and '.' in dominio and not dominio.startswith('.') and not dominio.endswith('.')

def validar_telefono(telefono):
    """
    Valida si un número de teléfono es válido.

    Verifica que el número:
        - Contenga únicamente dígitos.
        - Tenga exactamente 10 caracteres de longitud.

    Args:
        telefono (str): Número de teléfono a validar.

    Returns:
        bool: True si el número es válido, False en caso contrario.
    """
    return telefono.isdigit() and len(telefono) == 10

