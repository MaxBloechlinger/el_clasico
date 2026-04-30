import pandas as pd
import numpy as np

class Analyzer:
    """Analyze Barcelona vs Real Madrid statistics"""
    
    def __init__(self, barca_stats, madrid_stats, clasico_matches):
        self.barca_stats = barca_stats
        self.madrid_stats = madrid_stats
        self.clasico_matches = clasico_matches
    
    def compare_teams(self):
        """Compare overall team statistics"""
        comparison = pd.DataFrame({
            'Barcelona': self.barca_stats.iloc[-1],
            'Real Madrid': self.madrid_stats.iloc[-1]
        })
        return comparison
    
    def calculate_clasico_record(self):
        """Calculate El Clásico head-to-head record"""
        barcelona_wins = (self.clasico_matches['Barcelona_Goals'] > 
                         self.clasico_matches['Real_Madrid_Goals']).sum()
        draws = (self.clasico_matches['Barcelona_Goals'] == 
                self.clasico_matches['Real_Madrid_Goals']).sum()
        real_madrid_wins = (self.clasico_matches['Barcelona_Goals'] < 
                           self.clasico_matches['Real_Madrid_Goals']).sum()
        
        record = {
            'Barcelona Wins': barcelona_wins,
            'Draws': draws,
            'Real Madrid Wins': real_madrid_wins,
            'Barcelona Goals': self.clasico_matches['Barcelona_Goals'].sum(),
            'Real Madrid Goals': self.clasico_matches['Real_Madrid_Goals'].sum(),
            'Total Matches': len(self.clasico_matches),
            'Barcelona Avg Possession': self.clasico_matches['Barcelona_Possession'].mean(),
            'Real Madrid Avg Possession': self.clasico_matches['Real_Madrid_Possession'].mean()
        }
        return record
    
    def get_clasico_mvps(self):
        """Get most frequent MVPs in El Clásico"""
        mvp_counts = self.clasico_matches['MVP'].value_counts()
        return mvp_counts
    
    def calculate_interesting_facts(self):
        """Generate interesting facts about the rivalry"""
        facts = []
        
        # Calculate facts
        barca_last = self.barca_stats.iloc[-1]
        madrid_last = self.madrid_stats.iloc[-1]
        
        goals_diff = abs(barca_last['Goals'] - madrid_last['Goals'])
        possession_diff = abs(barca_last['Possession'] - madrid_last['Possession'])
        
        record = self.calculate_clasico_record()
        
        facts.append(f"Barcelona has won {record['Barcelona Wins']} out of {record['Total Matches']} recent El Clásicos")
        facts.append(f"In the latest season, Barcelona averaged {record['Barcelona Avg Possession']:.1f}% possession vs Madrid's {record['Real_Madrid Avg Possession']:.1f}%")
        facts.append(f"Total goals scored: Barcelona {record['Barcelona Goals']} vs Real Madrid {record['Real Madrid Goals']}")
        facts.append(f"Most frequent MVP: {self.clasico_matches['MVP'].value_counts().index[0]}")
        facts.append(f"Highest attendance: {self.clasico_matches['Attendance'].max():,} fans")
        
        return facts
    
    def get_team_trends(self, team_stats, team_name):
        """Get performance trends over seasons"""
        trends = {
            'Team': team_name,
            'Seasons': team_stats['Season'].tolist(),
            'Goals': team_stats['Goals'].tolist(),
            'Wins': team_stats['Wins'].tolist(),
            'Possession': team_stats['Possession'].tolist(),
            'Avg_Goals_Per_Season': team_stats['Goals'].mean(),
            'Win_Rate': (team_stats['Wins'].sum() / 
                        (team_stats['Wins'].sum() + team_stats['Draws'].sum() + team_stats['Losses'].sum())) * 100
        }
        return trends
