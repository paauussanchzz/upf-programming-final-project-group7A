import random
import numpy as np
import matplotlib.pyplot as plt
from final_project.city import City


def run_simulation(seed=42):
    random.seed(seed)
    np.random.seed(seed)

    area_rates = {
        0: (100, 200),
        1: (50, 250),
        2: (250, 350),
        3: (150, 450),
    }

    city = City(size=10, area_rates=area_rates)
    city.initialize()

    active_hosts_history = []

    for _ in range(180):
        city.iterate()
        active_hosts = sum(1 for h in city.hosts if len(h.assets) > 0)
        active_hosts_history.append(active_hosts)

    return city, active_hosts_history


def plot_graph1(city, filename="reports/graph1.png"):
    host_data = []
    for host in city.hosts:
        assets_value = 0
        for pid in host.assets:
            place = city.places[pid]
            latest_step = max(place.price.keys())
            assets_value += place.price[latest_step]

        total_wealth = host.profits + assets_value
        host_data.append((total_wealth, host.area))

    host_data.sort(key=lambda x: x[0])

    wealths = [x[0] for x in host_data]
    areas = [x[1] for x in host_data]

    area_colors = {0: "#1f77b4", 1: "#ff7f0e", 2: "#2ca02c", 3: "#d62728"}
    area_labels = {
        0: "Area 0 (Bottom-Left)",
        1: "Area 1 (Bottom-Right)",
        2: "Area 2 (Top-Left)",
        3: "Area 3 (Top-Right)",
    }
    colors = [area_colors[a] for a in areas]

    plt.figure(figsize=(12, 6))
    plt.bar(range(len(wealths)), wealths, color=colors)

    handles = [
        plt.Rectangle((0, 0), 1, 1, color=area_colors[a]) for a in sorted(area_colors)
    ]
    plt.legend(handles, [area_labels[a] for a in sorted(area_labels)], title="Origin Area")

    plt.title("Final Host Wealth after 15 Years (180 Months)")
    plt.xlabel("Hosts (Sorted from Lowest to Highest Wealth)")
    plt.ylabel("Total Wealth (Profits + Property Value)")
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()


def plot_graph2(active_hosts_history, filename="reports/graph2_v0.png"):
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, len(active_hosts_history) + 1), active_hosts_history, linewidth=2, color="#2ca02c")
    plt.title("Market Consolidation: Number of Active Hosts Over Time")
    plt.xlabel("Month (Step)")
    plt.ylabel("Hosts Owning at Least 1 Listing")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()


if __name__ == "__main__":
    city, active_hosts_history = run_simulation(seed=42)
    plot_graph1(city, "reports/graph1.png")
    plot_graph2(active_hosts_history, "reports/graph2_v0.png")
