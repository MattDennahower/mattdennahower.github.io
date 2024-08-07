import requests
import pandas as pd
import time
from bs4 import BeautifulSoup

# URL containing each of the matches and their respective links
# Update this with the current season or previous season's
url = 'https://fbref.com/en/comps/9/2023-2024/schedule/2023-2024-Premier-League-Scores-and-Fixtures'

output_file = 'match_links.csv'

def get_match_links(url, output_file):

    url_prefix = 'https://fbref.com'
    
    response = requests.get(url)  # Send GET request

    if response.status_code == 200:  # Check if the request was successful
        
        # Process the response data
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        tables = pd.read_html(data)
        
        # Create a DataFrame from the HTML table
        df = tables[0]
        
        # Remove rows where the 'Wk' column is NaN
        df = df[df['Wk'].notna()]
        
        # Reset the index of the DataFrame
        df.reset_index(drop=True, inplace=True)
        
        # Find all 'tr' elements in the HTML
        table_rows = soup.find_all('tr')
        
        # Filter the rows to only include rows that have a 'td' element with the 'data-stat' attribute set to 'week_num'
        table_rows = [row for row in table_rows if row.find('td', {'data-stat': 'week_num'})]
        
        # Find all 'a' elements with the text 'Match Report' in the HTML
        match_report_links = soup.find_all('a', text='Match Report')
        
        # Extract the 'Match Report' link from each row
        links = [url_prefix + link['href'] for link in match_report_links]
        
        # Create a new 'Match Report' column in the DataFrame
        df['Match Report'] = pd.Series(links)
        
        # Save the DataFrame to a CSV file
        df.to_csv(output_file, index=False)
        print('Data saved to', output_file)
        
    else:
        print('Failed to retrieve data. Status code:', response.status_code)

def get_match_data(url, home_team, away_team):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        tables = pd.read_html(data, header=1)  # Skip the first row when reading the table
        combined_table = pd.DataFrame()

        for i, table in enumerate(tables):
            if i == 3 or i == 10:  # 4th and 11th tables have indices 3 and 10
                table = table.iloc[:-1]  # Remove the last row
                team = home_team if i == 3 else away_team  # Assign the team name based on the table index
                table['Team'] = team  # Add a new 'Team' column
                
                # Clean the 'Nation' column
                if 'Nation' in table.columns:
                    table['Nation'] = table['Nation'].apply(lambda x: ''.join([c for c in x.split()[-1] if c.isupper()]))
                
                combined_table = pd.concat([combined_table, table], ignore_index=True)

        return combined_table
    else:
        print('Failed to retrieve data. Status code:', response.status_code)
        return pd.DataFrame()  # Return an empty DataFrame on failure

def process_all_matches(df):
    all_matches_data = pd.DataFrame()

    total_games = len(df)
    for i, (index, row) in enumerate(df.iterrows()):

        match_data = get_match_data(row['Match Report'], row['Home'], row['Away'])
        all_matches_data = pd.concat([all_matches_data, match_data], ignore_index=True)

        # Print a message indicating the game saved
        print(f'Game {i+1} of {total_games} saved.')

        # Wait for 5 seconds before moving to the next match link
        time.sleep(5)

    # Save all match data to a CSV file
    all_matches_data.to_csv('all_matches_data.csv', index=False)
    print('All match data saved to all_matches_data.csv.')

    # Print a completed message
    print('Completed saving all games.')

def main():
    get_match_links(url, output_file)
    df = pd.read_csv(output_file)
    process_all_matches(df)
    
if __name__ == '__main__':
    main()


