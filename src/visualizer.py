import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

class Visualizer:
    """Create visualizations for Barcelona vs Real Madrid analysis"""
    
    def __init__(self, style='seaborn-v0_8-darkgrid'):
        sns.set_style(style)
        self.colors = {'Barcelona': '#004687', 'Real Madrid': '#FDBF0B'}
    
    def plot_team_comparison(self, comparison_df, metric='Goals'):
        """Plot team comparison for a specific metric"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        teams = comparison_df.index
        values = comparison_df[metric]
        colors_list = [self.colors.get(team, '#999') for team in teams]
        
        bars = ax.bar(teams, values, color=colors_list, alpha=0.8, edgecolor='black', linewidth=1.5)
        ax.set_ylabel(metric, fontsize=12, fontweight='bold')
        ax.set_title(f'{metric} Comparison - Barcelona vs Real Madrid', fontsize=14, fontweight='bold')
        
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        return fig
    
    def plot_clasico_record(self, record_dict):
        """Plot El Clásico head-to-head record"""
        labels = ['Barcelona Wins', 'Draws', 'Real Madrid Wins']
        sizes = [record_dict['Barcelona Wins'], record_dict['Draws'], record_dict['Real Madrid Wins']]
        colors = ['#004687', '#808080', '#FDBF0B']
        
        fig, ax = plt.subplots(figsize=(10, 8))
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.0f%%',
                                           startangle=90, textprops={'fontsize': 11, 'weight': 'bold'})
        ax.set_title('El Clásico Head-to-Head Record', fontsize=14, fontweight='bold', pad=20)
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(12)
        
        plt.tight_layout()
        return fig
    
    def plot_possession_trend(self, clasico_matches):
        """Plot possession trends in El Clásico matches"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        matches = range(len(clasico_matches))
        ax.plot(matches, clasico_matches['Barcelona_Possession'], marker='o', 
               label='Barcelona', linewidth=2.5, markersize=8, color='#004687')
        ax.plot(matches, clasico_matches['Real_Madrid_Possession'], marker='s', 
               label='Real Madrid', linewidth=2.5, markersize=8, color='#FDBF0B')
        
        ax.set_xlabel('Match Number', fontsize=12, fontweight='bold')
        ax.set_ylabel('Possession %', fontsize=12, fontweight='bold')
        ax.set_title('Possession Trends in Recent El Clásicos', fontsize=14, fontweight='bold')
        ax.legend(fontsize=11, loc='best')
        ax.grid(True, alpha=0.3)
        ax.set_ylim([0, 100])
        
        plt.tight_layout()
        return fig
    
    def plot_goals_scored(self, barca_stats, madrid_stats):
        """Plot goals scored over seasons"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        seasons = barca_stats['Season']
        width = 0.35
        x = range(len(seasons))
        
        bars1 = ax.bar([i - width/2 for i in x], barca_stats['Goals'], width, 
                       label='Barcelona', color='#004687', alpha=0.8, edgecolor='black')
        bars2 = ax.bar([i + width/2 for i in x], madrid_stats['Goals'], width, 
                       label='Real Madrid', color='#FDBF0B', alpha=0.8, edgecolor='black')
        
        ax.set_xlabel('Season', fontsize=12, fontweight='bold')
        ax.set_ylabel('Goals Scored', fontsize=12, fontweight='bold')
        ax.set_title('Goals Scored by Season', fontsize=14, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(seasons)
        ax.legend(fontsize=11)
        
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{int(height)}', ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        return fig
    
    def create_interactive_dashboard(self, barca_stats, madrid_stats, clasico_matches):
        """Create interactive Plotly dashboard"""
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Goals Scored Over Seasons', 'El Clásico Record', 
                          'Possession in El Clásico', 'Wins Over Seasons'),
            specs=[[{'type': 'scatter'}, {'type': 'pie'}],
                   [{'type': 'scatter'}, {'type': 'bar'}]]
        )
        
        # Goals trend
        fig.add_trace(
            go.Scatter(x=barca_stats['Season'], y=barca_stats['Goals'], 
                      name='Barcelona', mode='lines+markers', line=dict(color='#004687', width=3)),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(x=madrid_stats['Season'], y=madrid_stats['Goals'], 
                      name='Real Madrid', mode='lines+markers', line=dict(color='#FDBF0B', width=3)),
            row=1, col=1
        )
        
        # Record pie
        record = {
            'Barcelona Wins': (clasico_matches['Barcelona_Goals'] > clasico_matches['Real_Madrid_Goals']).sum(),
            'Draws': (clasico_matches['Barcelona_Goals'] == clasico_matches['Real_Madrid_Goals']).sum(),
            'Real Madrid Wins': (clasico_matches['Barcelona_Goals'] < clasico_matches['Real_Madrid_Goals']).sum()
        }
        fig.add_trace(
            go.Pie(labels=list(record.keys()), values=list(record.values()),
                   marker=dict(colors=['#004687', '#808080', '#FDBF0B'])),
            row=1, col=2
        )
        
        # Possession scatter
        fig.add_trace(
            go.Scatter(x=clasico_matches.index, y=clasico_matches['Barcelona_Possession'],
                      name='Barcelona Possession', mode='lines+markers', line=dict(color='#004687')),
            row=2, col=1
        )
        fig.add_trace(
            go.Scatter(x=clasico_matches.index, y=clasico_matches['Real_Madrid_Possession'],
                      name='Real Madrid Possession', mode='lines+markers', line=dict(color='#FDBF0B')),
            row=2, col=1
        )
        
        # Wins bar chart
        fig.add_trace(
            go.Bar(x=barca_stats['Season'], y=barca_stats['Wins'], name='Barcelona Wins',
                   marker=dict(color='#004687')),
            row=2, col=2
        )
        fig.add_trace(
            go.Bar(x=madrid_stats['Season'], y=madrid_stats['Wins'], name='Real Madrid Wins',
                   marker=dict(color='#FDBF0B')),
            row=2, col=2
        )
        
        fig.update_layout(height=900, width=1400, showlegend=True,
                         title_text="Barcelona vs Real Madrid - El Clásico Analysis Dashboard",
                         title_font_size=18)
        
        return fig
