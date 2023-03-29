from scipy.stats import norm
from scipy.optimize import root_scalar

def prob(c, mu, sigma):
    return 2 * (1 - norm.cdf(c, mu, sigma))

mu = 0
sigma = 1
target_p = 0.51

sol = root_scalar(lambda c: prob(c, mu, sigma) - target_p, bracket=[0.1, 100])

print(sol.root)
