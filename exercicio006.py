def valorPagamento(vl, dias):
    if dias != 0:
        vl += vl*0.03
        vl += vl*(0.001*dias)
        print(vl)
    return vl

pagto = float(input('Valor do pagamento: '))
diasAtraso = int(input('Dias de atraso: '))
valorPagamento(pagto, diasAtraso)