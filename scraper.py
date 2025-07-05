# scraper.py
import pandas as pd
from datetime import datetime, timedelta
import random

def generate_mock_data():
    cities = ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide']
    data = []
    for _ in range(100):
        origin = random.choice(cities)
        destination = random.choice([c for c in cities if c != origin])
        price = random.randint(100, 500)
        date = datetime.today() + timedelta(days=random.randint(1, 30))
        data.append([origin, destination, price, date.strftime('%Y-%m-%d')])
    df = pd.DataFrame(data, columns=['Origin', 'Destination', 'Price', 'Date'])
    return df
