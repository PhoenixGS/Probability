from scipy.stats import norm

mu = 0
sigma = 1
p = 0.95

b = norm.ppf((1 + p) / 2, mu, sigma)

print(b)
