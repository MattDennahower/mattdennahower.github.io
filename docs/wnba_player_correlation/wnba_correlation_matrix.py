import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('wnba_2024.csv')

# Define the statistic you're interested in
values = 'TRB'  # Change this to the statistic you want

# Define the team you're interested in
team_to_plot = ''  # Change this to the team you want, leave empty to process all teams

# Get the list of teams to process
teams_to_process = data['team_id'].unique() if not team_to_plot else [team_to_plot]

# For each unique team in the data
for team in data['team_id'].unique():
    # Filter the data for the current team
    team_data = data[data['team_id'] == team]
    
    # Pivot the filtered data so that each row is a game, each column is a player, and the values are assists
    pivot_data = team_data.pivot(index='game_id', columns='Starters', values=values)
    
    # Compute the correlation matrix for assists
    assists_corr = pivot_data.corr()
    
    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(10, 10))
    sns.heatmap(assists_corr, cmap='coolwarm', center=0, annot=False)
    plt.title(f'Correlation Matrix of {values} between Players for Team {team}')
    plt.show()