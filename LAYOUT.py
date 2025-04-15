import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy.optimize import dual_annealing

# Parâmetros do layout da fábrica
factory_length = 50  # metros
factory_width = 30   # metros
minimum_distance = 2  # metros

# Definição inicial das máquinas
machines = {
    "Machine 1": (5, 5, 10, 3),
    "Machine 2": (20, 5, 10, 3),
    "Machine 3": (35, 5, 10, 3),
    "Machine 4": (5, 15, 10, 3)
}

# Parâmetros operacionais
process_time_per_machine = 5  # minutos
time_per_meter = 1  # minutos por metro

# Função para visualizar o layout com tempos no canto superior esquerdo
def plot_layout(machines, factory_length, factory_width, title="Factory Layout", show_time=None, save_file=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    previous_position = None

    for i, (machine, (x, y, w, h)) in enumerate(machines.items()):
        rect = patches.Rectangle((x, y), w, h, edgecolor='blue', facecolor='lightblue', lw=2)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, machine, ha='center', va='center', fontsize=10, color='black')

        if previous_position is not None:
            start_x = previous_position[0] + previous_position[2]
            start_y = previous_position[1] + previous_position[3]/2
            end_x = x
            end_y = y + h/2

            distance = np.sqrt((end_x - start_x)**2 + (end_y - start_y)**2)

            ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                        arrowprops=dict(facecolor='red', edgecolor='red', arrowstyle="->", lw=2))

            mid_x = (start_x + end_x) / 2
            mid_y = (start_y + end_y) / 2
            offset_x = (end_y - start_y) / distance * 0.5
            offset_y = (start_x - end_x) / distance * 0.5
            ax.text(mid_x + offset_x, mid_y + offset_y, f'{distance:.1f} m', fontsize=8, color='red', ha='center', va='center')

        previous_position = (x, y, w, h)

    ax.set_xlim(0, factory_length)
    ax.set_ylim(0, factory_width)
    ax.set_xticks(np.arange(0, factory_length + 1, 5))
    ax.set_yticks(np.arange(0, factory_width + 1, 5))
    ax.grid(True)

    ax.set_title(title)
    ax.set_xlabel('Length (m)')
    ax.set_ylabel('Width (m)')

    # Tempo no canto superior esquerdo
    if show_time is not None:
        ax.text(1, factory_width - 1, f"Tempo total: {show_time:.2f} min",
                ha='left', va='top', fontsize=12, color='black', fontweight='bold')

    plt.tight_layout()

    # Salvar o gráfico, se o caminho de arquivo for fornecido
    if save_file is not None:
        plt.savefig(save_file, dpi=300, bbox_inches='tight')

    plt.show()

# Calcula a distância total entre máquinas
def total_distance(machines):
    positions = []
    for machine in machines:
        x, y, w, h = machines[machine]
        positions.append((x + w, y + h / 2))
    return sum(np.sqrt((positions[i+1][0] - positions[i][0])**2 + (positions[i+1][1] - positions[i][1])**2)
               for i in range(len(positions) - 1))

# Calcula o tempo total
def calculate_total_time(machines):
    positions = [(x + w, y + h / 2) for x, y, w, h in machines.values()]
    total_time = process_time_per_machine * len(machines)
    total_time += sum(np.sqrt((positions[i+1][0] - positions[i][0])**2 + (positions[i+1][1] - positions[i][1])**2)
                      * time_per_meter for i in range(len(positions) - 1))
    return total_time

# Função de custo para o otimizador
def cost_function(updated_positions):
    total_dist = total_distance(updated_positions)
    overlap_penalty = 0
    machine_list = list(updated_positions.values())

    for i in range(len(machine_list)):
        x1, y1, w1, h1 = machine_list[i]
        for j in range(i+1, len(machine_list)):
            x2, y2, w2, h2 = machine_list[j]
            dist_x = abs(x1 - x2)
            dist_y = abs(y1 - y2)
            overlap_x = (w1 + w2) / 2 + minimum_distance
            overlap_y = (h1 + h2) / 2 + minimum_distance
            if dist_x < overlap_x and dist_y < overlap_y:
                overlap_penalty += (overlap_x - dist_x) * (overlap_y - dist_y)

    boundary_penalty = sum(
        1e4 for x, y, w, h in machine_list if x < 0 or y < 0 or x + w > factory_length or y + h > factory_width
    )

    return total_dist + overlap_penalty + boundary_penalty

# Custo adaptado para otimização
def optimization_cost(positions):
    updated_positions = {
        name: (positions[i*2], positions[i*2 + 1], machines[name][2], machines[name][3])
        for i, name in enumerate(machines)
    }
    return cost_function(updated_positions)

# Definir bounds para a otimização
bounds = []
for name in machines:
    _, _, w, h = machines[name]
    bounds.append((0, factory_length - w))  # x
    bounds.append((0, factory_width - h))   # y

# Tempo antes da otimização
initial_time = calculate_total_time(machines)
print(f"Tempo total antes da otimização: {initial_time:.2f} minutos")

# Otimização com simulated annealing
result = dual_annealing(optimization_cost, bounds)

# Aplicar as posições otimizadas
optimized_machines = {
    name: (result.x[i*2], result.x[i*2 + 1], machines[name][2], machines[name][3])
    for i, name in enumerate(machines)
}

# Tempo depois da otimização
optimized_time = calculate_total_time(optimized_machines)
print(f"Tempo total após otimização automática: {optimized_time:.2f} minutos")

# Visualizações com tempos individuais
plot_layout(machines, factory_length, factory_width, title="Initial Factory Layout",
            show_time=initial_time, save_file="layout-inicial.png")

plot_layout(optimized_machines, factory_length, factory_width, title="Optimized Factory Layout",
            show_time=optimized_time, save_file="layout-otimizado.png")