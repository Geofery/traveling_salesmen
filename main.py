from icecream import ic
from CitiesMap import CitiesMap
from TSM import TSM
import random


def fitness(tsm):
    return tsm.dist()


def crossover(tsm1, tsm2):
    child = tsm1.cross_breed(tsm2)
    if child is None:
        return tsm1
    return child


def mutate(tsm, mutation_rate=0.02):
    tsm.mutate(mutation_rate)


def create_initial_population(num_individuals, cities_map):
    return [TSM(cities_map) for _ in range(num_individuals)]


def genetic_algorithm(num_generations, population_size, cities_map):
    population = create_initial_population(population_size, cities_map)
    generation_number = 0
    for generation in range(num_generations):
        fitness_scores = [fitness(tsm) for tsm in population]
        best_tsm_indices = sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i])[:population_size//2]
        best_parents = [population[i] for i in best_tsm_indices]
        generation_number += 1

        next_generation = []
        for _ in range(population_size):

            parent1, parent2 = random.sample(best_parents, 2)
            child = crossover(parent1, parent2)
            mutate(child)
            ic(generation_number, child.dist())
            next_generation.append(child)

        population = next_generation

    best_tsm = min(population, key=fitness)
    ic(best_tsm.dist())
    return best_tsm


def run():
    cm = CitiesMap(seed=42, num_cities=50, map_size=(25, 25))
    shortest_tsm = genetic_algorithm(num_generations=220, population_size=500, cities_map=cm)
    ic(shortest_tsm.dist())
    shortest_tsm.plot().show()


run()
