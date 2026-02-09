import random

# Fitness function
def f(x):
    return -(x - 3)**2 + 9   # Peak at x=3, value=9

# Tabu Search Algorithm
def tabu_search(start, steps=50, tabu_size=5):
    current = start
    best = current
    tabu_list = []
    
    for _ in range(steps):
        # Generate neighbors
        neighbors = [current + random.uniform(-1, 1) for _ in range(10)]
        
        # Filter out tabu neighbors
        neighbors = [n for n in neighbors if round(n,2) not in tabu_list]
        
        # Pick best neighbor
        if neighbors:
            next_move = max(neighbors, key=f)
            
            # Update tabu list
            tabu_list.append(round(next_move,2))
            if len(tabu_list) > tabu_size:
                tabu_list.pop(0)
            
            # Move
            current = next_move
            if f(current) > f(best):
                best = current
    
    return best, f(best)

# Run Tabu Search
best_x, best_value = tabu_search(start=random.uniform(-10, 10))
print("Best x found:", best_x)
print("Best value:", best_value)
