import random

# Given Knapsack Capacity
MAX_WEIGHT = 250

# Box Data: (Weight, Importance)
boxes = [
    (20, 6), (30, 5), (60, 8), (90, 7), (50, 6),
    (70, 9), (30, 4), (30, 5), (70, 4), (20, 9),
    (20, 2), (60, 1)
]

POP_SIZE = 100  # Population Size
GENERATIONS = 100  # Max Generations
MUTATION_RATE = 0.1  # Probability of mutation

# Generate a random individual (binary list)
def random_individual():
    return [random.choice([0, 1]) for _ in range(len(boxes))]

# Maximize importance while staying within weight limit
def fitness(individual):
    total_weight = sum(ind * boxes[i][0] for i, ind in enumerate(individual))
    total_value = sum(ind * boxes[i][1] for i, ind in enumerate(individual))
    
    if total_weight > MAX_WEIGHT:
        return -1  # Small penalty for exceeding weight 
    
    return total_value

# Selects the most fit individual
def select(population):
    sample = random.sample(population, k=5)
    return max(sample, key=fitness)

# Uniform Crossover provides better diversity than single point
def crossover(parent1, parent2):
    return [
        [parent1[i] if random.random() > 0.5 else parent2[i] for i in range(len(boxes))],
        [parent2[i] if random.random() > 0.5 else parent1[i] for i in range(len(boxes))]
    ]

# Adaptive Mutation decreases mutation rate over time
def mutate(individual, generation):
    mutation_chance = MUTATION_RATE * (1 - generation / GENERATIONS)  # Applies adaptive rate
    for i in range(len(individual)):
        if random.random() < mutation_chance:
            individual[i] = 1 - individual[i]

# Genetic Algorithm
def genetic_algorithm():
    population = [random_individual() for _ in range(POP_SIZE)]
    
    for gen in range(GENERATIONS):
        population = sorted(population, key=fitness, reverse=True)
        new_population = population[:POP_SIZE // 2]  # Keep top 50%
        
        while len(new_population) < POP_SIZE:
            p1, p2 = select(population), select(population)
            child1, child2 = crossover(p1, p2)
            mutate(child1, gen)
            mutate(child2, gen)
            new_population += [child1, child2]
        
        population = new_population

    best_solution = max(population, key=fitness)
    best_weight = sum(best_solution[i] * boxes[i][0] for i in range(len(boxes)))
    best_importance = fitness(best_solution)

    return best_solution, best_weight, best_importance

# Run GA
solution, total_weight, total_importance = genetic_algorithm()
# i + 1: box number, boxes[i][0]: box weight, boxes[i][1]: box value/importance
selected_boxes = [(i + 1, boxes[i][0], boxes[i][1]) for i, bit in enumerate(solution) if bit == 1]

# Output
print("\n=== Genetic Algorithm Results ===")
print(f"Total Generations: {GENERATIONS}")
print(f"Selected Boxes (Index, Weight, Importance):")
for box in selected_boxes:
    print(f"  Box {box[0]}: Weight={box[1]}, Importance={box[2]}")
print(f"\nTotal Weight: {total_weight} / {MAX_WEIGHT}")
print(f"Total Importance: {total_importance}")
print("=================================\n")
