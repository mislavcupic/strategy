# Strategija za obračun cijene
class PriceStrategy:
    # Apstraktna metoda za izračunavanje cijene
    def calculate_price(self, base_price):
        pass

# Strategija bez popusta
class NoDiscount(PriceStrategy):
    def calculate_price(self, base_price):
        return base_price

# Strategija s postotnim popustom
class PercentageDiscount(PriceStrategy):
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def calculate_price(self, base_price):
        # Oduzimanje postotka popusta od osnovne cijene
        return base_price * (1 - self.discount_percentage / 100)

# Strategija s fiksnim popustom
class FixedDiscount(PriceStrategy):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def calculate_price(self, base_price):
        # Oduzimanje fiksnog iznosa popusta, ali cijena ne smije pasti ispod nule
        return max(0, base_price - self.discount_amount)

# Klasa Product (Proizvod)
class Product:
    def __init__(self, name, base_price, price_strategy: PriceStrategy):
        self.name = name  # Naziv proizvoda
        self.base_price = base_price  # Osnovna cijena proizvoda
        self.price_strategy = price_strategy  # Strategija za obračun cijene

    def calculate_price(self):
        # Koristi strategiju za izračun konačne cijene
        return self.price_strategy.calculate_price(self.base_price)

    def __str__(self):
        # Vraća osnovne informacije o proizvodu i konačnoj cijeni
        return f"Proizvod: {self.name}, Osnovna cijena: {self.base_price}, Konačna cijena: {self.calculate_price()}"

if __name__ == "__main__":
    # Kreiramo proizvode s različitim strategijama cijene
    product1 = Product("Laptop", 1000, NoDiscount())  # Bez popusta
    product2 = Product("Mobitel", 800, PercentageDiscount(10))  # 10% popusta
    product3 = Product("Slušalice", 150, FixedDiscount(20))  # Fiksni popust od 20

    # Ispisujemo rezultate za svaki proizvod
    print(product1)  # Output: Proizvod: Laptop, Osnovna cijena: 1000, Konačna cijena: 1000
    print(product2)  # Output: Proizvod: Mobitel, Osnovna cijena: 800, Konačna cijena: 720
    print(product3)  # Output: Proizvod: Slušalice, Osnovna cijena: 150, Konačna cijena: 130

    # Mijenjamo strategiju za slušalice
    product3.price_strategy = PercentageDiscount(30)  # 30% popusta
    print(product3)  # Output: Proizvod: Slušalice, Osnovna cijena: 150, Konačna cijena: 105
