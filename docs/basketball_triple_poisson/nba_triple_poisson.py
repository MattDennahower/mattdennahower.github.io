from scipy.stats import poisson
import scipy
from scipy.optimize import fsolve
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

# Create a function that converts odds to decimal odds
def odds_conversion(odds):

    if odds < 0:
        decimal_odds = (100/abs(odds)) + 1
    elif odds < 100 and odds > 1:
        decimal_odds = odds
    elif odds > 100:
        decimal_odds = (odds/100) + 1

    return decimal_odds

odds_conversion(1.724)

# Create a function that calculates the expected value of a bet
def EV(implied_prob, line):
    line = odds_conversion(line)
    return   implied_prob*line - 1

def basketball_poisson(ft_mean, two_pt_mean, three_pt_mean, tot_points):
    prob = 0
    for num_3pt in range(20):
        for num_2pt in range(20):
            for num_ft in range(20):
                points = num_3pt*3 + num_2pt*2 + num_ft
                if points <= tot_points:
                    prob += poisson.pmf(num_3pt,three_pt_mean)*poisson.pmf(num_2pt,two_pt_mean)*poisson.pmf(num_ft,ft_mean)
                else:
                    break
    return prob



def odds_to_implied_prob(over,under):

    over_implied = round((1/over)/((1/over)+(1/under)),5)
    under_implied = round(1 - over_implied,5)
    result = f'Implied Prob of Over {over_implied} and Implied Prob of Under {under_implied}'
    return over_implied, under_implied

odds_to_implied_prob(2.05,1.724)


threes = 2.5
under_prob = 0.492

def m(mean):

    prob = poisson.cdf(threes, mean) - under_prob 

    return prob

three_pt_mean = float(fsolve(m, 1))

three_pt_mean




three_pt_mean = 3
tot_pts_m = 30

two_pt_avg = 8.2
ft_avg = 8.9

def big(c):

    yes = 3*three_pt_mean + 2*two_pt_avg*c + ft_avg*c - tot_pts_m

    return yes

adjustment_factor = fsolve(big, 1)


c = float(adjustment_factor)

ft_mean = ft_avg*c
two_pt_mean = two_pt_avg*c

ft_mean, two_pt_mean,c



tot_points = 28.5
under_implied = 0.506
adjustment_factor = 1
two_pt_avg = 8.14
ft_avg = 4.47


def f(c):

    prob = basketball_poisson(ft_avg*c,two_pt_avg*c,three_pt_mean,tot_points) - 0.506
    return prob

adjustment_factor = fsolve(f, 1)
adjustment_factor




under_poisson = basketball_poisson(ft_mean,two_pt_mean, three_pt_mean, 29.5)
under_poisson

soft_decimal_odds = 1.9

EV(under_poisson, soft_decimal_odds)

#TriplePoisonModel

def over_prob(ft_avg, two_pt_avg, three_mean, over, under, mark_tot, alt_tot):
    under = odds_conversion(under)
    over = odds_conversion(over)
    adj = 0
    def basketball_poisson(ft_mean, two_pt_mean, three_pt_mean, tot_points):
        p = 0
        for num_3pt in range(20):
            for num_2pt in range(20):
                for num_ft in range(20):
                    points = num_3pt*3 + num_2pt*2 + num_ft
                    if points <= tot_points:
                        p += poisson.pmf(num_3pt,three_pt_mean)*poisson.pmf(num_2pt,two_pt_mean)*poisson.pmf(num_ft,ft_mean)
                    else:
                        break
        return p

    def f(c):    
        prob = basketball_poisson(ft_avg*c,two_pt_avg*c,three_pt_mean,mark_tot) - under
        return prob
    adj = fsolve(f, 1)  

    ft_mean = ft_avg*adj
    two_pt_mean = two_pt_avg

    return 1 - basketball_poisson(ft_mean,two_pt_mean,three_mean,alt_tot)
    

over_prob()