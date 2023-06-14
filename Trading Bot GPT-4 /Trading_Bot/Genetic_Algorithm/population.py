import random

class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0.0

def create_population(population_size, gene_pool, num_genes):
    population = []
    for i in range(population_size):
        genes = [random.choice(gene_pool) for j in range(num_genes)]
        chromosome = Chromosome(genes)
        population.append(chromosome)
    return population

def evaluate_population(population, fitness_fn):
    for chromosome in population:
        chromosome.fitness = fitness_fn(chromosome.genes)

def roulette_wheel_selection(population):
    fitnesses = [chromosome.fitness for chromosome in population]
    total_fitness = sum(fitnesses)
    rand_val = random.uniform(0, total_fitness)
    running_sum = 0
    for i in range(len(population)):
        running_sum += fitnesses[i]
        if running_sum > rand_val:
            return population[i]

def single_point_crossover(a, b):
    crossover_point = random.randint(1, len(a.genes) - 1)
    new_a = a.genes[:crossover_point] + b.genes[crossover_point:]
    new_b = b.genes[:crossover_point] + a.genes[crossover_point:]
    return (Chromosome(new_a), Chromosome(new_b))

def mutation(chromosome, gene_pool, pmut):
    new_genes = []
    for gene in chromosome.genes:
        if random.uniform(0, 1) < pmut:
            gene = random.choice(gene_pool)
        new_genes.append(gene)
    return Chromosome(new_genes)

def genetic_algorithm(gene_pool, fitness_fn, pop_size=100, num_generations=100, crossover_rate=0.8, mutation_rate=0.01):
    num_genes = len(gene_pool[0])
    population = create_population(pop_size, gene_pool, num_genes)
    for i in range(num_generations):
        evaluate_population(population, fitness_fn)
        new_population = []
        while len(new_population) < pop_size:
            parent1 = roulette_wheel_selection(population)
            if random.uniform(0, 1) < crossover_rate:
                parent2 = roulette_wheel_selection(population)
                child1, child2 = single_point_crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent1
            new_population.append(mutation(child1, gene_pool, mutation_rate))
            new_population.append(mutation(child2, gene_pool, mutation_rate))
        population = new_population
    evaluate_population(population, fitness_fn)
    population.sort(key=lambda x: x.fitness, reverse=True)
    return population[0]
