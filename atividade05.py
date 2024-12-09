def perpetuidade(fluxo_ano, taxa_juros):

    vp = fluxo_ano / taxa_juros
    return vp

fluxo_ano = 200000 
taxa_juros = 0.10

valor_presente = perpetuidade(fluxo_ano, taxa_juros)

print(f"O valor presente necessário para criar o fundo de bolsa é: ${valor_presente:,.2f}")
