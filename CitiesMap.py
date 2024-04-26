import random
import math
from matplotlib.collections import PathCollection
import matplotlib.pyplot as plt


class CitiesMap:
    """Euclidean map of random city locations."""

    def __init__(self, *, seed: int, num_cities: int, map_size: (int, int)):
        self.seed = seed
        self.num_cities = num_cities
        self.map_size = map_size

        random.seed(self.seed)
        self.cities = [(random.random() * map_size[0], random.random() * map_size[1]) for i in range(num_cities)]

    def __str__(self) -> str:
        return ''.join([f'{city}' for city in self.cities])

    def __getitem__(self, index) -> (float, float):
        return self.cities[index]

    def __len__(self) -> int:
        return len(self.cities)

    def inter_dist(self, a: int, b: int) -> float:
        """Inter-distance between two cities by index."""
        return math.sqrt((self.cities[a][0] - self.cities[b][0]) ** 2
                         + (self.cities[a][1] - self.cities[b][1]) ** 2)

    def plot(self) -> PathCollection:
        """Return plot of cities"""
        plt.scatter([x for x, y in self.cities], [y for x, y in self.cities])
        plt.xlim([0, self.map_size[0]])
        plt.ylim([0, self.map_size[1]])
        return plt