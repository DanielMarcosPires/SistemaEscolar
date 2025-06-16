from classes.SisGE import SisGE


def limite(quantidade,max):
    if quantidade < max:
     return f"{quantidade} de {max}"
    elif quantidade >= 0:
     return f"O valor não deve ser negativo!"
    else:
     return f"Atingiu um limite máximo: {quantidade} de {max}*"