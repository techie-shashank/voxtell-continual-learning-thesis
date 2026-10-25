"""Rebuild every result artefact from results/hpc in the right order.

  1. build_experiment_index.py  -> results/experiment_index.csv (keeps label/role/notes)
  2. extract_per_volume.py      -> thesis/tables/per_volume_dice.csv
  3. compute_cl_metrics.py      -> thesis/tables/cl_metrics.csv
     compare_strategies.py      -> thesis/tables/cl_differences.csv (paired bootstrap of differences)
  4. make_results_tables.py     -> thesis/tables/ch6_*.tex
     make_setup_tables.py       -> thesis/tables/ch6_experiments.tex, ch6_hparams.tex, ch6_strategy_params.tex
     make_appendix_tables.py    -> thesis/tables/appA_volumes.tex, appA_matrices.tex
  5. plot_results.py            -> thesis/figures/ch6_*.pdf
  6. make_compute_table.py      -> thesis/tables/compute.csv, ch6_compute.tex
  7. selected_epochs.py         -> thesis/tables/selected_epochs.csv
     build_tikz.py              -> thesis/figures/ch*_*.pdf (TikZ sources in thesis/figures/tikz/)
  8. plot_data.py              -> thesis/tables/ch4_*.tex, thesis/figures/ch4_*.pdf
                                   (only if results/data_stats/ exists; it is produced on
                                   the HPC by scripts/hpc/data_stats.py)
  9. make_diagram_assets.py    -> thesis/figures/tikz/knee_patch*.png (same condition as 8)

Usage (from the repository root):
    python scripts/run_all.py
"""
import subprocess
import sys
from pathlib import Path

STEPS = ["build_experiment_index.py", "extract_per_volume.py", "compute_cl_metrics.py",
         "compare_strategies.py", "make_results_tables.py", "make_setup_tables.py", "make_appendix_tables.py", "plot_results.py", "make_compute_table.py", "selected_epochs.py", "build_tikz.py"]

if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    for step in STEPS:
        print(f"== {step}")
        subprocess.run([sys.executable, str(here / step)], check=True)
    if (here.parent / "results" / "data_stats").exists():
        print("== plot_data.py")
        subprocess.run([sys.executable, str(here / "plot_data.py")], check=True)
        print("== make_diagram_assets.py")
        subprocess.run([sys.executable, str(here / "make_diagram_assets.py")], check=True)
    else:
        print("== plot_data.py skipped: results/data_stats/ not found (run scripts/hpc/data_stats.py on the HPC)")
