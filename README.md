# FC Barcelona vs Real Madrid Analysis

A comprehensive data analysis tool for comparing Barcelona and Real Madrid statistics with special focus on El Clásico head-to-head matchups.

## Features
- **Team Statistics**: Goals, assists, possession, shots, etc.
- **El Clásico Analysis**: Historical H2H records, MVPs, key moments
- **Leaderboards**: Top scorers, assists, appearances
- **Visualizations**: Interactive charts and plots
- **Interesting Facts**: Key statistics and records

## Project Structure
```
clasico-analysis/
├── data/
│   ├── barcelona_stats.csv
│   ├── real_madrid_stats.csv
│   └── clasico_matches.csv
├── notebooks/
│   └── analysis.ipynb
├── src/
│   ├── data_loader.py
│   ├── analyzer.py
│   └── visualizer.py
├── requirements.txt
└── README.md
```

## Setup
```bash
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb
```

## Data Sources
- Football-Data.co.uk API
- ESPN API
- Manual data compilation from official records
