
class Product:

    def __init__(self, price, tax_rate=0.16):
        self.tax_rate = tax_rate
        self.price = price

    @property
    def full_price(self):
        # (taza_impuests + 1) * precio
        return (self.tax_rate + 1) * self.price
