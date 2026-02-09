import math, random

# Function to maximize
def f(x):
    return -(x - 3)**2 + 9   # Peak at x=3, value=9

# Simulated Annealing Algorithm
def simulated_annealing(start, steps=1000, temp=10, cooling=0.99):
    current = start
    current_value = f(current)
    
    for _ in range(steps):
        # Generate a neighbor
        neighbor = current + random.uniform(-1, 1)
        neighbor_value = f(neighbor)
        
        # Decide whether to move
        if neighbor_value > current_value:
            current, current_value = neighbor, neighbor_value
        else:
            # Accept worse move with some probability
            prob = math.exp((neighbor_value - current_value) / temp)
            if random.random() < prob:
                current, current_value = neighbor, neighbor_value
        
        # Cool down temperature
        temp *= cooling
    
    return current, current_value

# Run the algorithm
best_x, best_value = simulated_annealing(start=random.uniform(-10, 10))
print("Best x found:", best_x)
print("Best value:", best_value)
