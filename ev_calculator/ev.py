import numpy as np
from scipy.stats import norm
from scipy.optimize import fsolve

def implied_prob(odds): 
    """Convert American odds to implied probability"""
    if odds > 0:
        return 100 / (odds + 100)
    else:
        return -odds / (-odds + 100)

def prob_to_odds(prob):
    """Convert implied probability to American odds"""
    if prob < 0.5:
        return round(100 / prob - 100)
    else:
        return round(-100 / (1 - prob) + 100)

def remove_vig(odds_sets):
    """Iterate through all the sets of odds and remove the vig from each set
    
    Args:
        *odds_sets: A variable number of odds sets to remove the vig from 
        
    Returns:
        list: A list of lists, each containing the adjusted odds for each set
    """
    adjusted_odds = []
    adjusted_probs = []
    
    for odds in odds_sets:
        probabilities = [implied_prob(odd) for odd in odds]
        
        # Convert raw probabilities to z-scores
        z_scores = [norm.ppf(prob) for prob in probabilities]
        
        # Find the adjustment factor c
        c = fsolve(lambda c: sum(norm.cdf(z + c) for z in z_scores) - 1, 0)[0]
        
        # Adjust z-scores
        z_adjusted = [z + c for z in z_scores]
        
        # Convert back to probabilities
        probabilities_novig = [norm.cdf(z_adj) for z_adj in z_adjusted]
        
        # Convert adjusted probabilities to American odds
        odds_novig = [prob_to_odds(prob) for prob in probabilities_novig]
        
        adjusted_odds.append(odds_novig)
        adjusted_probs.append(probabilities_novig)  # Save the adjusted probabilities
    
    return adjusted_odds, adjusted_probs  # Return both adjusted odds and probabilities

def calculate_fair_value(combined_prob):
    """Convert combined probability to fair odds."""
    if combined_prob > 0:
        if combined_prob < 0.5:  # For probabilities less than 0.5
            fair_odds = (1 / combined_prob - 1) * 100  # Convert probability to fair odds
        else:  # For probabilities greater than or equal to 0.5
            fair_odds = -100 / (1 - combined_prob) + 100  # Adjusted formula for negative odds
        return f"+{round(fair_odds)}" if fair_odds > 0 else str(round(fair_odds))  # Format with + if positive
    return "0"  # Return "0" if combined probability is 0 or negative


def calculate_combined_probability(odds_sets):
    """Calculate the combined probability by multiplying the implied probabilities of the first value of each set."""
    if len(odds_sets) == 1:  # Check if there's only one set of odds
        return odds_sets[0][0]  # Return the first probability of the single event
    combined_prob = 1.0
    for odds_set in odds_sets:
        first_prob = odds_set[0]  # Get the first odd from the set
        combined_prob *= first_prob  # Multiply the implied probabilities
    return combined_prob

def calculate_expected_value(bet_odds, fair_prob):
    """Calculate expected value based on the bet odds and fair probability."""
    bet_prob = implied_prob(bet_odds)
    
    # Adjust expected value calculation based on the sign of bet_odds
    if bet_odds > 0:  # Positive odds
        expected_value = fair_prob * (bet_odds / 100) - (1 - fair_prob)
    else:  # Negative odds
        expected_value = fair_prob * (100 / abs(bet_odds)) - (1 - fair_prob)
    
    return expected_value

def calculate_quarter_kelly(bet_odds, fair_prob):
    """Calculate quarter Kelly percentage based on bet odds and fair probability."""
    bet_prob = implied_prob(bet_odds)
    
    # Adjust quarter Kelly calculation based on the sign of bet_odds
    if bet_odds > 0:  # Positive odds
        quarter_kelly = (fair_prob - (1 - fair_prob) / (bet_odds / 100)) / 4 * 100
    else:  # Negative odds
        quarter_kelly = (fair_prob - (1 - fair_prob) / (100 / abs(bet_odds))) / 4 * 100
    
    return quarter_kelly

def parse_odds_input(odds_input):
    """Parse a string of odds into a list of floats"""
    odds_list = []
    for odds_set in odds_input.split(','):
        # Split each set by '/' and convert to float
        odds = [float(odd) for odd in odds_set.split('/')]
        odds_list.extend(odds)  # Add the odds to the main list
    return odds_list

# Example usage
odds_input = input("Enter odds in the format '700/-900,300/-350,125/352/221': ")
odds_sets = [list(map(float, odds_set.split('/'))) for odds_set in odds_input.split(',')]
odds_novig, probs_novig = remove_vig(odds_sets)  # Get both adjusted odds and probabilities

# Input for bet odds
bet_odds = float(input("Enter your bet odds in American format (e.g., 700 or -900): "))

# Calculate the combined probability using the fair probabilities
combined_prob = calculate_combined_probability(probs_novig)

# Calculate expected value and quarter Kelly percentage
expected_value = calculate_expected_value(bet_odds, combined_prob)

# Calculate quarter kelly
quarter_kelly = calculate_quarter_kelly(bet_odds, combined_prob)

# Calculate fair value (FV) from combined probability
fair_value = calculate_fair_value(combined_prob)

# Print results
print(f"Adjusted American Odds: {odds_novig}")
print(f"EV: {expected_value * 100:.2f}%    QK: {quarter_kelly:.4f}%")
print(f"FV: {fair_value}")