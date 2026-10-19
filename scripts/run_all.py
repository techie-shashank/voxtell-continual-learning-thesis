"""Rebuild every result artefact from results/hpc in the right order.

  1. build_experiment_index.py  -> results/experiment_index.csv (keeps label/role/notes)
  2. extract_per_volume.py      -> thesis/tables/per_volume_dice.csv
  3. compute_cl_metrics.py      -> thesis/tables/cl_metrics.csv
  4. make_results_tables.py     -> thesis/tables/ch6_*.tex
  5. plot_results.py            -> thesis/figures/ch6_*.pdf
  6. make_compute_table.py      -> thesis/tables/compute.csv, ch6_compute.tex
  7. plot_data.py               -> thesis/tables/ch4_*.tex, thesis/figures/ch4_*.pdf
                                   (only if results/data_stats/ exists; it is produced on
                                   the HPC by scripts/hpc/data_stats.py)

Usage (from the repository root):
    python scripts/run_all.py
"""
import subprocess
import sys
from pathlib import Path

STEPS = ["build_experiment_index.py", "extract_per_volume.py", "compute_cl_metrics.py",
         "make_results_tables.py", "plot_results.py", "make_compute_table.py"]

if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    for step in STEPS:
        print(f"== {step}")
        subprocess.run([sys.executable, str(here / step)], check=True)
    if (here.parent / "results" / "data_stats").exists():
        print("== plot_data.py")
        subprocess.run([sys.executable, str(here / "plot_data.py")], check=True)
    else:
        print("== plot_data.py skipped: results/data_stats/ not found (run scripts/hpc/data_stats.py on the HPC)")
