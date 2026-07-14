############ Função Calcular ############
def Calcular(expressão):
    try:
        return eval(expressão)
    except:
        return "Error"
    