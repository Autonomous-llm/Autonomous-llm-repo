import unittest
from population import Chromosome, create_population, evaluate_population, select_parents, single_point_crossover, mutate, evolve_population
from strategies.moving_average import moving_average_strategy

class TestPopulation(unittest.TestCase):
   
    def test_create_population(self):
        population = create_population(10)
        self.assertEqual(len(population), 10)

    def test_evaluate_population(self):
        historical_data = []  # Provide historical data for testing
        population = create_population(10)
        evaluate_population(population, historical_data, moving_average_strategy)

        for individual in population:
            self.assertNotEqual(individual.fitness, -1)

    def test_select_parents(self):
        historical_data = []  # Provide historical data for testing
        population = create_population(10)
        evaluate_population(population, historical_data, moving_average_strategy)
        parents = select_parents(population)

        for parent in parents:
            self.assertTrue(parent in population)

    def test_crossover(self):
        parent1 = Chromosome({'TEMA': {}, 'DEMA': {}})
        parent2 = Chromosome({'TEMA': {}, 'Supertrend': {}})
        child = crossover(parent1, parent2)

        self.assertTrue(child.genes['TEMA'] in [parent1.genes['TEMA'], parent2.genes['TEMA']])
        self.assertTrue(child.genes['DEMA'] in [parent1.genes['DEMA'], parent2.genes['DEMA']])
        self.assertTrue(child.genes['Supertrend'] in [parent1.genes.get('Supertrend'), parent2.genes['Supertrend']])

    def test_mutate(self):
        individual = Chromosome({'TEMA': {}, 'DEMA': {}})
        mutated_individual = mutate(individual)

        self.assertNotEqual(mutated_individual.genes, individual.genes)

    def test_evolve_population(self):
        historical_data = []  # Provide historical data for testing
        population = create_population(10)
        new_population = evolve_population(population, historical_data, moving_average_strategy)

        self.assertEqual(len(new_population), len(population))


if __name__ == '__main__':
    unittest.main()
