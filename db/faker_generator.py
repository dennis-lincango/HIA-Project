import random
import pandas as pd
from faker import Faker

fake = Faker()


# Función para generar datos aleatorios
def generate_electronic_data(n):
    categories = ['laptop', 'tablet', 'smartphone', 'televisor', 'smartwatch']
    brands = ['Samsung', 'Apple', 'Sony', 'LG', 'Lenovo', 'HP']
    availability = ['in stock', 'out of stock', 'limited']
    data = []

    for i in range(n):
        amount_min = round(random.uniform(100, 800), 2)
        amount_max = round(amount_min + random.uniform(50, 500), 2)

        data.append({
            "id": i + 1,
            "prices.amountMax": amount_max,
            "prices.amountMin": amount_min,
            "prices.availability": random.choice(availability),
            "prices.isSale": random.choice([True, False]),
            "prices.merchant": fake.company(),
            "prices.shipping": f"{random.randint(0, 30)} USD",
            "brand": random.choice(brands),
            "categories": random.choice(categories),
            "name": fake.catch_phrase(),
            "weight": f"{round(random.uniform(0.5, 5.0), 2)} kg"
        })

    return pd.DataFrame(data)
