#!/usr/bin/env python3
"""
Barcelona vs Real Madrid Analysis Script
Runs the complete analysis from the notebook
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Import custom modules
from data_loader import DataLoader
from analyzer import Analyzer
from visualizer import Visualizer

def main():
    print("⚽ FC BARCELONA VS REAL MADRID ANALYSIS")
    print("=" * 50)

    # Initialize components
    loader = DataLoader()

    # Load data
    print("\n📂 Loading data...")
    barca_stats = loader.load_team_stats('barcelona')
    madrid_stats = loader.load_team_stats('real_madrid')
    clasico_matches = loader.load_clasico_matches()

    if barca_stats is None or madrid_stats is None or clasico_matches is None:
        print("❌ Data not found. Creating sample data...")
        barca_stats, madrid_stats, clasico_matches = loader.create_sample_data()

    print("✅ Data loaded successfully!")

    # Display basic info
    print(f"\nBarcelona seasons: {len(barca_stats)}")
    print(f"Real Madrid seasons: {len(madrid_stats)}")
    print(f"El Clásico matches: {len(clasico_matches)}")

    # Initialize analyzer with data
    analyzer = Analyzer(barca_stats, madrid_stats, clasico_matches)
    visualizer = Visualizer()

    # Run analysis
    print("\n🔍 Running analysis...")

    # Team comparison
    print("\n📊 TEAM STATISTICS COMPARISON")
    print("=" * 40)
    team_comparison = analyzer.compare_teams()
    print(team_comparison)

    # El Clásico analysis
    print("\n🏆 EL CLÁSICO ANALYSIS")
    print("=" * 30)
    clasico_record = analyzer.calculate_clasico_record()
    print("El Clásico Record:")
    for key, value in clasico_record.items():
        print(f"  {key}: {value}")
    
    mvp_counts = analyzer.get_clasico_mvps()
    print(f"\nEl Clásico MVPs:\n{mvp_counts}")

    # Create visualizations
    print("\n📈 Creating visualizations...")

    try:
        # Goals comparison chart
        fig1 = visualizer.plot_goals_scored(barca_stats, madrid_stats)
        plt.savefig('goals_comparison.png', dpi=150, bbox_inches='tight')
        print("✅ Goals comparison chart saved as 'goals_comparison.png'")
        plt.close()
    except Exception as e:
        print(f"⚠️ Could not create goals chart: {e}")

    try:
        # El Clásico results chart
        fig2 = visualizer.plot_clasico_record(clasico_record)
        plt.savefig('clasico_results.png', dpi=150, bbox_inches='tight')
        print("✅ El Clásico results chart saved as 'clasico_results.png'")
        plt.close()
    except Exception as e:
        print(f"⚠️ Could not create clasico chart: {e}")

    try:
        # Interactive dashboard
        print("\n🎯 Creating interactive dashboard...")
        dashboard = visualizer.create_interactive_dashboard(barca_stats, madrid_stats, clasico_matches)
        print("✅ Interactive dashboard created!")
    except Exception as e:
        print(f"⚠️ Could not create dashboard: {e}")

    print("\n🎉 Analysis complete!")
    print("\nNext steps:")
    print("1. View the generated PNG charts in your project folder")
    print("2. For the interactive dashboard, run the notebook in Jupyter")
    print("3. To get real data, check the README for API sources")