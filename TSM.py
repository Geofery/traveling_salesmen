import random
from matplotlib.collections import PathCollection
import CitiesMap


def loop(lst) -> []:
    """Return a looped list of paths to travel."""
    loop_lst = []
    for i, j in zip(lst, lst[1:]):
        loop_lst.append((i, j))
    loop_lst.append((lst[-1], lst[0]))
    return loop_lst


class TSM:
    """Taveling Salesman Agent."""

    def __init__(self, cities_map: CitiesMap):
        self.map = cities_map
        self.DNA = [i for i in range(self.map.num_cities)]
        random.shuffle(self.DNA)

    def dist(self) -> float:
        """Return total distance traveled."""
        return sum([self.map.inter_dist(i, j) for i, j in loop(self.DNA)])

    def plot(self) -> PathCollection:
        """Return plot of path traveled."""
        p = self.map.plot()
        for i, j in loop(self.DNA):
            ax, ay = self.map[i]
            bx, by = self.map[j]
            p.plot([ax, bx], [ay, by])
        return p

    def mutate(self, mutation_rate=0.02) -> None:
        if random.random() <= mutation_rate:
            samples = random.sample(range(len(self.map)), 2)
            self.DNA[samples[0]], self.DNA[samples[1]] = self.DNA[samples[1]], self.DNA[samples[0]]

    def cross_breed(self, other) -> 'TSM':
        start, end = sorted(random.sample(range(len(self.DNA)), 2))
        child_DNA = [None] * len(self.DNA)
        child_DNA[start:end] = self.DNA[start:end]

        added_cities = set(child_DNA[start:end])

        remaining_indices = [i for i in other.DNA if i not in added_cities]
        remaining_indices_idx = 0
        for i in range(len(child_DNA)):
            if child_DNA[i] is None:
                child_DNA[i] = remaining_indices[remaining_indices_idx]
                added_cities.add(remaining_indices[remaining_indices_idx])
                remaining_indices_idx += 1

        offspring = TSM(self.map)
        offspring.DNA = child_DNA
        offspring.mutate()

        return offspring
