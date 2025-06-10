from classes.SisGE import SisGE


def limite(quantidade,max):
    if quantidade < max:
         return f"{quantidade} de {max}"
    else:
         return f"Atingiu um limite máximo: {quantidade} de {max}*"