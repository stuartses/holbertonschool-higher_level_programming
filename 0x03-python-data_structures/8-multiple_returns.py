#!/usr/bin/python3
def multiple_returns(sentence):
    len_sente = len(sentence)
    first_sente = ""

    if len_sente == 0:
        first_sente = "None"
    else:
        first_sente = sentence[0]

    tupla_sente = (len_sente, first_sente)

    return tupla_sente
