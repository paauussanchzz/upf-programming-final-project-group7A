# Airbnb Market Simulation & Real Data Analysis (Group 7A)

Final Project for **Programming (21960)** — Universitat Pompeu Fabra (UPF).

## Group Members
- **Pau Sánchez Llopis** (`paauussanchzz`)
- **Blanca Santos i Trias**
- **Jana Saguer Amills**
- **Bru Raga Derid**

## Repository Structure
- `src/final_project/`: Core simulation classes (`place.py`, `host.py`, `city.py`).
- `main.py`: Entry point to run the simulation and generate `reports/graph1.png`, `reports/graph2_v0.png`, and `reports/graph2_v1.png`.
- `notebooks/part2.ipynb`: Exploratory analysis of real Airbnb listings in Barcelona and Madrid.
- `reports/`: Generated figures (`graph1.png`, `graph2_v0.png`, `graph2_v1.png`, `graph3.png`) and final slides (`presentation.pdf`).

## Installation & Execution
```bash
conda env create -f environment.yml
conda activate final-project
pip install -e .
python main.py
