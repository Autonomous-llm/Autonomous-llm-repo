# Contains fitness functions for the genetic algorithm
import numpy as np
from typing import List

def fitness_function(data: List[float], population: np.ndarray) -> np.ndarray:
    fitness_scores = np.zeros(population.shape[0])
    for i in range(population.shape[0]):
        # calculate fitness score for each solution in the population
        solution = population[i]
        # TODO: Implement fitness score calculation based on the requirements of the project
        # and the data passed in
        fitness_scores[i] = 0.0  # placeholder value for now
    return fitness_scores
