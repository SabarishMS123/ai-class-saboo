import random
# Fitness function
def f(x):
    return -(x - 3)**2 + 9   # Peak at x=3, value=9

# Create initial population
def create_population(size=10):
    return [random.uniform(-10, 10) for _ in range(size)]

# Selection: pick best individuals
def selection(population):
    return sorted(population, key=f, reverse=True)[:len(population)//2]
# Crossover: combine two parents
def crossover(parent1, parent2):
    return (parent1 + parent2) / 2
# Mutation: small random change
def mutate(x, rate=0.1):
    return x + random.uniform(-rate, rate)
# Genetic Algorithm
def genetic_algorithm(generations=50, pop_size=10):
    population = create_population(pop_size)
    for _ in range(generations):
        # Selection
        selected = selection(population)
        # Crossover + Mutation to create new population
        children = []
        while len(children) < pop_size:
            p1, p2 = random.sample(selected, 2)
            child = crossover(p1, p2)
            child = mutate(child)
            children.append(child)
        
        population = children
    # Best solution
    best = max(population, key=f)
    return best, f(best)
# Run GA
best_x, best_value = genetic_algorithm()
print("Best x found:", best_x)
print("Best value:", best_value)
