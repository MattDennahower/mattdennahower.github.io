from scipy.stats import poisson
from scipy.optimize import fsolve

# Create a function to convert American odds to decimal odds
def odds_conversion(odds):

    if odds < 0:
        decimal_odds = (100/abs(odds)) + 1
    elif odds < 100 and odds > 1:
        decimal_odds = odds
    elif odds > 100:
        decimal_odds = (odds/100) + 1

    return decimal_odds

# Create a function to calculate the expected value
def ev(implied_prob, line):
    line = odds_conversion(line)
    return   implied_prob*line - 1

# Create a function to convert implied probability to American odds
def implied_prob_to_amer_odds(implied_prob):
    return round(1/implied_prob,2) - 100

# Create a Triple Poisson Model to calculate the probability of a player scoring a certain number of points and making a certain number of 3-pointers
def pts_over_3ptm_over(total_pts,total_3ptm,mean_3ptm,mean_2ptm,mean_ftm):
    cum_prob = 0
    for made_3p in range(0,20):
        for made_2p in range(0,20):
            for made_ft in range(0,20):
                if made_3p >= total_3ptm and 3*made_3p + 2*made_2p + made_ft >= total_pts:
                    cum_prob += poisson.pmf(made_3p,mean_3ptm)*poisson.pmf(made_2p,mean_2ptm)*poisson.pmf(made_ft,mean_ftm)
    return cum_prob

# Define the parameters for Player 1
p1_total_pts = 34.5
p1_total_3ptm = 4.5
p1_mean_3ptm = 2.917176
p1_mean_2ptm = 5.782439
p1_mean_ftm = 5.396943067

p1_win_prob = pts_over_3ptm_over(p1_total_pts,p1_total_3ptm,p1_mean_3ptm,p1_mean_2ptm,p1_mean_ftm)
print(f"Fair Value Player 1 = +{round(implied_prob_to_amer_odds(p1_win_prob / 100))}")

# Define the parameters for Player 2
p2_total_pts = 29.5
p2_total_3ptm = 5.5
p2_mean_3ptm = 3.1978
p2_mean_2ptm = 4.379432
p2_mean_ftm = 2.189716

p2_win_prob = pts_over_3ptm_over(p2_total_pts,p2_total_3ptm,p2_mean_3ptm,p2_mean_2ptm,p2_mean_ftm)
print(f"Fair Value Player 2 = +{round(implied_prob_to_amer_odds(p2_win_prob / 100))}")

# Calculate the fair value for the combo
win_prob = p1_win_prob * p2_win_prob
print(f"Fair Value Combo = +{round(implied_prob_to_amer_odds(win_prob / 100))}") 

sb_odds = 25000
print(F"Expected Value = {round(ev(win_prob, sb_odds)*100,2)}%")