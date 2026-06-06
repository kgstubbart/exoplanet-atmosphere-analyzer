# exoplanet-atmosphere-analyzer
This project analyizes exoplanet atmosphere's from transmission spectra. The goal is to be able to predict common gasses and temperature. 

exoplanet-retrieval/
├── README.md
├── environment.yml          # conda environment spec
├── .gitignore
├── data/
│   ├── raw/                  # downloaded FITS — never edit, never commit large files
│   └── processed/            # your cleaned spectra
├── src/
│   ├── __init__.py
│   ├── data_acquisition.py   
│   ├── preprocessing.py      
│   ├── forward_model.py      
│   ├── likelihood.py        
│   └── retrieval.py          
├── notebooks/                # exploration; not the source of truth
├── tests/
├── results/                  # plots and posterior outputs
└── docs/
