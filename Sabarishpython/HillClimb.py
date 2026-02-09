import random
# Function to maximize
def f(x):
    return -(x - 3)**2 + 9   # Peak at x=3, value=9

# Hill Climbing Algorithm
def hill_climb(start, steps=100, step_size=0.1):
    current = start
    for _ in range(steps):
        # Generate a neighbor (slightly move left or right)
        neighbor = current + random.choice([-step_size, step_size])
        
        # If neighbor is better, move there
        if f(neighbor) > f(current):
            current = neighbor
    return current, f(current)
# Run the algorithm
best_x, best_value = hill_climb(start=random.uniform(-10, 10))
print("Best x found:", best_x)
print("Best value:", best_value)
