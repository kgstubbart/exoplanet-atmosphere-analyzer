# Exoplanet Atmosphere Analyzer

This project analyzes exoplanet atmospheres using transmission spectra. The goal is to predict common atmospheric gases and estimate atmospheric temperature.

## Project Structure

```text
exoplanet-retrieval/
├── README.md
├── environment.yml          # Conda environment specification
├── .gitignore
├── data/
│   ├── raw/                 # Downloaded FITS files; never edit or commit large files
│   └── processed/           # Cleaned spectra
├── src/
│   ├── __init__.py
│   ├── data_acquisition.py
│   ├── preprocessing.py
│   ├── forward_model.py
│   ├── likelihood.py
│   └── retrieval.py
├── notebooks/               # Exploration; not the source of truth
├── tests/
├── results/                 # Plots and posterior outputs
└── docs/
```
