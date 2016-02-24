class Cobrador():
    def cobrar(orden, metodo):
        if metodo.validar(orden):
            metodo.cobrar(orden.gran_total)


class Metodo():
    def cobrar(total):
        pass

    def validar(total):
        pass


class Paypal(Metodo):
    pass


class Stripe(Metodo):
    pass
