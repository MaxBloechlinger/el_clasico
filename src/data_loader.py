import pandas as pd
import numpy as np
from pathlib import Path

class DataLoader:
    """Load and manage Barcelona vs Real Madrid data"""
    
    def __init__(self, data_dir='data'):
        self.data_dir = Path(data_dir)
    
    def load_team_stats(self, team_name):
        """Load team statistics from CSV"""
        filepath = self.data_dir / f"{team_name.lower()}_stats.csv"
        if filepath.exists():
            return pd.read_csv(filepath)
        else:
            print(f"File {filepath} not found. Create it with sample data first.")
            return None
    
    def load_clasico_matches(self):
        """Load El Clásico historical matches"""
        filepath = self.data_dir / "clasico_matches.csv"
        if filepath.exists():
            return pd.read_csv(filepath)
        else:
            print(f"File {filepath} not found. Create it with sample data first.")
            return None
    
    def create_sample_data(self):
        """Create sample data for testing"""
        # Sample Barcelona stats
        barcelona_stats = pd.DataFrame({
            'Season': ['2022-23', '2023-24', '2024-25'],
            'Goals': [90, 95, 88],
            'Assists': [45, 52, 48],
            'Shots': [320, 350, 330],
            'Possession': [63.2, 62.1, 64.5],
            'Tackles': [450, 470, 460],
            'Wins': [28, 27, 26],
            'Draws': [4, 3, 5],
            'Losses': [2, 4, 3]
        })
        
        # Sample Real Madrid stats
        real_madrid_stats = pd.DataFrame({
            'Season': ['2022-23', '2023-24', '2024-25'],
            'Goals': [92, 94, 91],
            'Assists': [48, 50, 47],
            'Shots': [330, 325, 335],
            'Possession': [58.1, 59.2, 57.8],
            'Tackles': [480, 475, 485],
            'Wins': [29, 28, 27],
            'Draws': [3, 3, 4],
            'Losses': [2, 3, 3]
        })
        
        # Sample El Clásico matches
        clasico_matches = pd.DataFrame({
            'Date': ['2022-10-16', '2023-03-19', '2023-10-28', '2024-04-21', '2024-11-30'],
            'Competition': ['La Liga', 'Copa del Rey', 'La Liga', 'La Liga', 'La Liga'],
            'Venue': ['Camp Nou', 'Santiago Bernabéu', 'Camp Nou', 'Santiago Bernabéu', 'Camp Nou'],
            'Barcelona_Goals': [1, 3, 2, 1, 2],
            'Real_Madrid_Goals': [0, 1, 1, 2, 1],
            'Barcelona_Possession': [65.2, 62.1, 64.8, 61.2, 66.1],
            'Real_Madrid_Possession': [34.8, 37.9, 35.2, 38.8, 33.9],
            'MVP': ['Lewandowski', 'Gavi', 'De Jong', 'Benzema', 'Gundogan'],
            'Attendance': [99354, 80354, 99354, 80354, 99354],
            'Key_Events': [
                'Dominated possession',
                'Barcelona comeback win',
                'Close contest',
                'Real Madrid resilience',
                'Barcelona control'
            ]
        })
        
        # Save to CSV
        barcelona_stats.to_csv(self.data_dir / 'barcelona_stats.csv', index=False)
        real_madrid_stats.to_csv(self.data_dir / 'real_madrid_stats.csv', index=False)
        clasico_matches.to_csv(self.data_dir / 'clasico_matches.csv', index=False)
        
        print("Sample data created successfully!")
        return barcelona_stats, real_madrid_stats, clasico_matches
