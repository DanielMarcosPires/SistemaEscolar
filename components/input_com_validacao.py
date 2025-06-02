import re


def input_com_validacao(prompt,regex, erro_message):
    data = input(prompt)
    if not re.match(regex,data):
        print(erro_message)
        return input_com_validacao(prompt,regex,erro_message)
    return data
