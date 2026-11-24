import random
import numpy as np


class Place:
    def __init__(self, place_id, host_id, city):
        self.place_id = place_id
        self.host_id = host_id
        self.city = city

    def setup(self):
        n = self.city.size
        row = self.place_id // n
        col = self.place_id % n

       
        self.neighbours = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if 0 <= r < n and 0 <= c < n:
                    self.neighbours.append(r * n + c)

       
        half = n // 2
        if row < half and col < half:
            self.area = 0
        elif row < half and col >= half:
            self.area = 1
        elif row >= half and col < half:
            self.area = 2
        else:
            self.area = 3

       
        low, high = self.city.area_rates[self.area]
        self.rate = random.uniform(low, high)

        
        self.price = {0: 900 * self.rate}

    def update_occupancy(self):
       
        area_rates = [p.rate for p in self.city.places if p.area == self.area]
        mean_rate = np.mean(area_rates)

       
        if self.rate > mean_rate:
            self.occupancy = random.randint(5, 15)
        else:
            self.occupancy = random.randint(10, 20)
