from product import Product

paleta = Product(10)

dict_of_attributes = {
    "color": "Red",
    "flavor": "Pinapple",
    "manufacturer": "Mini Paletita"
}

for attr, value in dict_of_attributes:
    setattr(paleta, attr, value)

# Ahora puedes consultar todos los atributos como propios del objeto
# paleta.color
# paleta.flavor
# paleta.manufacturer
