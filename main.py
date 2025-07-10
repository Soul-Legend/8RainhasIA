import pygad
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

N = 8

def fitness_func(ga_instance, solution, solution_idx):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if solution[i] == solution[j] or abs(solution[i] - solution[j]) == abs(i - j):
                conflicts += 1
    return 28 - conflicts

gene_space = list(range(N))

ga_instance = pygad.GA(
    num_generations=200,
    num_parents_mating=20,
    fitness_func=fitness_func,
    sol_per_pop=100,
    num_genes=N,
    gene_space=gene_space,
    parent_selection_type="tournament",
    crossover_type="single_point",
    mutation_type="random",
    mutation_num_genes=1,
    stop_criteria=["reach_28"]
)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
solution = list(map(int, solution))

print("Melhor solução encontrada:", solution)
print("Fitness da melhor solução:", solution_fitness)

def print_board(solution):
    board = [["." for _ in range(N)] for _ in range(N)]
    for col, row in enumerate(solution):
        board[row][col] = "Q"
    for row in board:
        print(" ".join(row))

print("\nTabuleiro resultante:")
print_board(solution)

# Plot do fitness
fitness_values = ga_instance.best_solutions_fitness
plt.figure(figsize=(10, 5))
plt.plot(fitness_values, marker='o')
plt.title("Evolução do Fitness ao Longo das Gerações")
plt.xlabel("Geração")
plt.ylabel("Fitness da Melhor Solução")
plt.grid(True)
plt.tight_layout()
plt.savefig("fitness_plot.png")
print("Gráfico salvo como 'fitness_plot.png'")
plt.show()
